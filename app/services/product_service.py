from app.data.dummy_data import products

def search_products(query):
    return [
        (p["img"], f"{p['name']} - {p['price']}")
        for p in products if query.lower() in p["name"].lower()
    ]

def get_all_products():
    return [(p["img"], f"{p['name']} - {p['price']}") for p in products]

def filter_products(products, category):
    if category == "All":
        return products
    return [p for p in products if category.lower() in p["name"].lower()]