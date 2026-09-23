import pandas as pd

df = pd.read_csv("traffic.csv")

def level(speed):
    if speed < 20:
        return "혼잡"
    if speed < 35:
        return "서행"
    return "원활"

df["상태"] = df["평균속도"].apply(level)

road_mean = df.groupby("도로")["평균속도"].mean()

slowest = df.loc[df["평균속도"].idxmin()]
print(df)
with pd.ExcelWriter("traffic_result.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="원본데이터", index=False)
    road_mean.reset_index().to_excel(writer, sheet_name="도로별평균", index=False)

print(slowest[["시각", "도로", "평균속도", "상태"]])