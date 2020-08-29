import copy
import json
import random
import requests
import unittest

import config
from util import util


class Person(unittest.TestCase):
    # Test data.
    personal_data = \
        {'ID': 0, 'Password': 'password', 'PasswordDigits': 'abcd1234'}

    @classmethod
    def setUpClass(cls):
        config.session = requests.Session()
        util.login_session(config.session, config.login_url, config.auth_data)


    @classmethod
    def tearDownClass(cls):
        if config.session:
            config.session.close()


    def test_personal_add(self):
        # 準備新增使用者必填資料
        code = 'TestCode' + str(random.randint(0, 999))
        input = copy.deepcopy(self.personal_data)
        input['Code'] = code
        input['Name'] = 'TestName' + str(random.randint(0, 999))
        input['Account'] = 'TestAccount' + str(random.randint(0, 999))

        # 新增使用者
        resp_org = config.session.post(config.base_url + '/api/user', json=input, verify=False)
        res_person = json.loads(resp_org.text)
        assert res_person['status'] == 1, '新增人員帳號失敗'

        # 新增使用者未回傳ID，故以列表方式檢查
        input = {'keyword': 'TestCode', 'page': 1, 'pageSize': 50}
        resp_list = config.session.post(config.base_url + '/api/user/list', data=input, verify=False)
        res_person = json.loads(resp_list.text)
        assert len(res_person) > 0, '新增人員帳號列表失敗'
        
        #print(res_person)
        flag = False
        person_id = 0
        for person in res_person['rows']:
            #print(person)
            if person['Code'] == code:
                flag = True
                person_id = person['ID']
                #print('新增人員帳號ID: {}'.format(person_id))
        assert flag is True, '查無新增人員帳號{}'.format(code)

        # 刪除該帳號
        assert person_id != 0, '人員帳號ID為0'
        input = {'ids': [person_id]}
        response = config.session.post(config.base_url + '/api/user/delete', data=input, verify=False)
        #print(response.text)
        #print(response.status_code)
        result = json.loads(response.text)
        assert result['Status'] == 1, '刪除人員帳號失敗'


    def test_personal_list(self):
        # 人員帳號列表
        input = {'keyword': '', 'page': 1, 'pageSize': 50}
        resp_list = config.session.post(config.base_url + '/api/user/list', data=input, verify=False)
        res_person = json.loads(resp_list.text)
        #print(resp_list.text)
        assert len(res_person) > 0, '人員帳號列表失敗'


if __name__ == '__main__':
    unittest.main()
