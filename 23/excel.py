from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "날씨데이터"

ws.append(["시각", "지역", "기온", "습도"])
ws.append(["2026-10-01 09:00", "서울", 23.1, 58])

wb.save("weather.xlsx")