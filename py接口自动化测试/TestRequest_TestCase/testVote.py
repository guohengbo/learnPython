import xlrd
from TestRequest import *
from testdata.getpath import GetTestDataPath

Testdata = xlrd.open_workbook(GetTestDataPath())

testUrl="http://127.0.0.1:8000"
def post_vote():
    try:
        table = Testdata.sheets()[1]
        for i in range(3,5):
            choice=table.cell(i,0).value
            status=table.cell(i,1).value
            expect=table.cell(i,2).value

            hdata={
                "choice":int(choice)
            }
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testCaseid="1-1"
            testName="TestVote"+testCaseid
            testHope=str(int(status))
            response_testhope=expect
            r =testPostRequest(testUrl+'/polls/1/vote/',hdata,header,testCaseid,testName,testHope,response_testhope)
            # print(r)
    except Exception as e:
        print(e)
        
def get_polls():
    try:
        table = Testdata.sheets()[1]
        for i in range(13,14):
            status=table.cell(i,0).value
            expect=table.cell(i,1).value
            hdata={}
            header = {
                'content-type': "application/json;charset=UTF-8"
            }
            testCaseid="2-1"
            testName="TestPolls"+testCaseid
            testHope=str(int(status))
            response_testhope=expect
            r =testGetRequest(testUrl+'/polls/1/',hdata,header,testCaseid,testName,testHope,response_testhope)
            # print(r)
    except Exception as e:
        print(e)

def test_login():
    try:
        table = Testdata.sheets()[3]
        for i in range(3,7):
            username=table.cell(i,0).value
            password=table.cell(i,1).value
            status=table.cell(i,2).value
            expect=table.cell(i,3).value
            hdata={
                "username":username,
                "password":int(password)
            }
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testCaseid="3-1"
            testName="TestLogin"+testCaseid
            testHope=str(int(status))
            response_testhope=expect
            r =testPostRequest(testUrl+'/polls/login/',hdata,header,testCaseid,testName,testHope,response_testhope)
            # print(r)
    except Exception as e:
        print(e)

# post_vote()
# test_login()
# get_polls()