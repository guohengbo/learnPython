import pymysql.cursors
import configparser
from testdata.getpath import GetTestConfig

config = configparser.ConfigParser()
config.read(GetTestConfig("dbconfig.conf"))
db='pyTest'
host = config[db]['host']
user = config[db]['user']
password = config[db]['passwd']
db = config[db]['db']

class MySQLOperating():
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
            user=user,
            password=password,
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as e: 
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
            self.connection.commit()
    def insert(self, table_name, data):
        for key in data:
            data[key] = "'"+str(data[key])+"'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value +")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()
    #select question_text from polls_question where id=1;
    def select(self, table_name, data,data2):
        key = ','.join(data.keys())
        case=''.join(data2.replace('{','').replace('}','').replace(':','=')[1:].split()).replace("'=","=").replace(",'"," and ")
        real_sql = "select " + key + " from " + table_name  +" where " +case+ ";"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            c =cursor.fetchall()
            for cc in c:
                print(cc)
            self.connection.commit()
    #UPDATE table_name SET field1=new-value1, field2=new-value2[WHERE Clause]
    def upate(self, table_name, data,data2):
        values=''.join(data.replace('{','').replace('}','').replace(':','=')[1:].split()).replace("'=","=").replace(",'",",")
        case=''.join(data2.replace('{','').replace('}','').replace(':','=')[1:].split()).replace("'=","=").replace(",'"," and ")
        real_sql="update "+ table_name +" set "+ values +" where "+ case + ";"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()
    def close(self):
        self.connection.close()

if __name__ == '__main__':
    db = MySQLOperating()
    table_name = "polls_question"
    # data = {'id':1, 'question_text':'你喜欢的游戏是什么？'}
    # db.clear(table_name)
    # db.insert(table_name, data)
    # data="{'question_text':'你喜欢的歌曲是什么？'}"
    data={'question_text':'你喜欢的歌曲是什么？'}
    data2="{'id':1}"
    # db.upate(table_name,data,data2)
    db.select(table_name,data,data2)
    db.close()