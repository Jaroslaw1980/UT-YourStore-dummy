import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=3)

suite = loader.discover('C:/Python/Selenium/UTYourStore/Tests/test_register')

result = runner.run(suite)

if __name__ == '__main__':
    unittest.main()


