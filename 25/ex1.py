import numpy as np

pm=np.array([32,48,55,71,29,44,63])
print(round(np.mean(pm), 2))
print(np.max(pm))
print(np.min(pm))
s=pm>=50
print(pm[s])
st=np.where(s,"주의","보통")
print(st)
