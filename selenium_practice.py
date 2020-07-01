from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # To use Keys
import time

PATH = "C:/Users/taeho/Desktop/python_workplace/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://unsplash.com/")

search = driver.find_element_by_id("SEARCH_FORM_INPUT_nav-bar")
search.send_keys("github")
search.send_keys(Keys.RETURN)  # It works like hitting enter key

# It prints entire source codes behind
# print(driver.page_source)

time.sleep(5)  # it delays 5 seconds window is closed.

driver.quit()