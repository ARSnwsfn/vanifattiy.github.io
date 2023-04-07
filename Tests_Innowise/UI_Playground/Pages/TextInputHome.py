from vanifattiy_.Tests_Innowise.UI_Playground.Pages.BasePage import BasePage
from selenium import webdriver


class TextInputHome(BasePage):
    def __init__(self, driver):
        self.driver = driver


locators = {
    "input_field": ("By.ID", "newButtonName"),
    "changeable_btn": ("By.ID", "updatingButton"),
    "check_changeable_btn": ("LINK_TEXT", "Button That Should Change it's Name Based on Input Value")
}


# def open_site(self):
#     driver = Webdriver.Chrome()
#     return driver.get('http://uitestingplayground.com/dynamicid')
