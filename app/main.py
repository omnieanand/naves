import os

from flask import Flask, abort, redirect, render_template, request, session, url_for

from app.services.product_service import (
    NAV_ROUTE_MAP,
    get_all_products,
    get_cart_items,
    get_collection_page,
    get_filter_options,
    get_homepage_context,
    get_nav_products,
    get_product_by_slug,
    get_related_products,
    get_site_context,
    search_products,
    sort_products,
)


app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY", "naves-dev-secret")


@app.context_processor
def inject_site_context():
    context = get_site_context()
    cart = session.get("cart", {})
    context["cart_count"] = sum(cart.values())
    return context


@app.route("/")
def home():
    context = get_homepage_context()
    return render_template("home.html", **context)


@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    sort_by = request.args.get("sort", "Featured")
    results = sort_products(search_products(query), sort_by)
    page = {
        "title": "Search Results",
        "subtitle": f"Results for '{query}'" if query else "Browse all NAVES products.",
        "products": results,
        "sort_by": sort_by,
        "selection": "Search",
        "slug": "search",
    }
    return render_template(
        "category.html",
        page=page,
        filter_options=get_filter_options(),
        search_query=query,
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
    product = get_product_by_slug(slug)
    if not product:
        abort(404)

    return render_template(
        "product.html",
        product=product,
        related_products=get_related_products(slug),
    )


@app.route("/cart")
def cart():
    cart_map = session.get("cart", {})
    items, subtotal, total_items = get_cart_items(cart_map)
    return render_template(
        "cart.html",
        cart_items=items,
        subtotal=subtotal,
        total_items=total_items,
    )


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
    page = get_collection_page(selection, sort_by)
    return render_template(
        "category.html",
        page=page,
        filter_options=get_filter_options(),
        search_query="",
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port, debug=False)
