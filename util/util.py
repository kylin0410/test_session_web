import re


def login_session(session, login_url, auth_data):
    resp_token = session.get(login_url, verify=False)
    token = re.search(r'(_RequestVerificationToken" type="hidden" value=")(.*?)(" />)', resp_token.text)
    auth_data['__RequestVerificationToken'] = token.group(2)
    resp_login = session.post(login_url, data=auth_data, verify=False)
    assert not re.search(r'無效的帳號', resp_login.text), '登入測試失敗'
    assert resp_login.status_code == 200, '登入測試失敗'

