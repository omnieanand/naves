from app.data.dummy_data import (
    categories,
    hot_stories,
    link_groups,
    primary_nav,
    products,
    sport_tiles,
    style_shortcuts,
    trust_signals,
    utility_links,
)


NAV_ROUTE_MAP = {
    "Shoes": "shoes",
    "Men": "men",
    "Women": "women",
    "Kids": "kids",
    "Sports & Lifestyle": "sports_lifestyle",
    "Outlet": "outlet",
}


def get_site_context():
    return {
        "utility_links": utility_links,
        "primary_nav": primary_nav,
        "nav_route_map": NAV_ROUTE_MAP,
        "trust_signals": trust_signals,
    }


def get_homepage_context():
    return {
        "hero": {
            "kicker": "New Campaign",
            "title": "Supernova Run",
            "copy": "Precision cushioning, sharper traction, and daily speed for athletes who want clean performance.",
            "image": "https://images.unsplash.com/photo-1491553895911-0055eca6402d?auto=format&fit=crop&w=1800&q=80",
        },
        "hot_stories": hot_stories,
        "style_shortcuts": style_shortcuts,
        "categories": categories,
        "sport_tiles": sport_tiles,
        "link_groups": link_groups,
        "featured_products": products[:6],
    }


def get_all_products(sort_by="Featured"):
    return sort_products(products, sort_by)


def get_product_names():
    return [product["name"] for product in products]


def get_product_by_slug(slug):
    for product in products:
        if product["slug"] == slug:
            return product
    return None


def get_product_by_name(name):
    for product in products:
        if product["name"] == name:
            return product
    return None


def search_products(query):
    if not query:
        return products

    normalized_query = query.strip().lower()
    return [
        product
        for product in products
        if normalized_query in product["name"].lower()
        or normalized_query in product["category"].lower()
        or normalized_query in product["badge"].lower()
        or normalized_query in product["description"].lower()
    ]


def get_related_products(slug, limit=4):
    current = get_product_by_slug(slug)
    if not current:
        return products[:limit]

    related = [
        product
        for product in products
        if product["slug"] != slug and product["category"] == current["category"]
    ]
    if len(related) < limit:
        related.extend(
            product for product in products
            if product["slug"] != slug and product not in related
        )
    return related[:limit]


def get_cart_items(cart_map):
    items = []
    subtotal = 0
    total_items = 0

    for slug, quantity in cart_map.items():
        product = get_product_by_slug(slug)
        if not product:
            continue

        line_total = product["price"] * quantity
        subtotal += line_total
        total_items += quantity
        items.append(
            {
                "product": product,
                "quantity": quantity,
                "line_total": line_total,
                "line_total_label": f"₹{line_total:,}",
            }
        )

    return items, subtotal, total_items


def get_nav_products(selection):
    if selection == "NAVES":
        return products
    if selection == "Outlet":
        return [product for product in products if product["is_outlet"]]
    if selection in {"Men", "Women", "Kids"}:
        return [
            product for product in products
            if selection in product["audience"]
        ]
    return [
        product for product in products
        if selection in product["nav_tags"]
    ]


def get_collection_page(selection, sort_by="Featured"):
    items = get_nav_products(selection)
    if not items:
        items = products
        selection = "NAVES"

    title_map = {
        "Shoes": "Shoes",
        "Men": "Men",
        "Women": "Women",
        "Kids": "Kids",
        "Sports & Lifestyle": "Sports & Lifestyle",
        "Outlet": "Outlet",
        "NAVES": "All NAVES Products",
    }
    subtitle_map = {
        "Shoes": "Performance, sport, and lifestyle footwear built for movement.",
        "Men": "Technical silhouettes and everyday staples designed for men.",
        "Women": "Elevated styles for training, running, and everyday wear.",
        "Kids": "Comfort-first essentials with sporty durability for younger shoppers.",
        "Sports & Lifestyle": "Cross-category gear for movement, sport, and daily rotation.",
        "Outlet": "End-of-season prices and discounted NAVES picks.",
        "NAVES": "Browse the complete NAVES catalog.",
    }

    return {
        "slug": NAV_ROUTE_MAP.get(selection, ""),
        "selection": selection,
        "title": title_map.get(selection, selection),
        "subtitle": subtitle_map.get(selection, "Explore the NAVES catalog."),
        "products": sort_products(items, sort_by),
        "sort_by": sort_by,
    }


def get_filter_options():
    return {
        "sort_options": [
            "Featured",
            "Newest",
            "Top Rated",
            "Price: Low to High",
            "Price: High to Low",
        ]
    }


def sort_products(items, sort_by):
    if sort_by == "Price: Low to High":
        return sorted(items, key=lambda product: product["price"])
    if sort_by == "Price: High to Low":
        return sorted(items, key=lambda product: product["price"], reverse=True)
    if sort_by == "Top Rated":
        return sorted(
            items,
            key=lambda product: (product["rating"], product["reviews"]),
            reverse=True,
        )
    if sort_by == "Newest":
        badge_priority = {
            "New Arrival": 4,
            "Limited": 3,
            "Best Seller": 2,
            "Performance": 1,
        }
        return sorted(
            items,
            key=lambda product: badge_priority.get(product["badge"], 0),
            reverse=True,
        )
    return list(items)
