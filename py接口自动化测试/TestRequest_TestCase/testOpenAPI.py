import xlrd
from TestRequest import testGetRequest
from testdata.getpath import GetTestDataPath

Testdata = xlrd.open_workbook(GetTestDataPath())

testUrl="http://api.apiopen.top"

def get_recommendPoetry():
    try:
        table = Testdata.sheets()[4]
        for i in range(3,4):
            status=table.cell(i,0).value
            expect=table.cell(i,1).value
            hdata={}
            header = {
                'content-type': "application/json;charset=UTF-8"
            }
            testCaseid="1-1"
            testName="TestrecommendPoetry"+testCaseid
            testHope=str(int(status))
            response_testhope=expect
            r =testGetRequest(testUrl+'/recommendPoetry',hdata,header,testCaseid,testName,testHope,response_testhope)
            print(r)
    except Exception as e:
        print(e)

def get_searchAuthors():
    try:
        table = Testdata.sheets()[4]
        for i in range(13,15):
            name=table.cell(i,0).value
            status=table.cell(i,1).value
            expect=table.cell(i,2).value
            hdata=""
            header = {
                'content-type': "application/json;charset=UTF-8"
            }
            testCaseid="2-1"
            testName="TestsearchAuthors"+testCaseid
            testHope=str(int(status))
            response_testhope=expect
            r =testGetRequest(testUrl+'/searchAuthors?name='+name,hdata,header,testCaseid,testName,testHope,response_testhope)
            print(r)
    except Exception as e:
        print(e)


def get_searchMusic():
    try:
        table = Testdata.sheets()[4]
        for i in range(21,22):
            status=table.cell(i,0).value
            expect=table.cell(i,1).value
            hdata=""
            header = {
                'content-type': "application/json;charset=UTF-8"
            }
            testCaseid="3-1"
            testName="TestsearchMusic"+testCaseid
            testHope=str(int(status))
            response_testhope=expect
            r =testGetRequest(testUrl+'/searchMusic',hdata,header,testCaseid,testName,testHope,response_testhope)
            print(r)
    except Exception as e:
        print(e)

get_recommendPoetry()
get_searchAuthors()
get_searchMusic()