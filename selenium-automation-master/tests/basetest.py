from selenium import webdriver
import os, time, sys

current_dir = os.getcwd()
path = os.path.split((current_dir))
import configparser


class BaseTest(object):
    driver = None
    config = configparser.ConfigParser()
    config.read(path[0] + '/auth.ini')

    #before class
    def setup_class(self):
        print("Start class")

    #before every test
    def setup_method(self):
        print("start test")
        os.chdir('..')
        path = os.getcwd() + '/driver/chromedriver'
        # current = os.getcwd()
        # path = os.path.split((current))
        # driver_path = path[0] + "/drivers/chromedriver"
        self.driver = webdriver.Chrome(executable_path=path)
        # self.driver.set_window_size(1500, 1200)

    #after every test
    def teardown_method(self):
        self.driver.close()
        self.driver.quit()
        print("End test")

    #after class
    def teardown_class(self):
        print("End class")


def timestamp():
    return int(time.time() * 1000)


