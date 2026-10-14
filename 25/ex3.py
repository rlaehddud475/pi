import pandas as pd
df = pd.read_csv(
"subway.csv",
encoding="cp949"
)

df['총이용객'] = df['승차총승객수'] + df['하차총승객수']

df = df[df['총이용객'] >= 8000]

df = df.sort_values('총이용객', ascending=False)

result = df[['역명', '총이용객']]
print(result)