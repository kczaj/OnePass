import unittest

from sample.model.MProfile import MProfile


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.profile = MProfile('kuba', 'c', 'dwqd@wfaf.pl', 'test', 'Testtttt21')

    def test_update_all_good(self):
        name = 'pwoq'
        surname = 'jdiwoq'
        email = 'iuhwqd@qwjfqf.pl'
        data = (name, surname, email)
        exp = 1;
        result = self.profile.update(data)
        self.assertEqual(exp, result)

    def test_update_wrong_name(self):
        name = 'pwoq123'
        surname = 'jdiwoq'
        email = 'iuhwqd@qwjfqf.pl'
        data = (name, surname, email)
        exp = -1001;
        result = self.profile.update(data)
        self.assertEqual(exp, result)

    def test_update_wrong_surname(self):
        name = 'pwoq'
        surname = 'jdiwoq2141421'
        email = 'iuhwqd@qwjfqf.pl'
        data = (name, surname, email)
        exp = -1002;
        result = self.profile.update(data)
        self.assertEqual(exp, result)

    def test_update_wrong_email(self):
        name = 'pwoq'
        surname = 'jdiwoq'
        email = 'iuhwqdqwjfqf.pl'
        data = (name, surname, email)
        exp = -1003;
        result = self.profile.update(data)
        self.assertEqual(exp, result)

    def test_update__wrong_password(self):
        password = 'drt1'
        exp = False
        result = self.profile.update_password(password)
        self.assertEqual(exp, result)

    def test_update__good_password(self):
        password = 'Lowskwqi76'
        exp = True
        result = self.profile.update_password(password)
        self.assertEqual(exp, result)


if __name__ == '__main__':
    unittest.main()
