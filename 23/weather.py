import random
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
city = random.choice(["서울", "부산"])
temp = round(random.uniform(18, 30), 1)
humidity = random.randint(40, 85)
status = random.choice(["맑음", "흐림", "비, 강풍"])

row = [now, city, temp, humidity, status]

print(row)