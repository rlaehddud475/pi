import numpy as np

scores = np.array([
    [80, 65, 32],
    [30, 80, 90],
    [100, 50, 40]
])

print(scores.shape)


print(np.mean(scores, axis=1))


print(np.mean(scores, axis=0))