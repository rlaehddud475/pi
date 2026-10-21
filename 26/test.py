import pandas as pd
import numpy as np

df = pd.read_csv("subway.csv",
encoding="cp949")

print(df.head())
print(df.shape)
print(df.columns)
df.info()

df = df.rename(columns={
"사용일자": "날짜",
"호선명": "호선",
"역명": "역명",
"승차총승객수": "승차",
"하차총승객수": "하차"
})

df = df[["날짜", "호선", "역명", "승차", "하차"]]

df["승차"] = pd.to_numeric(df["승차"],
errors="coerce")
df["하차"] = pd.to_numeric(df["하차"],
errors="coerce")

print(df[["승차", "하차"]].isna().sum())
df = df.dropna(subset=["역명", "승차", "하차"])
df = df.drop_duplicates()

df["총이용객"] = df["승차"] + df["하차"]

print(df[[
"날짜", "호선", "역명",
"승차", "하차", "총이용객"
]].head())

station = (
df.groupby("역명", as_index=False)[
["승차", "하차", "총이용객"]
].sum()
)

station = station.sort_values(
"총이용객", ascending=False
)

print(station.head(10))

values = station["총이용객"].to_numpy()

mean_value = np.mean(values)
median_value = np.median(values)
cut = np.percentile(values, 90)
print("평균:", round(mean_value))
print("중앙값:", round(median_value))
print("상위 10% 기준:", round(cut))

q50 = np.percentile(values, 50)
q90 = np.percentile(values, 90)

conditions = [
station["총이용객"] >= q90,
station["총이용객"] >= q50
]
choices = ["매우 혼잡", "보통 이상"]
station["이용수준"] = np.select(
conditions, choices, default="보통 이하"
)