import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.stats import ttest_rel
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
new_visitors = 120
predicted = (
    result.intercept
    + result.slope * new_visitors
)
print(round(predicted, 2))

paired = df.pivot(
index="date",
columns="store",
values="sales_10k"
).dropna()
print(paired.shape)
print(paired.head(2))
test = ttest_rel(
paired["부천점"],
paired["인천점"]
)
diff = paired["부천점"] - paired["인천점"]
print(round(diff.mean(), 2))
print(test.statistic, test.pvalue)