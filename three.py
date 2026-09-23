import csv

rows = ["천안", "비,강풍", 21]

with open("weather_note.csv", "w", newline="", encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(["지역", "기후","온도"])
