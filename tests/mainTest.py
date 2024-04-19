import test_AgeStats
import test_LinkGetter
import test_Load
import test_Cleaner
import test_HeightStats
import unittest

def main(): 
    # define the test suite
    suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(test_AgeStats.TestAgeStatistics),
                                unittest.TestLoader().loadTestsFromTestCase(test_LinkGetter.TestGetNBATeams),
                                unittest.TestLoader().loadTestsFromTestCase(test_Load.TestConnectToDb),
                                unittest.TestLoader().loadTestsFromTestCase(test_Cleaner.TestCleaner),
                                unittest.TestLoader().loadTestsFromTestCase(test_HeightStats.TestHeightStatistics),
                                ])
    # run the test suite
    unittest.TextTestRunner(verbosity=2).run(suite)
    
if __name__ == '__main__':
    main()