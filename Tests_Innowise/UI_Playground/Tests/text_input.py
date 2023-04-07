from selenium import webdriver
driver = webdriver.Chrome()

from vanifattiy_.Tests_Innowise.UI_Playground.Pages.TextInputHome import TextInputHome

def test_text_input():
    driver = webdriver.Chrome()
    driver.get('http://uitestingplayground.com/textinput')

    do_send_keys(locators.input_field,'My_Button')
    do_click(locators.changeable_btn)
    assert locators.check_if_visible(locators.check_changeable_btn)

