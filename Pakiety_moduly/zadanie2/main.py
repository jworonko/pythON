from actions import create_new_order

print("Witaj w sklepie spożywczym")
product_name = input("Jaki towar chcesz kupić")
quantity = int(input("Ile tego potrzebujesz?"))

result = create_new_order(product_name, quantity)
if result is not None:
    total_price = result["total_price"]
    print(f"Łączny koszt wyniesie: {total_price} PLN")