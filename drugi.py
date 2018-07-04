import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


m = pd.read_csv("files/order_products__prior.csv")
n = len(set(m["order_id"]))
t = len(set(m["product_id"]))
print("Prosecno: " + str(n/t))
niz = [0] * 3 * n
for i in Mesovita["order_id"]:
    niz[i] += 1
b = np.array(niz)
a = np.array(range(0, 3*n))

plt.plot(a, b)
plt.show()