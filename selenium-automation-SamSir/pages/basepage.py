import os
current_dir = os.getcwd()
path = os.path.split((current_dir))
import configparser


class BasePage(object):
    config = configparser.ConfigParser()
    config.read(path[0] + '/auth.ini')
    URL = str(config.get('env', 'url'))
    url = URL
    wait_extra_small = 30
    wait_small = 60
    wait_medium = 90
    wait_large = 150
    wait_extra_large = 300

    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def base_url(self):
        return self.url
