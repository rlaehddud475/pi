import matplotlib.pyplot as plt
days = [1, 2, 3, 4]
sales = [32, 40, 44, 48]
plt.figure(figsize=(7, 4))
plt.plot(days, sales, marker="o")
plt.title("Daily sales")
plt.xlabel("Day")
plt.ylabel("Sales (10,000 KRW)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()