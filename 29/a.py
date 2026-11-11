import pandas as pd
s = pd.Series(["C01/김민수/부천"])
parts = s.str.split("/", expand=True)
print(parts)
