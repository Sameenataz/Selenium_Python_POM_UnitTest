import os
import unittest

# get all tests from SearchText and HomePageTest class
from HtmlTestRunner import HTMLTestRunner

# get the directory path to output report file
from Test_Cases.test_LoginPage import Github_Login_Functionality_validation


dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
gitHub_Test = unittest.TestLoader().loadTestsFromTestCase(Github_Login_Functionality_validation)


# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([gitHub_Test])


# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(output='example_suite1')
# runner = unittest.TextTestRunner()
# run the suite using HTMLTestRunner
runner.run(test_suite)

