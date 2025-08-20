inventory = {}

product1_name = "Mobile phone"
product1_quantity = 5
product1_price = 2000
product1_release_year=2020

inventory["product1_name"] = product1_name
inventory["product1_price"] = product1_price
inventory["product1_quantity"] = product1_quantity
inventory["product1_release_year"] = product1_release_year

product2_name = "Laptop"
product2_quantity = 10
product2_price = 50000
product2_release_year = 2023


inventory["product2_name"] = product2_name
inventory["product2_quantity"] = product2_quantity
inventory["product2_price"] = product2_price
inventory["product2_release_year"] = product2_release_year

del(inventory["product1_release_year"])
del(inventory["product2_release_year"])

print(inventory.keys())


