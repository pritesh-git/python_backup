from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .basepage import BasePage
from .searchpage import  TexIncSearchPeople


class TexIncHomePage(BasePage):
    click_register_button='/html/body/div[1]/div/div[1]/header/div/ul/li[2]/button'
    click_sign_in_button='//header/div[1]/ul[1]/li[1]/button[1]'
    enter_email_id="//input[@id='1-email']"
    enter_password='/html/body/div/div/div[2]/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div/input'
    click_on_login_button="//button[@class='auth0-lock-submit']"

    def __init__(self,driver):
        self.driver = driver

    def load(self):
        url = self.base_url()
        self.driver.get(url)

    def open_login_page(self):
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, self.click_register_button)))
        # return self.browser.find_elements_by_xpath(self.click_register_button)[0]
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.click_sign_in_button)))
        return self.driver.find_elements_by_xpath(self.click_sign_in_button)[0]

    def enter_email_id_in_login_page(self,email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.enter_email_id)))
        import time;time.sleep(5)
        return self.driver.find_elements_by_xpath(self.enter_email_id)[0].send_keys(email)

    def enter_password_in_login_page(self,pwd):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.enter_password)))
        import time;time.sleep(5)
        return self.driver.find_elements_by_xpath(self.enter_password)[0].send_keys(pwd)

    def click_on_login_button_in_login_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.click_on_login_button)))
        return self.driver.find_elements_by_xpath(self.click_on_login_button)[0]

    def do_login(self,email,pwd):
        self.load()
        self.open_login_page().click()
        self.enter_email_id_in_login_page(email)
        self.enter_password_in_login_page(pwd)
        self.click_on_login_button_in_login_page().click()
        return TexIncSearchPeople(self.driver)




