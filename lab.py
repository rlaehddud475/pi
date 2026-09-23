import csv
import os
import random
from datetime import datetime
import pandas as pd

path = "weather.csv"
first = not os.path.exists(path)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
city = random.choice(["서울", "부산", "인천", "춘천"])
temp = round(random.uniform(18, 30), 1)
humidity = random.randint(40, 85)
status = random.choice(["맑음", "흐림", "비, 강풍"])
row = [now, city, temp, humidity, status]

with open(path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if first:
        writer.writerow(["날짜","시각", "지역", "기온", "습도", "날씨"])
    writer.writerow(row)

df = pd.read_csv(path)
print(df.head(10))
print("평균 기온:", df["기온"].mean())
print("평균 습도:", df["습도"].mean())