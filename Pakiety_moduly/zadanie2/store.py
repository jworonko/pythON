


products = {
    "cleb": dict(quantity=10, price=3),
    "masło": dict(quantity=20, price=8.5),
    "jabłka": dict(quantity=50, price=3.5),
}

def update_product_quantity (product_name, ordered_quantity):
    products [product_name] ["quantity"] -= ordered_quantity