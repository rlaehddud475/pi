import matplotlib.pyplot as plt
values = [32, 36, 40, 40, 44, 48, 52, 56]
plt.figure(figsize=(7, 4))
plt.hist(values, bins=4, color="royalblue")
plt.xlabel("Sales (10,000 KRW)")
plt.ylabel("Record count")
plt.tight_layout()
plt.show()
print(int(0.5 * 10**7))
print(40000000 / 10000)