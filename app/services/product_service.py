from app.data.dummy_data import (
    categories,
    hero_slides,
    hot_stories,
    link_groups,
    primary_nav,
    products,
    sport_tiles,
    style_shortcuts,
    trust_signals,
    utility_links,
)
from datetime import datetime


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
            "kicker": "Engineered For Champions",
            "title": "Run Faster. Push Harder.",
            "copy": "Performance footwear tuned for speed, confidence, and repeat wear. Designed to help athletes move with more intent every day.",
            "urgency": "New drop live now | Member discount ends tonight",
            "identity_points": [
                "Built for runners who refuse limits",
                "Designed for movement with identity",
                "Performance that still looks sharp off the track",
            ],
        },
        "hero_slides": hero_slides,
        "hot_stories": hot_stories,
        "style_shortcuts": style_shortcuts,
        "categories": categories,
        "sport_tiles": sport_tiles,
        "link_groups": link_groups,
        "featured_products": products[:6],
        "brand_pillars": [
            {
                "title": "Performance Tested",
                "copy": "Built to hold up through training, long runs, and daily wear.",
            },
            {
                "title": "Premium Materials",
                "copy": "Sharper uppers, better cushioning, and comfort-first construction.",
            },
            {
                "title": "Trusted by Athletes",
                "copy": "Designed for people who want confidence before every session.",
            },
        ],
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


def get_product_page_context(slug):
    product = get_product_by_slug(slug)
    if not product:
        return None

    sold_count = max(1000, product["reviews"] * 9)
    urgency_message = ""
    if "Low" in product["stock_status"] or "Limited" in product["stock_status"]:
        urgency_message = "Only a few pairs left in stock"
    elif product["is_outlet"]:
        urgency_message = "Sale price available for a limited time"

    trust_badges = [
        "14-day returns",
        "Secure checkout",
        "Fast delivery",
    ]

    usage_context_map = {
        "Running": "Built for runners who want daily comfort, responsive energy return, and a silhouette that still looks sharp after the session.",
        "Football": "Designed for players who want fast traction, locked-in confidence, and match-ready control.",
        "Sneakers": "Made for shoppers who want everyday identity, premium materials, and all-day wearability.",
        "Lifestyle": "Created for everyday rotation with comfort, cleaner styling, and understated confidence.",
    }

    review_highlights = [
        {
            "label": "Comfort Highlight",
            "copy": "Comfort feels immediate from the first wear.",
        },
        {
            "label": "Performance Note",
            "copy": "Support and stability stand out on longer sessions.",
        },
        {
            "label": "Style Feedback",
            "copy": "Looks strong enough for both training and everyday styling.",
        },
    ]

    confidence_points = [
        "Most buyers use this for repeat training and daily movement.",
        "Best match for shoppers who want responsive comfort with sharper styling.",
        "Works especially well for everyday sessions, commuting, and long wear windows.",
    ]

    delivery_reassurance = [
        "Free returns within 14 days",
        product["delivery"],
        "Verified payments and secure checkout",
    ]

    return {
        "product": product,
        "sold_count": sold_count,
        "urgency_message": urgency_message,
        "trust_badges": trust_badges,
        "usage_context": usage_context_map.get(product["category"], "Designed for people who want performance and everyday confidence."),
        "decision_helper": "True-to-size fit with a comfort-first shape and enough support for repeat wear.",
        "review_highlights": review_highlights,
        "confidence_points": confidence_points,
        "delivery_reassurance": delivery_reassurance,
        "wishlist_signal": f"{max(28, product['reviews'] // 3)} shoppers saved this this week",
    }


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


def get_wishlist_items(wishlist_slugs):
    return [
        product for product in products
        if product["slug"] in wishlist_slugs
    ]


def get_checkout_summary(cart_map):
    items, subtotal, total_items = get_cart_items(cart_map)
    shipping = 0 if subtotal >= 12000 else 499
    taxes = round(subtotal * 0.18)
    total = subtotal + shipping + taxes

    return {
        "items": items,
        "subtotal": subtotal,
        "subtotal_label": f"₹{subtotal:,}",
        "shipping": shipping,
        "shipping_label": "Free" if shipping == 0 else f"₹{shipping:,}",
        "taxes": taxes,
        "taxes_label": f"₹{taxes:,}",
        "total": total,
        "total_label": f"₹{total:,}",
        "total_items": total_items,
        "delivery_note": "Delivery in 2-4 business days for metro cities.",
    }


def build_order_invoice(cart_map, shipping_form):
    summary = get_checkout_summary(cart_map)
    order_number = f"NAV-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    placed_at = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    address_lines = [
        shipping_form["full_name"],
        shipping_form["address_line_1"],
    ]
    if shipping_form.get("address_line_2"):
        address_lines.append(shipping_form["address_line_2"])
    address_lines.append(
        f"{shipping_form['city']}, {shipping_form['state']} {shipping_form['postal_code']}"
    )
    address_lines.append(shipping_form["country"])

    return {
        "order_number": order_number,
        "placed_at": placed_at,
        "shipping": shipping_form,
        "address_lines": address_lines,
        "summary": summary,
        "payment_method": shipping_form.get("payment_method", "Card"),
    }


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
        "category_options": sorted({product["category"] for product in products}),
        "badge_options": sorted({product["badge"] for product in products}),
        "audience_options": ["Men", "Women", "Kids"],
        "price_options": [
            ("All Prices", ""),
            ("Under ₹10,000", "under-10000"),
            ("₹10,000 - ₹12,999", "10000-12999"),
            ("₹13,000 and above", "13000-plus"),
        ],
        "sort_options": [
            "Featured",
            "Newest",
            "Top Rated",
            "Price: Low to High",
            "Price: High to Low",
        ]
    }


def apply_filters(items, filters):
    filtered = list(items)

    category = filters.get("category", "").strip()
    badge = filters.get("badge", "").strip()
    audience = filters.get("audience", "").strip()
    price = filters.get("price", "").strip()

    if category:
        filtered = [
            product for product in filtered
            if product["category"] == category
        ]

    if badge:
        filtered = [
            product for product in filtered
            if product["badge"] == badge
        ]

    if audience:
        filtered = [
            product for product in filtered
            if audience in product["audience"]
        ]

    if price == "under-10000":
        filtered = [product for product in filtered if product["price"] < 10000]
    elif price == "10000-12999":
        filtered = [product for product in filtered if 10000 <= product["price"] <= 12999]
    elif price == "13000-plus":
        filtered = [product for product in filtered if product["price"] >= 13000]

    return filtered


def build_active_filters(filters):
    active = []
    for key, label in (
        ("category", "Category"),
        ("badge", "Badge"),
        ("audience", "Audience"),
        ("price", "Price"),
    ):
        value = filters.get(key, "").strip()
        if value:
            active.append({"label": label, "value": value})
    return active


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
