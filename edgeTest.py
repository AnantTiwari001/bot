from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


edgeOption= webdriver.EdgeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
edgeOption.add_experimental_option('prefs', prefs)

driver= webdriver.Edge('D:\\python\\automation\\selenium\\msedgedriver.exe',options=edgeOption)
driver.get('https://facebook.com/anant.tiwari')

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Like"]')))

time.sleep(100)
driver.quit()