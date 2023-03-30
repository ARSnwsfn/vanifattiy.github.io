from selenium import Webdriver
from UI_Playground.Pages.DynamicHome import DynamicHome

def test_dynamic_id():
    driver = Webdriver.Chrome()
    driver.get('http://uitestingplayground.com/dynamicid')



    assert id(dynamic_btn) != "87fe9407-10c1-c0bb-ff42-73b2a0bec7db"
