import unittest,requests
from db import *

class MyTestCase(unittest.TestCase):
    url = "http://192.168.55.42:8080/p2p_management/addProduct"
    header = {
        "Content-Type: application/x-www-form-urlencoded"
    }
    def test_xz_ok(self):
        if check_product("110"):
            del_product("110")
        data = {"proNum":"110","proName":"菊花","proLimit":"54","annualized":"70"}
        r = requests.post(url=self.url,json=data)
        self.assertNotIn("失败", r)
    def test_xz_err(self):
        if not check_product("110"):
            add_product("110","菊花","54","70")
        data={"proNum":"110","proName":"菊花","proLimit":"54","annualized":"70%"}
        r = requests.post(url=self.url,json=data)
        self.assertIn('400',r.text)



if __name__ == '__main__':
    unittest.main()
