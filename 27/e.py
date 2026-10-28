df["store"] = df["store"].str.strip()
for col in ["quantity", "unit_price", "sales", "visitors"]:
    text = df[col].astype("string").str.replace(",", "", regex=False)
df[col] = pd.to_numeric(text, errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.drop_duplicates().copy()
print(df.isna().sum())
