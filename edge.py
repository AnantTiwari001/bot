from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


driver= webdriver.Edge('D:\\python\\automation\\selenium\\msedgedriver.exe')
driver.get('https://www.google.com/')

time.sleep(10)
driver.quit()