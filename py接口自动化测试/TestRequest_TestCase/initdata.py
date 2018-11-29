from mysqlOperation import MySQLOperating

def insert_data(table, datas):
    db = MySQLOperating()
    db.clear(table)
    for data in datas:
        db.insert(table, data)
    db.close()

def select_data(table, datas,data2):
    db = MySQLOperating()
    for data in datas:
        db.select(table, data,data2)
    db.close()
table_poll_question = "polls_question"
datas_poll_question =[{'id': 1, 'question_text': '你喜欢的语言是什么?'}]
table_poll_choice = "polls_choice"
datas_poll_choice =[
    {'id': 1, 'choice_text': 'java', 'votes': 0, 'question_id': 1},
    {'id': 2, 'choice_text': 'python', 'votes': 0, 'question_id': 1},]

def init_data():
    insert_data(table_poll_question, datas_poll_question)
    insert_data(table_poll_choice, datas_poll_choice)

if __name__ == '__main__':
    init_data()