from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import random

firefox_options = Options()
firefox_options.set_preference("dom.webnotifications.enabled", False)

driver = webdriver.Firefox(options=firefox_options)

driver.get("https://www.facebook.com/")
fnumber='9814253523'
fpassword='Anant@123'
driver.maximize_window()

def fblogin():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        print('found the email!')
        email= driver.find_element(By.NAME, 'email')
        password= driver.find_element(By.NAME, 'pass')
        email.send_keys(fnumber)
        password.send_keys(fpassword)
        password.send_keys(Keys.RETURN)
        print('logged in successfully!')
        time.sleep(3)
    except TimeoutException:
        print('\033[91mLoading took too much time!\033[0m')

def React(element):
    # Only liking for now
    # need to add dynamic reacting based on most used emoje

    # Reactions= driver.find_element(By.CSS_SELECTOR,'span[aria-label="See who reacted to this"]')
    # mostEmoje= Reactions.find_element(By.XPATH,"./*/*/*/*/*") 
    # attrValue= mostEmoje.get_attribute("attribute_name")
    # splited= attrValue.split(':')
    


    element.click()
    print('reacted to the post!')
    time.sleep(2)


def main():
    fblogin()
    driver.implicitly_wait(25)
    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Like"]')))

    i=0
    while i<10: 
        try:
            LikeBtns= driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Like"]')
            print('start wait')
            try:
                WebDriverWait(driver,40).until(EC.element_to_be_clickable(LikeBtns[i]))
            except:
                print('Wait failed here! element not clickable')
            print('end wait')
            LikeBtns[i].click()
            time.sleep(5)
            i+=1
            time.sleep(5)
        except Exception as e :
            print('exception occured')
            print(e)
            continue


        # while True:
        #     driver.execute_script("arguments[0].scrollIntoView();", LikeBtns[i])
        #     if (EC.visibility_of_element_located((By.ID, "myElementId"))):
        #         break
        # random_number = random.randint(1, 7)
        # if random_number == 5:
        #     # React(LikeBtns[i])
        #     LikeBtns[i].click()

main()

print('done')
time.sleep(15)