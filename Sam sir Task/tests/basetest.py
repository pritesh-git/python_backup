import time
from selenium import webdriver
import os


class BaseTest(object):
    driver = None

    # before class
    @staticmethod
    def setup_class():
        print("Start class")

    # before every test
    def setup_method(self):
        print("start test")
        path = os.getcwd() + '/driver/chromedriver'
        self.driver = webdriver.Chrome(executable_path=path)

    # after every test
    def teardown_method(self):
        self.driver.close()
        self.driver.quit()
        print("End test")

    # after class
    @staticmethod
    def teardown_class():
        print("End class")


def timestamp():
    return int(time.time() * 1000)
