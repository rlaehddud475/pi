import pandas as pd
raw = pd.read_csv("orders_raw.csv")
print(raw.shape)
print(raw["order_id"].tolist())
names = raw.groupby("customer_id")
counts = names["customer_name"].nunique()
print(counts)