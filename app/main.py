import os

from flask import Flask, abort, render_template, request

from app.services.product_service import (
    NAV_ROUTE_MAP,
    get_all_products,
    get_collection_page,
    get_filter_options,
    get_homepage_context,
    get_product_by_slug,
    get_related_products,
    get_site_context,
    search_products,
    sort_products,
)


app = Flask(__name__, template_folder="templates", static_folder="static")


@app.context_processor
def inject_site_context():
    return get_site_context()


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
