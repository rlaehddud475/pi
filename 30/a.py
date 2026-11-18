import pandas as pd
import matplotlib.pyplot as plt
raw = pd.read_csv("orders_raw.csv")
print(raw.shape)
print(raw["order_id"].tolist())
names = raw.groupby("customer_id")
counts = names["customer_name"].nunique()
print(counts)
customers = raw[[
"customer_id", "customer_name"
]].drop_duplicates()
products = raw[[
"product_id", "product_name", "unit_price"
]].drop_duplicates()
orders = raw[[
"order_id", "date", "store", "customer_id"
]].drop_duplicates()
items = raw[[
"order_id", "line_no",
"product_id", "quantity"
]].copy()
ids = customers["customer_id"]
print(ids.isna().sum())
print(ids.duplicated().sum())
keys = ["order_id", "line_no"]
print(items.duplicated(keys).sum())
analysis = items.merge(
products,
on="product_id",
how="left",
validate="many_to_one"
)
analysis = analysis.merge(
orders, on="order_id",
how="left", validate="many_to_one"
)
analysis["sales"] = (
analysis["quantity"] * analysis["unit_price"]
)

g = analysis.groupby("store")["sales"]
totals = g.sum()
print(totals)

daily = pd.read_csv("daily_sales.csv")
g = daily.groupby("store")["sales_10k"]
print(g.count())
print(daily["sales_10k"].isna().sum())

s = daily.loc[
daily["store"] == "부천점", "sales_10k"
]
print(s.mean())
print(s.median())
print(raw["product_id"].mode().tolist())

s = daily.loc[
daily["store"] == "부천점", "sales_10k"
]
print(s.mean())
print(s.median())
print(raw["product_id"].mode().tolist())

print(s.max() - s.min())
print(s.var(ddof=0))
print(round(s.std(ddof=0), 2))
print(s.max() - s.min())
print(s.var(ddof=0))
print(round(s.std(ddof=0), 2))
g = daily.groupby("store")["sales_10k"]
summary = g.agg(["count", "mean", "median"])
summary["std_pop"] = g.std(ddof=0)
print(summary.round(2))

a = daily.loc[
daily["store"] == "부천점", "sales_10k"
]
b = daily.loc[
daily["store"] == "인천점", "sales_10k"
]
plt.figure(figsize=(8, 4))
plt.plot(range(1, 6), a,
marker="o", label="Bucheon")
plt.plot(range(1, 6), b,
marker="o", label="Incheon")
plt.ylim(0, 80)
plt.xlabel("Day")
plt.ylabel("Sales (10,000 KRW)")
plt.legend()
plt.tight_layout()
plt.show()