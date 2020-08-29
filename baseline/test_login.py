import requests
import unittest
import re

import config


class Login(unittest.TestCase):
    # Basic variable.
    session = None
    
    # Test data.
    login_data = {'Account': 'admin', 'Password': 'password'}
    wrong_login_data = {'Account': 'admin', 'Password': 'konichiwa'}

    def setUp(self):
        self.session = requests.Session()


    def tearDown(self):
        if self.session:
            self.session.close()


    def test_login(self):
        resp_token = self.session.get(config.base_url + '/api/auth', verify=False)
        token = re.search(r'(_RequestVerificationToken" type="hidden" value=")(.*?)(" />)', resp_token.text)
        self.login_data['__RequestVerificationToken'] = token.group(2)
        resp_login = self.session.post(config.base_url + '/api/auth', data=self.login_data, verify=False)
        assert not re.search(r'無效的帳號', resp_login.text), '登入測試失敗'


    def test_login_fail(self):
        resp_token = self.session.get(config.base_url + '/api/auth', verify=False)
        token = re.search(r'(_RequestVerificationToken" type="hidden" value=")(.*?)(" />)', resp_token.text)
        self.wrong_login_data['__RequestVerificationToken'] = token.group(2)
        resp_login = self.session.post(config.base_url + '/api/auth', data=self.wrong_login_data, verify=False)
        assert re.search(r'無效的帳號', resp_login.text), '登入失敗測試失敗'
    
    
if __name__ == '__main__':
    unittest.main()
