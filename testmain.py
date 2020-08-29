import sys
import unittest


# 測試啟動點
if __name__ == '__main__':

	# 用discover尋找指定目錄下的測試項目
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().discover('./baseline', pattern='test_*.py'))
    
    runner = unittest.TextTestRunner(verbosity=2, warnings="ignore")
    result = runner.run(suite)
    #print("---- START OF TEST RESULTS")
    #print(result)
    #
    #print("result::errors")
    #print(result.errors)
    #
    #print("result::failures")
    #print(result.failures)
    #
    #print("result::skipped")
    #print(result.skipped)
    #
    #print("result::successful")
    #print(result.wasSuccessful())
    #
    #print("result::test-run")
    #print(result.testsRun)
    #print("---- END OF TEST RESULTS")





