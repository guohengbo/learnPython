import pymysql

host = "127.0.0.1"
user = "root"
password = "wdfqiumo"
db = "polls"
connection = pymysql.connect(host=host,
    user=user,
    password=password,
    db=db,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor=connection.cursor()
# table_name="polls_question"
# real_sql = "delete from " + table_name + ";"
# cursor.execute("SET FOREIGN_KEY_CHECKS=0;")#去除外键约束,删除某个表要先删除外键约束才可以
real_sql="select * from polls_question;"
cursor.execute(real_sql)
c =cursor.fetchall()
for cc in c:
    print(cc)
connection.close()