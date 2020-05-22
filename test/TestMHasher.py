import unittest

from sample.model.MHasher import MHasher


class MyTestCase(unittest.TestCase):

    def test_hash(self):
        hasher = MHasher()
        exp = '40c67842b4cd51e3e08331ecff3749d6c051718a183573bf8d79e4ec0c7222b1'
        result = hasher.hash('passwrd1')
        self.assertEqual(exp,result)


if __name__ == '__main__':
    unittest.main()
