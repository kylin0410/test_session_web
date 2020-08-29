import copy
import json
import random
import re
import requests
import unittest

import config
from util import util


class SourceTrace(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        config.session = requests.Session()
        util.login_session(config.session, config.login_url, config.auth_data)


    @classmethod
    def tearDownClass(cls):
        if config.session:
            config.session.close()


    def test_source_trace(self):
        input = {'DocumentCode': 'SHD20190523001'}
        resp_trace = config.session.post(config.base_url + '/api/source_trace', data=input, verify=False)
        print(resp_trace.text)
        print(resp_trace.status_code)


if __name__ == '__main__':
    unittest.main()
