import csv

weather_rows = [
    ["09:00", "인천", 26, 50],
    ["09:00", "춘천", 23, 45]
]

with open("weather.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "지역", "기온", "습도"])
    writer.writerows(weather_rows)