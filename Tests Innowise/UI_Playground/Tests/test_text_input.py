from selenium import webdriver

from UI_Playground.Pages.TextInputHome import TextInputHome

def test_text_input():
    driver = Webdriver.Chrome()
    driver.get('http://uitestingplayground.com/textinput')

    do_send_keys(locators.input_field,'My_Button')
    do_click(locators.changeable_btn)
    assert locators.check_if_visible(locators.check_changeable_btn)

