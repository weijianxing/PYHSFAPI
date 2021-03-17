__author__ = 'jianxing.wei@wuage.com '
from hsf_telnet_client.telnetUtil import HSFTelnet
import unittest as punit
import json

class hsfTest(punit.TestCase):
    tn=HSFTelnet()
    def setUp(self):
        self.tn.connection()
    def tearDown(self):
        self.tn.close()
    def test_sellerInvoke(self):
        respone=self.tn.invoke(method="searchSeller" ,singleParm="友发").decode("utf-8")
        print("resonse => {0}".format(respone))
        sellers=[]
        sellers=json.loads(respone)
        print("找到商家数量：{0} ".format(len(sellers)))
        self.assertEqual(5, len(sellers) , "返回商家数量应该为5")
        find=0
        for item in sellers:
            if item=="4lv8ll4g":
                find=1
                break
        self.assertEqual(find, 1 , "没有找到 4lv8ll4g 商铺")




if __name__ == '__main__':
     punit.main()