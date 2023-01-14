from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome("C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\seleniumbase\\drivers\\chromedriver.exe",chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
driver.maximize_window()
# fnumber= input('Enter facebook number or email!')
# fpassword= input('Enter facebook password!')
fnumber= '9814253523'
fpassword= 'Anant@123'

def Login():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    print('found the email!')
    email= driver.find_element(By.NAME, 'email')
    password= driver.find_element(By.NAME, 'pass')
    email.send_keys(fnumber)
    password.send_keys(fpassword)
    password.send_keys(Keys.RETURN)


def main():
    Login()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Like"]')))
    for i in range(20):
        actions = ActionChains(driver)
        likeButtons= driver.find_elements(By.CSS_SELECTOR,'div[aria-label="Like"]')
        num= random.randint(1,100)
        actions.scroll_to_element(likeButtons[i])
        if (num<40):
            likeButtons[i].click()


main()