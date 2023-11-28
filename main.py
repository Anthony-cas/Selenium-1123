from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://yahoo.com")

search_bar = driver.find_element(By.CLASS_NAME, "_yb_1pduh")
#search_bar.clear() sometimes you may need to clear text thats in the element you are trying to target
search_bar.send_keys("twitch" + Keys.ENTER)



# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Twitch")

# link.click()


# time.sleep(20)

# driver.quit()


