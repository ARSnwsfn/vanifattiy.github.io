from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory

class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def check_if_visible(self, by_locator):
        button_check = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(button_check)
