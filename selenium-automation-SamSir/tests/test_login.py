import pytest
from .basetest import BaseTest
from pages.loginpage import TexIncHomePage
import configparser,os
current_dir = os.getcwd()
path = os.path.split((current_dir))
config = configparser.ConfigParser()
config.read(path[0] + '/auth.ini')
EMAIL = str(config.get('env', 'email'))
PASSWORD = str(config.get('env', 'password'))

class TestCase(BaseTest):

    def test_login_to_tex(self):
        email=EMAIL
        pwd= PASSWORD
        login_page = TexIncHomePage(self.driver)
        pageObject = login_page.do_login(EMAIL,PASSWORD)
        import time;time.sleep(10)

    def test_login_again(self):
        login_page = TexIncHomePage(self.driver)
        searchpage = login_page.do_login(EMAIL,PASSWORD)
        import time;time.sleep(10)