import unittest
from lib import xzs_login


class MyTestCase(unittest.TestCase):
    x=xzs_login.xzs_login()
    def test_login_ok(self):
        t = self.x.login("student26","123456")
        self.assertIn("成功", t)
    def test_login_err01(self):
        t = self.x.login("","123456")
        self.assertIn("用户名或密码错误",t)
    def test_login_err02(self):
        t = self.x.login("student26","")
        self.assertIn("用户名或密码错误",t)
if __name__ == '__main__':
    unittest.main()
