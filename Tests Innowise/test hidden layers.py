from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("http://uitestingplayground.com/hiddenlayers")
time.sleep(2)
driver.find_element(By.ID, "greenButton").click()
try:
    grn_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(By.ID, "greenButton")
    )
except:
    print('Test Passed')
