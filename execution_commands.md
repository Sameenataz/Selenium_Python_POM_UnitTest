1) to run all the testfile.py in a directory
cd <path where all the testfile.py> available then type in terminal
eg:
    cd /Users/rakjha/PyProjects/Automation/PyFrameworks/PyTest
    'pytest' #it will run all the testfile
2)  to run an individual test file
eg:
cd /Users/rakjha/PyProjects/Automation/PyFrameworks/PyTest
'pytest -v -s test_file.py'

3) to run an individual test case
eg:
cd /Users/rakjha/PyProjects/Automation/PyFrameworks/PyTest
'pytest -v -s test_file.py::test_case_name'

4) to run and get htm report
pip install pytest-html
eg:
cd /Users/rakjha/PyProjects/Automation/PyFrameworks/PyTest
'pytest -v -s test_google_search.py --html=report.html'


5) to get allure report
$ pip install allure-pytest
$ cd /Users/rakjha/PyProjects/POM_UnitTest_Project/Test_Cases
$ pytest --alluredir=/Users/rakjha/PyProjects/POM_UnitTest_Project/Allure_Demo
$ cd /Users/rakjha/PyProjects/POM_UnitTest_Project/Allure_Demo
$ allure generate /Users/rakjha/PyProjects/POM_UnitTest_Project/Allure_Demo
