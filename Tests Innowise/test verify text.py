from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("http://uitestingplayground.com/verifytext")
time.sleep(2)
button_change_check = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")))
print('Test Passed')
driver.quit()






