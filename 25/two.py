import pandas as pd

data = {
"역명": ["서울역", "강남", "홍대입구"],
"승차": [1200, 1800, 1500],
"하차": [1100, 1750, 1420]
}

df = pd.DataFrame(data)
print(df)



df = pd.read_csv(
"subway.csv",
encoding="cp949"
)

print(df.head())

print(df["승차"])
print(df[["역명", "승차"]])
columns = ["역명", "승차", "하차"]
small = df[columns]
busy = df[df["승차"] >= 1500]
line2 = df[df["호선"] == "2호선"]
result = df[(df["승차"] >= 1500) &
(df["호선"] == "2호선")]