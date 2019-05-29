import unittest
from po.Myp2p.PrepayCash import PrepayClass
from libs.Tools import VerifyClass

class TestPrepayApi(VerifyClass):

    def setUp(self):
        self.p = PrepayClass()

    def test_prepay_success_001(self):
        result = self.p.prepayApi()
        self.verifyCode(result,200)

if __name__ == '__main__':
    unittest.main()