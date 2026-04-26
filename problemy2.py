def find_top_seller(products: dict, sales: dict) -> str:
    new_dict = {}
    for item in products:
        new_dict[item]=products[item]*sales[item]
    best_products = max(new_dict, key = new_dict.get)
    return best_products


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},{"Olma": 10,   "Banan": 5,    "Uzum": 8}))