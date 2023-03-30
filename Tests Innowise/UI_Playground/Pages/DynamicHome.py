from seleniumpagefactory.Pagefactory import PageFactory


class DynamicHome(PageFactory):
    def __init__(self, driver):
        self.driver = driver


locators = {
    'dynamic_btn': ('XPATH', '//button["Button with Dynamic ID"]')
}


def click_btn(self):
    self.dynamic_btn.click()
