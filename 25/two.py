import pandas as pd

data = {
"역명": ["서울역", "강남", "홍대입구"],
"승차": [1200, 1800, 1500],
"하차": [1100, 1750, 1420]
}

df = pd.DataFrame(data)
print(df)



