import pandas as pd

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
    orders,
    on="order_id",
    how="left",
    validate="many_to_one"
)
for table, key_cols in [
    (customers, ["customer_id"]),
    (products, ["product_id"]),
    (orders, ["order_id"])
    (items, ["order_id", "line_no"])
]:
     print(table[key_cols].isna().any().any())
     print(table[key_cols].duplicated(key_cols).sum())
analysis = items.merge(
    products,
    on="product_id",
    how="left",
    validate="many_to_one"
)
print(analysis)
g = analysis.groupby("store")["sales"]
totals = g.sum()
print(totals)