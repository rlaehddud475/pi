import selenium
from selenium import webdriver

from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# print(selenium.__version__)
# driver = webdriver.Chrome()
# driver.get("https://www.naver.com")
# print(driver.title)
# driver.quit()

keyword = "빅데이터"
url = f"https://search.naver.com/search.naver?where=news&query={quote(keyword)}"
driver = webdriver.Chrome()
driver.get(url)
selector = 'a[href*="news.naver.com"]'
items = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
)
item = next(x for x in items if x.text.strip())
print(item.text.strip())
print(item.get_attribute("href"))