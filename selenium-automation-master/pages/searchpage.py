from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .basepage import BasePage

class TexIncSearchPeople(BasePage):
    click_search_icon='StyledIconBase-ea9ulj-0 duvCfz bk33ssm'
    search_placeholder='ant-select ant-select-lg sl1rq62 ant-select-multiple ant-select-allow-clear ant-select-show-search'

    def __init__(self,driver):
        self.driver = driver

