import os

from flask import Flask, abort, flash, jsonify, redirect, render_template, request, session, url_for

from app.services.product_service import (
    NAV_ROUTE_MAP,
    apply_filters,
    build_order_invoice,
    build_active_filters,
    get_all_products,
    get_cart_items,
    get_checkout_summary,
    get_collection_page,
    get_filter_options,
    get_homepage_context,
    get_nav_products,
    get_product_page_context,
    get_product_by_slug,
    get_related_products,
    get_site_context,
    get_wishlist_items,
    search_products,
    sort_products,
)


app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY", "naves-dev-secret")


@app.context_processor
def inject_site_context():
    context = get_site_context()
    cart = session.get("cart", {})
    wishlist = session.get("wishlist", [])
    context["cart_count"] = sum(cart.values())
    context["wishlist_count"] = len(wishlist)
    context["wishlist_slugs"] = wishlist
    return context


@app.route("/")
def home():
    context = get_homepage_context()
    return render_template("home.html", **context)


@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    sort_by = request.args.get("sort", "Featured")
    filters = _get_filters_from_request()
    results = apply_filters(search_products(query), filters)
    results = sort_products(results, sort_by)
    page = {
        "title": "Search Results",
        "subtitle": f"Results for '{query}'" if query else "Browse all NAVES products.",
        "products": results,
        "sort_by": sort_by,
        "selection": "Search",
        "slug": "search",
        "result_count": len(results),
        "active_filters": build_active_filters(filters),
    }
    return render_template(
        "category.html",
        page=page,
        filter_options=get_filter_options(),
        search_query=query,
        selected_filters=filters,
    )


@app.route("/shoes")
def shoes():
    return _render_collection("Shoes")


@app.route("/men")
def men():
    return _render_collection("Men")


@app.route("/women")
def women():
    return _render_collection("Women")


@app.route("/kids")
def kids():
    return _render_collection("Kids")


@app.route("/sports-lifestyle")
def sports_lifestyle():
    return _render_collection("Sports & Lifestyle")


@app.route("/outlet")
def outlet():
    return _render_collection("Outlet")


@app.route("/products/<slug>")
def product_detail(slug):
    product_page = get_product_page_context(slug)
    if not product_page:
        abort(404)

    return render_template(
        "product.html",
        product=product_page["product"],
        product_page=product_page,
        related_products=get_related_products(slug),
        is_wishlisted=slug in session.get("wishlist", []),
    )


@app.route("/wishlist")
def wishlist():
    wishlist_slugs = session.get("wishlist", [])
    items = get_wishlist_items(wishlist_slugs)
    return render_template("wishlist.html", wishlist_items=items)


@app.route("/cart")
def cart():
    cart_map = session.get("cart", {})
    items, subtotal, total_items = get_cart_items(cart_map)
    summary = get_checkout_summary(cart_map)
    return render_template(
        "cart.html",
        cart_items=items,
        subtotal=subtotal,
        total_items=total_items,
        cart_summary=summary,
    )


@app.route("/checkout")
def checkout():
    cart_map = session.get("cart", {})
    summary = get_checkout_summary(cart_map)
    if not summary["items"]:
        return redirect(url_for("cart"))

    checkout_form = session.get("checkout_form", {
        "full_name": "",
        "address_line_1": "",
        "address_line_2": "",
        "city": "",
        "state": "",
        "postal_code": "",
        "country": "India",
        "phone": "",
        "email": "",
        "payment_method": "Card",
    })

    return render_template("checkout.html", checkout=summary, checkout_form=checkout_form)


@app.route("/checkout/place-order", methods=["POST"])
def place_order():
    cart_map = session.get("cart", {})
    summary = get_checkout_summary(cart_map)
    if not summary["items"]:
        return redirect(url_for("cart"))

    shipping_form = {
        "full_name": request.form.get("full_name", "").strip(),
        "address_line_1": request.form.get("address_line_1", "").strip(),
        "address_line_2": request.form.get("address_line_2", "").strip(),
        "city": request.form.get("city", "").strip(),
        "state": request.form.get("state", "").strip(),
        "postal_code": request.form.get("postal_code", "").strip(),
        "country": request.form.get("country", "India").strip(),
        "phone": request.form.get("phone", "").strip(),
        "email": request.form.get("email", "").strip(),
        "payment_method": request.form.get("payment_method", "Card").strip(),
    }

    required_fields = [
        "full_name",
        "address_line_1",
        "city",
        "state",
        "postal_code",
        "country",
        "phone",
        "email",
    ]
    if any(not shipping_form[field] for field in required_fields):
        session["checkout_form"] = shipping_form
        return redirect(url_for("checkout"))

    invoice = build_order_invoice(cart_map, shipping_form)
    session["last_order"] = invoice
    session["checkout_form"] = shipping_form
    session["cart"] = {}
    flash("Order placed successfully. Your invoice is ready.", "success")
    return redirect(url_for("invoice"))


@app.route("/invoice")
def invoice():
    order = session.get("last_order")
    if not order:
        return redirect(url_for("home"))
    return render_template("invoice.html", order=order)


@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    slug = request.form.get("slug", "")
    quantity = max(int(request.form.get("quantity", 1)), 1)
    redirect_to = request.form.get("redirect_to") or request.referrer or url_for("cart")

    product = get_product_by_slug(slug)
    if not product:
        abort(404)

    cart_map = session.get("cart", {})
    cart_map[slug] = cart_map.get(slug, 0) + quantity
    session["cart"] = cart_map
    flash("Added to bag successfully.", "success")
    return redirect(redirect_to)


@app.route("/wishlist/add", methods=["POST"])
def add_to_wishlist():
    slug = request.form.get("slug", "")
    redirect_to = request.form.get("redirect_to") or request.referrer or url_for("wishlist")
    product = get_product_by_slug(slug)
    if not product:
        abort(404)

    wishlist_slugs = session.get("wishlist", [])
    added = False
    if slug not in wishlist_slugs:
        wishlist_slugs.append(slug)
        session["wishlist"] = wishlist_slugs
        added = True
        flash("Saved to wishlist.", "success")
    else:
        flash("Already in your wishlist.", "success")

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify(
            {
                "ok": True,
                "wishlist_count": len(session.get("wishlist", [])),
                "is_wishlisted": True,
                "message": "Saved to wishlist." if added else "Already in your wishlist.",
            }
        )
    return redirect(redirect_to)


@app.route("/wishlist/remove", methods=["POST"])
def remove_from_wishlist():
    slug = request.form.get("slug", "")
    redirect_to = request.form.get("redirect_to") or request.referrer or url_for("wishlist")
    wishlist_slugs = session.get("wishlist", [])
    if slug in wishlist_slugs:
        wishlist_slugs = [item for item in wishlist_slugs if item != slug]
        session["wishlist"] = wishlist_slugs
        flash("Removed from wishlist.", "success")

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify(
            {
                "ok": True,
                "wishlist_count": len(session.get("wishlist", [])),
                "is_wishlisted": False,
                "message": "Removed from wishlist.",
            }
        )
    return redirect(redirect_to)


@app.route("/cart/update", methods=["POST"])
def update_cart():
    slug = request.form.get("slug", "")
    quantity = int(request.form.get("quantity", 1))

    cart_map = session.get("cart", {})
    if slug in cart_map:
        if quantity <= 0:
            cart_map.pop(slug, None)
        else:
            cart_map[slug] = quantity
        session["cart"] = cart_map

    return redirect(url_for("cart"))


@app.route("/cart/remove", methods=["POST"])
def remove_from_cart():
    slug = request.form.get("slug", "")
    cart_map = session.get("cart", {})
    cart_map.pop(slug, None)
    session["cart"] = cart_map
    return redirect(url_for("cart"))


def _render_collection(selection):
    sort_by = request.args.get("sort", "Featured")
    filters = _get_filters_from_request()
    page = get_collection_page(selection, sort_by)
    page["products"] = sort_products(apply_filters(page["products"], filters), sort_by)
    page["result_count"] = len(page["products"])
    page["active_filters"] = build_active_filters(filters)
    return render_template(
        "category.html",
        page=page,
        filter_options=get_filter_options(),
        search_query="",
        selected_filters=filters,
    )


def _get_filters_from_request():
    return {
        "category": request.args.get("category", ""),
        "badge": request.args.get("badge", ""),
        "audience": request.args.get("audience", ""),
        "price": request.args.get("price", ""),
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port, debug=False)
