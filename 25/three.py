import pandas as pd

df = pd.read_csv(
"subway.csv",
encoding="cp949"
)

print(df.head())

print(df["승차총승객수"])
print(df[["역명", "승차총승객수"]])
columns = ["역명", "승차총승객수", "하차총승객수"]
small = df[columns]
busy = df[df["승차총승객수"] >= 1500]
line2 = df[df["호선명"] == "2호선"]
result = df[(df["승차총승객수"] >= 1500) &
(df["호선명"] == "2호선")]
df["승차총승객수"] = pd.to_numeric(df["승차총승객수"], errors="coerce")
df = df.dropna(subset=["역명", "승차총승객수", "하차총승객수"])
df = df.drop_duplicates()
df["총이용객"] = df["승차총승객수"] + df["하차총승객수"]
df["승하차차이"] = abs(df["승차총승객수"] - df["하차총승객수"])

print(df.head())

top3 = (
df.sort_values("승차총승객수", ascending=False)
.head(3)
)

print(top3[["역명", "사용일자"]])

station = (
df.groupby("역명", as_index=False)["승차총승객수"]
.sum()
)

line = (
df.groupby("호선명", as_index=False)["승차총승객수"]
.mean()
)
print(line.sort_values("승차총승객수", ascending=False).head(3))
print(station.sort_values("승차총승객수", ascending=False).head(3))


values = df["총이용객"].to_numpy()

print(type(values))
print(np.mean(values))
print(np.percentile(values, 90))