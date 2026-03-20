from app.data.dummy_data import products

def search_products(query):
    return [
        (p["img"], f"{p['name']} - {p['price']}")
        for p in products if query.lower() in p["name"].lower()
    ]

def get_all_products():
    return [(p["img"], f"{p['name']} - {p['price']}") for p in products]