import unittest

from sample.model.MEncryptor import MEncryptor


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.encryptor = MEncryptor()

    def test_decrypt(self):
        exp = 'admin;40c67842b4cd51e3e08331ecff3749d6c051718a183573bf8d79e4ec0c7222b1'
        result = self.encryptor.decrypt('log')
        self.assertEqual(exp, result)


if __name__ == '__main__':
    unittest.main()
