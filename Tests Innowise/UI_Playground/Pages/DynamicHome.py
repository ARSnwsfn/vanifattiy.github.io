from UI_Playground.Pages.BasePage import BasePage
from selenium import Webdriver


class DynamicHome(BasePage):
    def __init__(self, driver):
        self.driver = driver


locators = {
    'dynamic_btn': ('XPATH', '//button["Button with Dynamic ID"]')
}


# def open_site(self):
#     driver = Webdriver.Chrome()
#     return driver.get('http://uitestingplayground.com/dynamicid')
