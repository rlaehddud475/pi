from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
from selenium.webdriver.common.keys import Keys

driver.get("https://www.naver.com")
search = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "query"))
)
search.clear()
search.send_keys("빅데이터")
search.send_keys(Keys.ENTER)

print(driver.title)
print(driver.current_url)
items = driver.find_elements(
    By.CSS_SELECTOR, 'a[href*="news.naver.com"]'
)
titles, links = [], []
for item in items:
    title = item.text.strip()
    link = item.get_attribute("href")
    if not title or not link or link in links:
        continue
    titles.append(title)
    links.append(link)
    if len(titles) >= 10:
        break

print("수집 기사 수:", len(titles))