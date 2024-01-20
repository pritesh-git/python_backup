from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .basepage import BasePage
from .registerPage import RegistrationPage
import time


class HomePage(BasePage):
    enter_email = 'email'
    login_button = 'span'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        url = self.base_url()
        self.driver.get(url)
        time.sleep(2)

    def enter_email_id_in_login_page(self, email):
        WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.enter_email)))
        return self.driver.find_element_by_id(self.enter_email).send_keys(email)

    def click_on_login_button_in_login_page(self):
        WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.TAG_NAME, self.login_button)))
        return self.driver.find_element_by_tag_name(self.login_button)

    def do_login(self, email):
        self.load()
        self.enter_email_id_in_login_page(email)
        self.click_on_login_button_in_login_page().click()
        return RegistrationPage(self.driver)
