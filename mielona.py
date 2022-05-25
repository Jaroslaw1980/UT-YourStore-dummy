import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random

s = Service('C:/Selenium - dev/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service = s)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://tutorialsninja.com/demo/index.php?route=account/register')


firstname = driver.find_element(By.ID, "input-firstname").click()

# driver.find_element(By.XPATH, "//input[@type='submit']").click()
# driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
# warnning = driver.find_element(By.TAG_NAME('div')).below(firstname)
# warnning.text
# print(warnning)

time.sleep(3)
driver.close()
driver.quit()


