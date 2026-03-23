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


def _sort_products(items, sort_by):
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
    return items


def get_product_names():
    return [product["name"] for product in products]


def get_product_by_name(name):
    for product in products:
        if product["name"] == name:
            return product
    return products[0]


def render_product_detail_html(name):
    product = get_product_by_name(name)
    original_price = ""
    if product["original_price_label"]:
        original_price = f'<span class="detail-original-price">{product["original_price_label"]}</span>'

    feature_items = "".join(
        f"<li>{feature}</li>" for feature in product["features"]
    )
    color_items = "".join(
        f'<span class="detail-chip">{color}</span>' for color in product["colors"]
    )
    size_items = "".join(
        f'<span class="detail-size">{size}</span>' for size in product["sizes"]
    )
    gallery_items = "".join(
        f'<img src="{image}" alt="{product["name"]} gallery view" />'
        for image in product["gallery"]
    )

    return f"""
    <section class="product-detail">
        <div class="product-detail__gallery">
            <img class="product-detail__hero" src="{product['img']}" alt="{product['name']}" />
            <div class="product-detail__thumbs">{gallery_items}</div>
        </div>
        <div class="product-detail__content">
            <span class="eyebrow">{product['badge']}</span>
            <h2>{product['name']}</h2>
            <div class="detail-rating">{product['rating']} stars • {product['reviews']} verified reviews</div>
            <div class="detail-price-row">
                <strong>{product['price_label']}</strong>
                {original_price}
            </div>
            <p>{product['description']}</p>
            <div class="detail-meta">
                <span>{product['category']}</span>
                <span>{product['stock_status']}</span>
                <span>{product['delivery']}</span>
            </div>
            <div class="detail-block">
                <h4>Available colours</h4>
                <div class="detail-chip-row">{color_items}</div>
            </div>
            <div class="detail-block">
                <h4>Sizes</h4>
                <div class="detail-size-row">{size_items}</div>
            </div>
            <div class="detail-block">
                <h4>Why you'll like it</h4>
                <ul>{feature_items}</ul>
            </div>
            <div class="detail-note">{product['fit_note']}</div>
            <div class="detail-actions">
                <button>Add to Bag</button>
                <button class="secondary">Save to Wishlist</button>
            </div>
        </div>
    </section>
    """


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
        or normalized_query in product["description"].lower()
    ]


def get_all_products(sort_by="Featured"):
    return [
        _format_gallery_item(product)
        for product in _sort_products(products, sort_by)
    ]


def filter_products(items, category, badge, sort_by):
    filtered = list(items)

    if category != "All":
        filtered = [
            product for product in filtered
            if product["category"].lower() == category.lower()
        ]

    if badge != "All":
        filtered = [
            product for product in filtered
            if product["badge"].lower() == badge.lower()
        ]

    filtered = _sort_products(filtered, sort_by)
    return filtered


def get_filtered_gallery(category, badge, sort_by):
    filtered = filter_products(products, category, badge, sort_by)
    return [_format_gallery_item(product) for product in filtered]


def reset_filters():
    return "All", "All", "Featured", [_format_gallery_item(product) for product in products]


def get_nav_gallery(selection):
    if selection == "NAVES":
        items = products
        title = "All NAVES Products"
        subtitle = "Browse the full NAVES catalog across running, lifestyle, football, and streetwear."
    elif selection == "Outlet":
        items = [product for product in products if product["is_outlet"]]
        title = "Outlet Picks"
        subtitle = "Reduced-price styles and value-driven picks from the NAVES lineup."
    elif selection in {"Men", "Women", "Kids"}:
        items = [
            product for product in products
            if selection in product["audience"]
        ]
        title = f"{selection}'s Collection" if selection != "Kids" else "Kids Collection"
        subtitle = f"Shop NAVES styles curated for {selection.lower()}."
    else:
        items = [
            product for product in products
            if selection in product["nav_tags"]
        ]
        title = selection
        subtitle = f"Explore NAVES products grouped under {selection.lower()}."

    if not items:
        items = products
        title = "All NAVES Products"
        subtitle = "Browse the full NAVES catalog across running, lifestyle, football, and streetwear."

    heading = f"""
    <div class="catalog-heading">
        <span class="eyebrow">Top Navigation</span>
        <h2>{title}</h2>
        <p>{subtitle}</p>
    </div>
    """
    return heading, [_format_gallery_item(product) for product in items]
