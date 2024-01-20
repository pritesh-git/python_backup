from pages.loginpage import HomePage
from .basetest import BaseTest
import time

EMAIL = 'automation@yopmail.com'


class TestCase(BaseTest):
    def test_login(self):
        login_page = HomePage(self.driver)
        pageObject = login_page.do_login(EMAIL)
        print(pageObject)
        time.sleep(2)

    def test_login_again(self):
        login_page = HomePage(self.driver)
        searchpage = login_page.do_login(EMAIL)
        print(searchpage)
        time.sleep(2)
