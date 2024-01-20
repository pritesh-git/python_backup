class BasePage(object):
    url = 'http://demo.automationtesting.in/'
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
