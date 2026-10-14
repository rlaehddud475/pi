import selenium
from selenium import webdriver
print(selenium.__version__)
driver = webdriver.Chrome()
driver.get("https://www.naver.com")
print(driver.title)
driver.quit()
