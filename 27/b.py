import matplotlib.pyplot as plt
stores = ["Bucheon", "Incheon"]
sales = [120, 150]
plt.figure(figsize=(6, 4))
plt.bar(stores, sales, color="royalblue")
plt.ylabel("Sales (10,000 KRW)")
plt.title("Sales by store")
plt.tight_layout()
plt.show()

