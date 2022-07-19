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
# Importing the Keys class to use keys such as tab, enter, escape, etc. within webdriver
from selenium.webdriver.common.keys import Keys
# Importing WebDriverWait class to gain access to explicit waits
from selenium.webdriver.support.ui import WebDriverWait
# Importing ExpectedConditions class to verify element conditions / general conditions during explicit waits
from selenium.webdriver.support import expected_conditions
# Using time module for testing purposes
import time

# Configure and initializes the instance of chrome webdriver, options and service behavior defined above
chrome_options = Options()
# Session start
driver = webdriver.Chrome(options = chrome_options, service=Service(ChromeDriverManager().install()))

# Accessing the page of the video we'd like to scrape subtitles from
driver.get("https://youtu.be/eWgh_9jo67c")
# Pausing video to change settings before beginning
# videoPause = WebDriverWait(driver, timeout = 10).until(expected_conditions.element_to_be_clickable((By.ID, "movie-player")))
# Updating visual settings
# settingsButton = driver.find_element(By.CLASS_NAME, "ytp-settings-button")
# settingsButton.click()
# Unsure how to target quality as it's not a page element

# Toggling on fullscreen with webdriver wait
fullscreenButton = WebDriverWait(driver, timeout = 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "ytp-fullscreen-button")))
fullscreenButton.click()
screenshotTag = 0
playButton = driver.find_element(By.CLASS_NAME, "ytp-play-button")
# Every 3 seconds, a screenshot will be taken until the video ends
while playButton.get_attribute("title") != "Replay" :
    time.sleep(3)
    screenshotTag += 1
    driver.save_screenshot('./k2int/subtitle' + str(screenshotTag) + '.png')