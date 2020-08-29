
# Testing site
base_url = 'http://localhost:8000/'

# Login account
auth_data = {'Account': 'admin', 'Password': '1234'}
login_url = base_url + '/api/auth'

# Web auth使用的session
session = None

