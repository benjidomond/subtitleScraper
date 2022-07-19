# Importing webdriver API to control the browser
from selenium import webdriver
# Service object handles browser driver, used to pass ChromeDriverManager config as chrome webdriver is initialized
from selenium.webdriver.chrome.service import Service
# Importing By functionality to use when finding elements with driver
from selenium.webdriver.common.by import By
# Options instance defines what the browser must support and how it should behave
from selenium.webdriver.chrome.options import Options
# ChromeDriverManager automatically fetches the most recent version of chrome webdriver and installs it
from webdriver_manager.chrome import ChromeDriverManager
# Importing WebDriverWait class to gain access to explicit waits
from selenium.webdriver.support.ui import WebDriverWait
# Importing ExpectedConditions class to verify element conditions / general conditions during explicit waits
from selenium.webdriver.support import expected_conditions
# Using time module for testing purposes
import time
# Importing Selenium's exceptions in order to reference them and handle them during execution
from selenium.common import exceptions as seleniumExceptions
# Importing the Keys class to use keys such as tab, enter, escape, etc. within webdriver
from selenium.webdriver.common.keys import Keys

# Configure and initializes the instance of chrome webdriver, options and service behavior defined above
chrome_options = Options()
# Session start
driver = webdriver.Chrome(options = chrome_options, service=Service(ChromeDriverManager().install()))

# Accessing Yandex Translate OCR
driver.get("https://translate.yandex.com/ocr")
try:
    sourceLangButton = WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "srcLangButton")))
    sourceLangButton.click()
    # Break out of loop or return if successful
except seleniumExceptions.TimeoutException:
    time.sleep(10)
    # Gives you time to solve the captcha. After solving the captcha, have Selenium hit enter
    textBox = driver.find_element(By.ID, "xuniq-0-1")
    textBox.send_keys(Keys.ENTER)
    sourceLangButton = WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "srcLangButton")))
    sourceLangButton.click()
# Continue logic here
