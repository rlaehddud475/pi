import csv
import os
import pandas as pd

df = pd.read_csv("weather.csv")
print(df.head())
print("기온 평균:",

df["기온"].mean())
path = "weather.csv"

first = not os.path.exists(path)

with open(path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    if first:
        writer.writerow(["시각", "기온", "습도"])
        
    writer.writerow(["10:00", 25.1, 62])