import gradio as gr
import os

from app.ui.header import render_header
from app.ui.hero import render_hero
from app.ui.categories import render_categories
from app.ui.products import render_products
from app.ui.promo import render_promo
from app.ui.membership import render_membership
from app.ui.footer import render_footer
from app.ui.styles import GLOBAL_CSS

# NEW FEATURES
from app.ui.carousel import render_carousel
from app.ui.filters import render_filters
from app.ui.theme import render_theme_toggle

from app.data.dummy_data import products, categories
from app.services.product_service import search_products, filter_products, get_all_products


with gr.Blocks(css=GLOBAL_CSS) as demo:
    gr.HTML('<div id="top"></div>')

    search = render_header()
    render_theme_toggle()
    render_carousel()
    render_hero()
    render_categories(categories)

    gr.HTML("""
    <section class="section-block" id="running">
        <div class="section-heading split">
            <div>
                <span class="eyebrow">Discover</span>
                <h2>Filter the collection like a real storefront</h2>
            </div>
            <p>Professional shopping experiences feel organized. Users should be able to move from inspiration to a narrowed product set in one scroll.</p>
        </div>
    </section>
    """)
    category = render_filters()
    filtered_gallery = gr.Gallery(
        value=get_all_products(),
        columns=3,
        label="Filtered Products",
        object_fit="cover",
        height="auto",
    )

    category.change(
        lambda c: [(p["img"], f"{p['name']}\n{p['category']}  |  {p['price_label']}")
                   for p in filter_products(products, c)],
        inputs=category,
        outputs=filtered_gallery
    )

    render_products(products)
    render_promo()
    render_membership()

    gr.HTML("""
    <section class="section-block" id="sneakers">
        <div class="section-heading">
            <span class="eyebrow">Search</span>
            <h2>Search results should feel curated, not raw.</h2>
            <p>Even utility interactions benefit from stronger hierarchy, better spacing, and richer metadata.</p>
        </div>
    </section>
    """)
    result_gallery = gr.Gallery(columns=3, value=get_all_products(), object_fit="cover")

    search.submit(
        search_products,
        inputs=search,
        outputs=result_gallery
    )

    gr.HTML("""
    <script>
    function toggleDarkMode() {
        document.body.classList.toggle("dark");
    }
    </script>
    """)
    render_footer()


port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)
