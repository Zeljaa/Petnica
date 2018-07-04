import pandas as pd

m = pd.read_csv("files/order_products__prior.csv")
n = len(set(m["order_id"]))
t = len(set(m["product_id"]))

niz = [0] * 3 * t

for i in m["product_id"]:
    niz[i] += 1
niz.sort()

x = niz[-10:]

for i in x:
    print(i)