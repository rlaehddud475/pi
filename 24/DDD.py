import numpy as np

lengths = np.array([12, 18, 9, 25, 16])

print(lengths)
print("차원:", lengths.ndim)
print("모양:", lengths.shape)
print("개수:", lengths.size)
print("자료형:", lengths.dtype)
lengths = np.array([len(t) for t in titles])

avg = lengths.mean()
print("평균:", round(avg, 1))
print("최대:", lengths.max())
print("최소:", lengths.min())
print("표준편차:", round(lengths.std(), 1))