# Open browser
# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome
time.sleep(5)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)
