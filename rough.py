import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\')
options.add_argument('--disable-service-workers')
options.add_argument("--disable-features=Permissions-Policy")


driver = uc.Chrome( executable_path='C:\\Users\\chromedriver.exe',options=options)

driver.get('https://mail.google.com/mail/u/0/')
time.sleep(20)

driver.quit()