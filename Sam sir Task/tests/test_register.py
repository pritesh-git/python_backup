import time

from .basetest import BaseTest
from pages.registerPage import RegistrationPage


class TestCase(BaseTest):
    def test_register_to_site(self):
        register_page = RegistrationPage(self.driver)
        register_page.do_registration()
        time.sleep(5)
