from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("http://uitestingplayground.com/textinput")
driver.find_element(By.ID, "newButtonName").send_keys('My_Button')
driver.find_element(By.ID, "updatingButton").click()
time.sleep(5)

button_change_check = WebDriverWait(driver, 20).until_not(
    EC.element_to_be_clickable((By.LINK_TEXT, "Button That Should Change it's Name Based on Input Value")))
print('Test Passed')
driver.quit()

# второй вариант ожидания:
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.LINK_TEXT,"Button That Should Change it's Name Based on Input Value")
#     )
# except:
#     print('Test Passed')

