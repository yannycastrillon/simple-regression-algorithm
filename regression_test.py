# Testing library
import unittest
import regression

class RegressionTest(unittest.TestCase):

    def test_get_mean(self):
        test_arr = [1,2,3,4]
        # regression = Regression
        result = regression.Regression().get_mean(self,test_arr)
        expect = 2.5

        self.assertEqual(expect, result)

# Run test

if __name__ == '__main__':
    unittest.main()
