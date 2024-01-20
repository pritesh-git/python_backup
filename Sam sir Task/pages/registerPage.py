import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from .basepage import BasePage


class RegistrationPage(BasePage):
    firstName = "//input[@placeholder='First Name']"
    lastName = "//input[@placeholder='Last Name']"
    address = "textarea"
    email = "//input[@type='email']"
    firstPassword = "firstpassword"
    secondPassword = "secondpassword"
    mobileNo = "//input[@type='tel']"
    genderMale = "//input[@value='Male']"
    genderFemale = "//input[@value='Female']"
    checkbox_id = "checkbox2"
    uploadFile = "imagesrc"
    skills = "Skills"
    countries = "countries"
    yearBox = "yearbox"
    monthBox = "//select[@placeholder='Month']"
    dayBox = "daybox"
    submitButton = "Button1"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        url = self.base_url() + 'Register.html'
        self.driver.get(url)
        time.sleep(3)

    def fill_registration_fields(self):
        WebDriverWait(self.driver, 1).until(ec.presence_of_element_located((By.XPATH, self.firstName)))
        self.driver.find_element_by_xpath(self.firstName).send_keys("Raj")
        self.driver.find_element_by_xpath(self.lastName).send_keys("Jain")
        self.driver.find_element_by_tag_name(self.address).send_keys("12-D,Streets View,Docker Lane")
        self.driver.find_element_by_xpath(self.email).send_keys("raj@gmail.com")
        self.driver.find_element_by_xpath(self.mobileNo).send_keys("9658741256")
        self.driver.find_element_by_xpath(self.genderMale).click()
        self.driver.find_element_by_id(self.checkbox_id).click()
        # self.driver.find_element_by_id(self.uploadFile).send_keys(os.getcwd() + "/__init__.py")
        self.driver.find_element_by_id(self.skills).send_keys("Python")
        self.driver.find_element_by_id(self.countries).send_keys("Egypt")
        yearbox = Select(self.driver.find_element_by_id(self.yearBox))
        yearbox.select_by_value("1996")
        monthbox = Select(self.driver.find_element_by_xpath(self.monthBox))
        monthbox.select_by_value("June")
        daybox = Select(self.driver.find_element_by_id(self.dayBox))
        daybox.select_by_value("16")
        self.driver.find_element_by_id(self.firstPassword).send_keys("123456")
        self.driver.find_element_by_id(self.secondPassword).send_keys("123456")

    def scroll_registration_fields(self):
        for i in range(1, int(self.driver.execute_script("return document.body.scrollHeight")), 2):
            self.driver.execute_script("window.scrollTo(0, {});".format(i))

    def click_on_submit(self):
        self.driver.find_element_by_id(self.submitButton).click()
        self.driver.execute_script("window.scrollTo(0,0)")

    def do_registration(self):
        self.load()
        self.fill_registration_fields()
        self.scroll_registration_fields()
        self.click_on_submit()
        return True
