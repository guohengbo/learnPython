import unittest
import requests
import json

class testpolls(unittest.TestCase):
    def setUp(self):
        self.url="http://127.0.0.1:8000"
    
    def tearDown(self):
        pass
    def test_get_question(self):
        result=requests.get(self.url+'/polls')
        code=result.status_code
        text=result.text
        dicts=json.loads(text)#转换成字典
        self.assertEqual(code,200)
        self.assertEqual(dicts['msg'],'success')
        self.assertEqual(dicts['data']['1'],'选择你最喜欢的游戏？')
    
    def test_get_choice(self):
        result=requests.get(self.url+'/polls/1')
        code=result.status_code
        text=result.text
        dicts=json.loads(text)#转换成字典
        self.assertEqual(code,200)
        self.assertEqual(dicts['msg'],'success')
        self.assertEqual(dicts['data']['2'],'找茬')
    
    def test_get_votes(self):
        result=requests.get(self.url+'/polls/1/vote')
        code=result.status_code
        text=result.text
        dicts=json.loads(text)#转换成字典
        self.assertEqual(code,200)
        self.assertEqual(dicts['msg'],'success')
        self.assertEqual(dicts['data']['连连看'],1)

    
if __name__ == '__main__':
    unittest.main()