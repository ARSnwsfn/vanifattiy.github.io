from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element(By.LINK_TEXT,"My Account").click()
driver.find_element(By.ID,"username").send_keys("svyatoslav@mail.ru")
driver.find_element(By.ID,"password").send_keys("svyatoslavM73")
driver.find_element(By.CSS_SELECTOR,".form-row>input:nth-child(3)").click()
logout_check = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
driver.quit()
