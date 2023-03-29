from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("http://uitestingplayground.com/dynamicid")
time.sleep(2)
dynamic_button = driver.find_element(By.XPATH, "//button['Button with Dynamic ID']")

if id(dynamic_button) != "87fe9407-10c1-c0bb-ff42-73b2a0bec7db":
    print('Test Passed')
driver.quit()





