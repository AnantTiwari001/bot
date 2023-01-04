from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

loginStatus= True

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome("C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\seleniumbase\\drivers\\chromedriver.exe",chrome_options=chrome_options)
driver.get("https://www.like4like.org/")
driver.maximize_window()

def login():
    loginLink= driver.find_element(By.LINK_TEXT, 'Login')
    loginLink.click()

    emailInput= driver.find_element(By.NAME, 'username')
    emailInput.send_keys('Anant124')
    passwordInput= driver.find_element(By.NAME, 'password')
    passwordInput.send_keys('+p*%!VU.g7jyMYQ')
    submit = driver.find_element(By.CSS_SELECTOR, 'span.button.medium.orange.cursor')
    submit.click()

def fblogin():
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        print('found the email!')
        email= driver.find_element(By.NAME, 'email')
        password= driver.find_element(By.NAME, 'pass')
        email.send_keys('+9779814253523')
        password.send_keys('Anant@123')
        password.send_keys(Keys.RETURN)
        loginStatus=False

def follow():
    like=driver.find_element(By.CSS_SELECTOR,'div[aria-label="Like"]')
    like.click()

def earn():
    print('oh start boy')
    driver.implicitly_wait(2)
    print(driver.window_handles)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.earn_pages_button')))
    btn= driver.find_element(By.CSS_SELECTOR, 'a.earn_pages_button')#earn btn
    try:
        btn.click()
    except:
        earn()
    else:
        # new window opens
        print('clicked the button!')
        print(driver.window_handles)
        parentWindow= driver.current_window_handle
        # driver.switch_to.new_window('window')
        # switched to the opened window
        driver.switch_to.window(driver.window_handles[1])
        driver.maximize_window()
        print('fblogin')
        try:
            fblogin()
        except:
            print('already login')
        else:
            print('login sucessful!')
        print('follow next!')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Like"]')))
        driver.implicitly_wait(10)
        follow()
        driver.implicitly_wait(20)
        print('close after wait!')
        driver.close()
        print('switching window!')
        driver.switch_to.window(driver.window_handles[0])
        print('explicit wait!')
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'img[title="Click On The Button To Confirm Interaction!"]')))
        driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]').click()
        print('done the conform click!')
        driver.implicitly_wait(20)
        # time.sleep(10)
        driver.switch_to.window(parentWindow)
        # follow.click()


login()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Free Credits')))
driver.get('https://www.like4like.org/user/earn-facebook.php')
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'task0')))


print('should be after the wait!')
earn()
for i in range(20):
    earn()
    # try:
    #     earn()
    #     print('this earn function runs')
    # except:
    #     print('something went wrong!')

time.sleep(10)


driver.quit()