from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

# loginStatus= True
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)

# driver = webdriver.Chrome("C:\\Users\\chromedriver.exe",chrome_options=chrome_options)


options = Options()
options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\')
options.add_argument('--disable-service-workers')
options.add_argument("--disable-features=Permissions-Policy")

driver = uc.Chrome( executable_path='C:\\Users\\chromedriver.exe',options=options)


driver.get("https://www.like4like.org/")
# fnumber= input('Enter the facebook number!')
# fpassword= input('Enter the facebook password!')
NotfbLogged= False
fnumber='9814253523'
fpassword='Anant@123'
driver.maximize_window()

def page_loaded(driver):
    return driver.execute_script('return document.readyState') == 'complete'

def login():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
        loginLink= driver.find_element(By.LINK_TEXT, 'Login')
        loginLink.click()

        emailInput= driver.find_element(By.NAME, 'username')
        emailInput.send_keys('Anant124')
        passwordInput= driver.find_element(By.NAME, 'password')
        passwordInput.send_keys('+p*%!VU.g7jyMYQ')
        submit = driver.find_element(By.CSS_SELECTOR, 'span.button.medium.orange.cursor')
        submit.click()
        return(True)
    except:
        print('\033[91mLogin  failed!\033[0m')


def fblogin():
    global NotfbLogged
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        print('found the email!')
        email= driver.find_element(By.NAME, 'email')
        password= driver.find_element(By.NAME, 'pass')
        email.send_keys(fnumber)
        password.send_keys(fpassword)
        password.send_keys(Keys.RETURN)
        NotfbLogged= False
        print('logged in successfully!')
    except TimeoutException:
        print('\033[91mLoading took too much time!\033[0m')


def closeChat():
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located(By.CSS_SELECTOR, 'div[aria-label="Close chat"]'))
        close= driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Close chat"]')
        close.click()
    except:
        print('no chat open!')


def earnBtn():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.earn_pages_button')))
        btn= driver.find_element(By.CSS_SELECTOR, 'a.earn_pages_button')
        btn.click()
        return True
    except:
        print('Earn btn failed!')
        driver.refresh()

def conformEarn():
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'img[title="Click On The Button To Confirm Interaction!"]')))
        driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]').click()
        return True
    except:
        print('no conform button')

def like():
    try:
        likeBtn=driver.find_element(By.CSS_SELECTOR,'div[aria-label="Like"]')
        likeBtn.click()
        return True
    except:
        print('\033[91mCould not like the post  \033[0m')


def follow():
    WebDriverWait(driver, 40).until(lambda driver: page_loaded(driver)) # wait for page to load
    closeChat()
    while(True):
        result=like()
        if (result):
            break
    time.sleep(1)
    print('followed the post')





# login()

def main():
    while(True):    #Login
        result=login()
        if (result):
            driver.implicitly_wait(7)
            break
        time.sleep(1)
    
    # WebDriverWait(driver, 400).until(lambda driver: page_loaded(driver))
    time.sleep(2)
    driver.get('https://www.like4like.org/user/earn-facebook.php')

    
    # iteration should start from here    

    for i in range(20):
        while(True):    #EarnBtn
            result=earnBtn()
            if (result):
                print('clicked the button!')
                break
            time.sleep(1)

        # Selecting the new window and maximazing it
        print(driver.window_handles)
        parentWindow= driver.current_window_handle
        driver.switch_to.window(driver.window_handles[1])
        driver.maximize_window()
        while(NotfbLogged):
            print('Should not be run on second go')
            fblogin()
            time.sleep(1)
        
        # following next
        follow()
        time.sleep(3)
        driver.close()
        driver.switch_to.window(parentWindow)

        while(True):    #conformEarn
            result=conformEarn()
            if (result):
                print('clicked the button!')
                break
            time.sleep(1)
        time.sleep(5)
    # Loop iteration ends here


main()

print("Over now")

time.sleep(10)


driver.quit()