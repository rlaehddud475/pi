import pandas as pd
import matplotlib.pyplot as plt
part1 = pd.read_csv("cafe_part1.csv", encoding="utf-8-sig")
part2 = pd.read_csv("cafe_part2.csv", encoding="utf-8-sig")
raw = pd.concat([part1, part2], ignore_index=True)
df = raw.copy()
print(part1.shape, part2.shape, raw.shape)

df["store"] = df["store"].str.strip()

for col in ["quantity", "unit_price", "sales", "visitors"]:
    text = df[col].astype("string").str.replace(",", "", regex=False)
    df[col] = pd.to_numeric(text, errors="coerce")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.drop_duplicates().copy()
print(df.isna().sum())

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
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

clean["visitors_missing"] = clean["visitors"].isna()
store_median = clean.groupby("store")["visitors"].transform("median")
clean["visitors_filled"] = clean["visitors"].fillna(store_median)

print(clean["visitors"].isna().sum())
print(clean["visitors_filled"].isna().sum())

clean["sales_10k"] = clean["sales"] / 10000
clean["day"] = clean["date"].dt.day

summary = clean.groupby("store", as_index=False).agg(
    sales_total=("sales", "sum"), records=("record_id", "count")
)
print(summary)
daily = clean.groupby("date", as_index=False)["sales"].sum()
coverage = clean.groupby("date")["store"].nunique()
print(coverage[coverage < 2])
plt.plot(daily["date"], daily["sales"] / 10000, marker="o")
plt.ylabel("Observed sales (10,000 KRW)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.plot(daily["date"],
daily["sales"] / 10000)
plt.show()
print(before["sales"].mean())
print(before["sales"].median())
print(clean["sales"].mean())
print(clean["sales"].median())
print(clean["sales"].sum())
clean.to_csv("cafe_clean.csv",
            index=False, encoding="utf-8-sig")
excluded.to_csv("excluded_rows.csv",
            index=False, encoding="utf-8-sig")
summary.to_csv("store_summary.csv",
            index=False, encoding="utf-8-sig")
print(clean.shape)
