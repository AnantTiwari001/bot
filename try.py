from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


# Set up Firefox options
firefox_options = Options()
firefox_options.set_preference("dom.webnotifications.enabled", False)

# Set up proxy server configuration
proxy_ip = "202.133.53.36"
proxy_port = 80

# Set up proxy settings in Firefox options
firefox_options.set_preference("network.proxy.type", 1)
firefox_options.set_preference("network.proxy.http", proxy_ip)
firefox_options.set_preference("network.proxy.http_port", proxy_port)

# Initialize the Firefox WebDriver with the options and proxy settings
driver = webdriver.Firefox(options=firefox_options)

# Perform actions with the WebDriver
# For example:
driver.get("https://whatismyipaddress.com/")

time.sleep(15)

driver.quit()