purch_list = {
  "piekarnia": ["chleb", "bułki", "pączek"],
  "warzywniak": ["marchew", "seler", "rukola"]
}
print("Lista zakupów")

prod_number=0
for sklep, produkty in purch_list.items():
  capit_produkty = [p.upper() for p in produkty]
  prod_number= prod_number + len(produkty)
  print(f"Idę do {sklep.upper()} i kupuję tam {capit_produkty}.")

print(f"W sumie kupuję {prod_number} produktów.")

#Pierwszy commit na GitHub
#drugi commit na GitHub