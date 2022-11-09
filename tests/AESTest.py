import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "src"))

from mitWppSdk.util import AesHelper, isBase64
import unittest

class TestCipherFunctions(unittest.TestCase):

    def test_encrypt(self):
        helper = AesHelper( bytes.fromhex("5DCC67393750523CD165F17E1EFADD21"))
        s = helper.encrypt("hola mundo")
        self.assertTrue(isBase64(s))

    def test_decrypt(self):
        s = "IWbkgFfqf/NYJ/fC2WZhp2OK1pFMc9wjTry1CmludiY="
        helper = AesHelper( bytes.fromhex("5DCC67393750523CD165F17E1EFADD21"))
        s = helper.decrypt(s)
        self.assertEqual(s, "hola mundo")

if __name__ == '__main__':
    unittest.main()