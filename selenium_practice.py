from selenium import webdriver

PATH = "C:/Users/taeho/Desktop/python_workplace/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://naver.com")