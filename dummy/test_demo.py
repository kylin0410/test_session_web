import unittest


class Demo(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('\nIn setUpClass()')


    @classmethod
    def tearDownClass(cls):
        print('In tearDownClass()')


    def setUp(self):
        print('In setUp()')


    def tearDown(self):
        print('In tearDown()')


    def test_func1(self):
        print('In test_func1()')


    def test_func2(self):
        print('In test_func2()')
    
    
    def test_funcfail(self):
        print('In test_funcfail()')
        result = 0
        assert result == 0, "測試炸了"
    
    
if __name__ == '__main__':
    unittest.main()
