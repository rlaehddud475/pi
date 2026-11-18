import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df = pd.read_csv("cafe_analysis.csv")

print(df.shape)
print(df.isna().sum())
coverage = df.groupby("date")["store"].nunique()
print(coverage[coverage < 2])

b = df.loc[df["store"] == "부천점"].copy()
x = b["visitors"]
y = b["sales_10k"]
print(len(b), x.min(), x.max())
plt.scatter(x, y)
plt.xlabel("Visitors")
plt.ylabel("Sales (10,000 KRW)")
plt.show()

result = linregress(x, y)
print(round(result.slope, 3))
print(round(result.intercept, 3))
print(round(result.rvalue**2, 3))