import unittest
class Math:
    #初始化 self是类实例对象本身
    def __init__(self, a, b):
        self.a = a
        self.b = b
    #四则运算
    def add(self):
        return self.a + self.b
    def miuns(self):
        return self.a - self.b
    def multi(self):
        return self.a * self.b
    def divide(self):
        if self.a !=0:
            return self.a / self.b
        else:
            raise Exception("除数为0，无意义！")
ca = Math(5,6)
class TestMath(unittest.TestCase):
    #初始化(浏览器的调用和URL访问)
    def setUp(self):
        pass       
    def test_add(self):
        self.assertEqual(ca.add(),11,"加法error")
    def test_minus(self):
        self.assertEqual(ca.miuns(),-1,"减法error")
    def test_multi(self):
        self.assertEqual(ca.multi(),30,"乘法error")
    def test_divide(self):
        self.assertEqual(ca.divide(),0.8333333333333334,"除法error")
    #清理工作(退出浏览器，测试方法以test开头)    
    def tearDown(self):
        pass

# def suite():
#     suite=unittest.TestSuite()
#     suite.addTest(TestMath("test_add"))
#     suite.addTest(TestMath("test_minus"))
#     return suite          
if __name__ == '__main__':
    unittest.main() 