# ScienceViz Cafe

menu = {"tea": 25000, "coffee": 70000, "cake": 55000, "juice": 45000}

order = {"tea": 2, "coffee": 1, "cake": 1}

total = 0

print("===== ScienceViz Cafe =====")
print()

for product in order:
    quantity = order[product]
    price = menu[product]
    cost = price * quantity

    total += cost

    print("Product:", product)
    print("Quantity:", quantity)
    print("Cost:", cost)
    print()

print("----------------------")
print("Total:", total, "Toman")
print("----------------------")
