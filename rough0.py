from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\local\\Mozilla\\Firefox\\Profiles\\')
options.add_argument('--disable-service-workers')
# options.add_argument("--disable-features=Permissions-Policy")
options.profile = 'C:\\Users\\User\\AppData\\local\\Mozilla\\Firefox\\Profiles\\8dkqulh5.default'

driver = webdriver.Firefox(firefox_profile=options.profile, options=options)

driver.get('https://mail.google.com/mail/u/0/')
time.sleep(20)

driver.quit()
