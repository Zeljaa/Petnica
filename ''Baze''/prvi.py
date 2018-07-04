import pandas as pd

porudzbine = pd.read_csv("instacart_2017_05_01/orders.csv")
proizvodi = pd.read_csv("instacart_2017_05_01/products.csv")

brojProizvoda = len(set(Proizvodi["product_id"]))
brojNarudzbina = len(set(Porudzbine["order_id"]))
brojKorisnika = len(set(Porudzbine["user_id"]))
print("Broj korisnika: " + str(brojKorisnika) + " broj proizvoda:" + str(brojProizvoda) + " broj narudzbina: " + str(brojNarudzbina))
