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

options = Options()
options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\')
options.add_argument('--disable-service-workers')
options.add_argument("--disable-features=Permissions-Policy")

driver = uc.Chrome( executable_path='C:\\Users\\chromedriver.exe',options=options)

passwords= [['Anant124', '+p*%!VU.g7jyMYQ'], ['Ravi124', 'piQBcSXI']]

driver.get("https://www.like4like.org/")
# fnumber= input('Enter the facebook number!')
# fpassword= input('Enter the facebook password!')
NotfbLogged= False
ynumber='brijtiwarisir@gmail.com'
ypassword='Anant@hero'
driver.maximize_window()

def page_loaded(driver):
    return driver.execute_script('return document.readyState') == 'complete'

def login():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
        loginLink= driver.find_element(By.LINK_TEXT, 'Login')
        loginLink.click()

        emailInput= driver.find_element(By.NAME, 'username')
        emailInput.send_keys(passwords[1][0])      #Ravi124
        passwordInput= driver.find_element(By.NAME, 'password')
        passwordInput.send_keys(passwords[1][1])       #piQBcSXI
        submit = driver.find_element(By.CSS_SELECTOR, 'span.button.medium.orange.cursor')
        submit.click()
        time.sleep(3)
        return(True)
    except:
        print('\033[91mLogin  failed!\033[0m')


def ytlogin():
    global NotfbLogged
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Sign in"]')))
        print('found the google button!')
        googleBtn= driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Sign in"]')
        googleBtn.click()
        email= driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
        email.send_keys(ynumber)
        email.send_keys(Keys.RETURN)
        password= driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        password.send_keys(ypassword)
        password.send_keys(Keys.RETURN)
        NotfbLogged= True
        print('logged in successfully!')
        time.sleep(3)
    except TimeoutException:
        print('\033[91mLoading took too much time!\033[0m')


def closeChat():
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located(By.CSS_SELECTOR, 'button.ytp-ad-skip-button'))
        close= driver.find_element(By.CSS_SELECTOR, 'div.ytp-ad-skip-button')
        close.click()
    except:
        print('no ads open!')


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
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button.yt-spec-button-shape-next.yt-spec-button-shape-next--tonal.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-leading.yt-spec-button-shape-next--segmented-start')))
        likeBtn=driver.find_element(By.CSS_SELECTOR,'button.yt-spec-button-shape-next.yt-spec-button-shape-next--tonal.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-leading.yt-spec-button-shape-next--segmented-start')
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
    
    WebDriverWait(driver, 400).until(lambda driver: page_loaded(driver))
    driver.get('https://www.like4like.org/user/earn-youtube.php')

    
    # iteration should start from here    

    for i in range(50):
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
            ytlogin()
            time.sleep(1)
        
        # following next
        follow()
        time.sleep(4)
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