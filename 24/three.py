import time
import pandas as pd
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

keyword = "빅데이터"
url = f"https://search.naver.com/search.naver?where=news&query={quote(keyword)}"

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

driver.get(url)
time.sleep(2)

news_selector = "a.info"
WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, news_selector))
)

titles, links = [], []
elements = driver.find_elements(By.CSS_SELECTOR, news_selector)

for i in range(len(elements)):
    try:
        current_elements = driver.find_elements(By.CSS_SELECTOR, news_selector)
        item = current_elements[i]
        title = item.text.replace("새 창 열림", "").replace("새창열림", "").strip()
        link = item.get_attribute("href")
        if not title or not link or link in links or "news.naver.com" not in link:
            continue
        titles.append(title)
        links.append(link)
        if len(titles) >= 10:
            break
    except Exception:
        continue

print("수집 기사 수:", len(titles))

print("\n[기사 상세 목록]")
for idx, (title, link) in enumerate(zip(titles, links), 1):
    print(f"{idx}번째 | 제목: {title} | 링크: {link}")

df = pd.DataFrame({
    "검색어": [keyword] * len(titles),
    "제목": titles,
    "링크": links
})

df.to_csv("news_result.csv", index=False, encoding="utf-8-sig")

print("\n[DataFrame 출력]")
print(df)
print("CSV 파일 저장 완료: news_result.csv")

driver.quit()