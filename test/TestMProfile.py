import unittest


class MyTestCase(unittest.TestCase):

    def test_update_all_good(self):
        self.assertEqual(True, False)

    def test_update_wrong_name(self):
        self.assertEqual(True, False)

    def test_update_wrong_surname(self):
        self.assertEqual(True, False)

    def test_update_wrong_email(self):
        self.assertEqual(True, False)

    def test_update_password(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
