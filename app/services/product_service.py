from app.data.dummy_data import products


def _format_gallery_item(product):
    return (
        product["img"],
        (
            f"{product['badge']}\n"
            f"{product['name']}\n"
            f"{product['category']}  |  {product['price_label']}  |  "
            f"{product['rating']} stars"
        ),
    )


def search_products(query):
    if not query:
        return [_format_gallery_item(product) for product in products]

    normalized_query = query.strip().lower()
    return [
        _format_gallery_item(product)
        for product in products
        if normalized_query in product["name"].lower()
        or normalized_query in product["category"].lower()
        or normalized_query in product["badge"].lower()
    ]


def get_all_products():
    return [_format_gallery_item(product) for product in products]


def filter_products(products, category):
    if category == "All":
        return products
    return [
        product for product in products
        if product["category"].lower() == category.lower()
    ]
