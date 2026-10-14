import numpy as np

# a = [1, 2, 3]
# b = np.array([1, 2, 3])

# print(a * 2)
# print(b * 2)


# arr1=np.array([10,20,30])
# print(arr1.ndim)

# arr2=np.array([[10,20,30]])
# print(arr2.ndim)
# print(arr2.shape)

# import numpy as np

# scores = np.array([[80, 90, 75],
# [95, 88, 92]])

# print(scores.ndim)
# print(scores.shape)
# print(scores.size)
# print(scores.dtype)


# arr = np.array([10, 20, 30, 40, 50])

# print(arr[0])
# print(arr[-1])
# print(arr[1:4])
# print(arr[:3])

# scores = np.array([[80, 90, 75],
# [95, 88, 92],
# [70, 85, 78]])

# print(scores[1, 2])
# print(scores[0, :])
# print(scores[:, 1])

# temp = np.array([18.5, 20.0, 21.5, 23.0])

# print(temp + 1)
# print(temp * 1.8 + 32)
# print(temp >= 21)

speed = np.array([18, 25, 31, 42, 54])

# print(np.sum(speed))
# print(np.mean(speed))
# print(np.min(speed))
# print(np.max(speed))
# print(np.median(speed))

# mask = speed < 30
# print(mask)
# print(speed[mask])
# print(speed[speed < 30])


state = np.where(speed < 30, "혼잡", "원활")
print(state)