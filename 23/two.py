import csv

rows = [["지역", "날씨", "기온"],
["서울", "맑음", 24.2],

["울산","비,강풍",25.0],

["광주","흐림,비",23.0]]

for name, enc in [("korean_utf8.csv", "utf-8"),
            ("korean_sig.csv", "utf-8-sig")]:
    with open(name, "w", newline="", encoding=enc) as f:
        csv.writer(f).writerows(rows)