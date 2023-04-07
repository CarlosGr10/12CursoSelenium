import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HeloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(10)

    def test_hello(self):
        driver = self.driver
        driver.get('https://www.google.com/?hl=es')
        

    def testDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report'))