import pandas as pd

# 1. 기본 Series 및 결측치 테스트
s = pd.Series([80, 0, None, 120])
print(s.isna().tolist())
print(s.isna().sum())

# 2. 카페 데이터 로드 및 병합 (utf-8-sig로 인코딩 수정)
part1 = pd.read_csv("cafe_part1.csv", encoding="utf-8-sig")
part2 = pd.read_csv("cafe_part2.csv", encoding="utf-8-sig")
raw = pd.concat([part1, part2], ignore_index=True)
df = raw.copy()

print("컬럼 확인:", raw.columns.tolist())
print(raw.isna().sum())

# sales 컬럼 문자열 변환 후 결측치 확인
text = raw["sales"].astype("string")
text = text.str.replace(",", "", regex=False)
values = pd.to_numeric(text, errors="coerce")
print(raw.loc[values.isna(), ["record_id", "sales"]])

# 3. 결측치 및 평균 테스트
s = pd.Series([80, 100, None, 120])
print(s.dropna().mean())
print(s.fillna(0).mean())
print(s.fillna(s.median()).mean())

s = pd.DataFrame({
    "visitors": [80, 100, None, 120]
})
s["visitors_missing"] = s["visitors"].isna()
s["visitors_filled"] = s["visitors"].fillna(s["visitors"].median())
print(s)

# 4. 데이터프레임 전처리 (들여쓰기 오류 수정 완료)
df["store"] = df["store"].str.strip()

for col in ["quantity", "unit_price", "sales", "visitors"]:
    if col in df.columns:
        text = df[col].astype("string").str.replace(",", "", regex=False)
        df[col] = pd.to_numeric(text, errors="coerce")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.drop_duplicates().copy()

print("전처리 후 결측치 개수:")
print(df.isna().sum())

# 5. 매출액 계산 및 불일치 데이터 확인
calculated = df["quantity"] * df["unit_price"]
valid = df[["quantity", "unit_price", "sales"]]
valid = valid.notna().all(axis=1)
mismatch = valid & (df["sales"] != calculated)
print("매출 불일치 데이터:")
print(df.loc[mismatch, ["record_id", "sales"]])

# 6. 특정 레코드(R026) 확인
r = df.loc[df["record_id"] == "R026"]
print("R026 레코드:")
print(r[["quantity", "unit_price", "sales"]])
if not r.empty:
    print("계산된 매출액:", (r["quantity"] * r["unit_price"]).iloc[0])

negative = df["quantity"] < 0
print(df.loc[negative, ["record_id", "quantity"]])
print(df.loc[df["sales"] > 1000000])
before = df.copy()
check = pd.read_csv("source_check.csv")
for row in check.itertuples(index=False):
    df.loc[df["record_id"] == row.record_id, row.column] = row.confirmed_value

df["sales_recorded"] = df["sales"]
df["sales"] = df["quantity"] * df["unit_price"]
required = ["date", "store", "quantity", "unit_price"]
missing = df[required].isna().any(axis=1)
excluded = df.loc[missing].copy()
clean = df.dropna(subset=required).copy()
print(excluded["record_id"].tolist())
print(len(clean))

df["sales_recorded"] = df["sales"]
df["sales"] = df["quantity"] * df["unit_price"]
required = ["date", "store", "quantity", "unit_price"]
missing = df[required].isna().any(axis=1)
excluded = df.loc[missing].copy()
clean = df.dropna(subset=required).copy()
print(excluded["record_id"].tolist())
print(len(clean))