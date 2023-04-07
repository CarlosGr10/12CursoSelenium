import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class HelloWorld(unittest.TestCase):

    def setUp(self):
        service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)