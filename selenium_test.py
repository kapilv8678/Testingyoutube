from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Set Chrome options to enable PDF printing
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)
chrome_options.add_argument('--disable-gpu')  # Disable GPU (optional)
chrome_options.add_argument('home/kapildev//output.pdf')
# Navigate to the YouTube website
driver.get("https://www.youtube.com/")
time.sleep(10)

# Locate the search box and perform a search
textbox = driver.find_element(By.XPATH, '//form[@class="ytSearchboxComponentSearchForm"]/input')
textbox.send_keys('python')
clickbutton = driver.find_element(By.XPATH, '//button[@class="ytSearchboxComponentSearchButton"]/yt-icon')
clickbutton.click()
time.sleep(8)
# Locate all video titles
titles = driver.find_elements(By.XPATH, '//a[@id="video-title"]')

# Print the titles
for index, title in enumerate(titles):
    print(f"Video {index + 1}: {title.text}")

# Optionally wait before closing the driver
time.sleep(10)

# Close the driver
driver.quit()

