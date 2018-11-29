'''
用requests库和unittest任选5个接口进行接口的自动化测试，并且使用自动化测试报告模块HTMLTestRunner生成html的报告
网址：https://blog.csdn.net/c__chao/article/details/78573737
https://www.apiopen.top/weatherApi?city=武汉
https://www.apiopen.top/novelSearchApi?name=盗墓笔记
https://www.apiopen.top/addStatistics?appKey=00d91e8e0cca2b76f515926a36db68f5&type=点击统计&typeId=1&count=2
https://www.apiopen.top/createUser?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123654
https://www.apiopen.top/meituApi?page=1
python3HTMLTestRunner下载地址：https://github.com/defnngj/HTMLTestRunner 
'''
import HTMLTestRunner
import unittest
import requests

class TestInterface_Wearther(unittest.TestCase):
    #初始化(浏览器的调用和URL访问)
    def setUp(self):
        url = "https://www.apiopen.top/weatherApi" 
        self.url=url      
    def test_ok(self): #测试正确参数
        city = {'city': '武汉'}
        r = requests.get(self.url ,params=city)
        self.assertEqual('武汉' in r.text,True,'test fail')
    def test_er(self): #测试错误参数
        city = {'city': 'wuhan'}
        r = requests.get(self.url,params=city)
        self.assertEqual('武汉' in r.text,False,'test fail')

    #清理工作(退出浏览器，测试方法以test开头)    
    def tearDown(self):
        pass

class TestInterface_novelSearchApi(unittest.TestCase):
    #初始化(浏览器的调用和URL访问)
    def setUp(self):
        url = "https://www.apiopen.top/novelSearchApi" 
        self.url=url           
    def test_ok(self):
        name = {'name': '盗墓笔记'}
        r = requests.get(self.url ,params=name)
        self.assertEqual('成功' in r.text,True,'test fail')
        name = {'name': 'daomubiji'}
        r = requests.get(self.url,params=name)
        self.assertEqual('成功' in r.text,True,'test fail')
    def test_er(self):
        name = {'name': 'daomubiji123'}
        r = requests.get(self.url,params=name)
        self.assertEqual('成功' in r.text,False,'test fail')

    #清理工作(退出浏览器，测试方法以test开头)    
    def tearDown(self):
        pass

class TestInterface_addStatistics(unittest.TestCase):
    #初始化(浏览器的调用和URL访问)
    def setUp(self):
        url = "https://www.apiopen.top/addStatistics" 
        self.url=url           
    def test_ok(self):
        data = {'appKey': '00d91e8e0cca2b76f515926a36db68f5','type':'点击统计','typeId':'1','count':'2'}
        r = requests.get(self.url ,params=data)
        self.assertEqual('统计成功' in r.text,True,'test fail')

    def test_er(self):
        data = {'type':'点击统计','typeId':'1','count':'2'}
        r = requests.get(self.url,params=data)
        self.assertEqual('参数异常' in r.text,True,'test fail')
        data = {'appKey': '00d91e8e0cca2b76f515926a36db68f5','typeId':'1','count':'2'}
        r = requests.get(self.url,params=data)
        self.assertEqual('参数异常' in r.text,True,'test fail')
        data = {'appKey': '00d91e8e0cca2b76f515926a36db68f5','type':'点击统计','count':'2'}
        r = requests.get(self.url,params=data)
        self.assertEqual('参数异常' in r.text,True,'test fail')
        data = {'appKey': '00d91e8e0cca2b76f515926a36db68f5','type':'点击统计','typeId':'1'}
        r = requests.get(self.url,params=data)
        self.assertEqual('参数异常' in r.text,True,'test fail')

    #清理工作(退出浏览器，测试方法以test开头)    
    def tearDown(self):
        pass

class TestInterface_createUser(unittest.TestCase):
    #初始化(浏览器的调用和URL访问)
    def setUp(self):
        url = "https://www.apiopen.top/createUser" 
        self.url=url           
    def test_ok(self):
        data = {'key': '00d91e8e0cca2b76f515926a36db68f5','phone':'13594347817','passwd':'123654'}
        r = requests.get(self.url ,params=data)
        self.assertEqual('用户已注册' in r.text,True,'test fail')
        data = {'key': '00d91e8e0cca2b76f515926a36db68f5','phone':'18971419563','passwd':'124654','image':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1537638443532&di=d61f520720118a7bd30337bcc726e246&imgtype=0&src=http%3A%2F%2Fdesk.fd.zol-img.com.cn%2Ft_s960x600c5%2Fg5%2FM00%2F07%2F07%2FChMkJlXw8RuIa562ACDYjgXma80AACdegNqr0wAINim957.jpg'}
        r = requests.post(self.url,params=data)
        self.assertEqual('成功' in r.text,True,'test fail')
    def test_er(self):
        data = {'phone':'13594347817','passwd':'123654'}
        r = requests.get(self.url,params=data)
        self.assertEqual('参数异常' in r.text,True,'test fail')
        data = {'key': '00d91e8e0cca2b76f515926a36db68f5','passwd':'123654'}
        r = requests.get(self.url,params=data)
        self.assertEqual('参数异常' in r.text,True,'test fail')
        data = {'key': '00d91e8e0cca2b76f515926a36db68f5','phone':'18971419563'}
        r = requests.get(self.url,params=data)
        self.assertEqual('参数异常' in r.text,True,'test fail')
    #清理工作(退出浏览器，测试方法以test开头)    
    def tearDown(self):
        pass


class TestInterface_meituApi(unittest.TestCase):
    #初始化(浏览器的调用和URL访问)
    def setUp(self):
        url = "https://www.apiopen.top/meituApi" 
        self.url=url           
    def test_ok(self):
        data = {'page':'1'}
        r = requests.get(self.url ,params=data)
        self.assertEqual('美图' in r.text,True,'test fail')
        data = {'page':'0'}
        r = requests.get(self.url ,params=data)
        self.assertEqual('美图' in r.text,True,'test fail')
        data = {'page':'10'}
        r = requests.get(self.url ,params=data)
        self.assertEqual('美图' in r.text,True,'test fail')
        data = {'page':'100'}
        r = requests.get(self.url ,params=data)
        self.assertEqual('成功' in r.text,True,'test fail')
    def test_er(self):
        pass

    #清理工作(退出浏览器，测试方法以test开头)    
    def tearDown(self):
        pass


if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(TestInterface_Wearther("test_ok"))
    suit.addTest(TestInterface_Wearther("test_er"))
    suit.addTest(TestInterface_novelSearchApi("test_ok"))
    suit.addTest(TestInterface_novelSearchApi("test_er"))
    suit.addTest(TestInterface_addStatistics("test_ok"))
    suit.addTest(TestInterface_addStatistics("test_er"))
    suit.addTest(TestInterface_createUser("test_ok"))
    suit.addTest(TestInterface_createUser("test_er"))
    suit.addTest(TestInterface_meituApi("test_ok"))
    suit.addTest(TestInterface_meituApi("test_er"))
    fp = open('./InterfaceResult.html', 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,
                                          title='<5 interface>test report',
                                          description='describe: ... ')
    
    runner.run(suit)
    fp.close()