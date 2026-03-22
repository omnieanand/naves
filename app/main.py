import os

import gradio as gr

from app.data.dummy_data import categories, products, trust_signals
from app.services.product_service import (
    get_all_products,
    get_filtered_gallery,
    get_product_names,
    render_product_detail_html,
    reset_filters,
    search_products,
)
from app.ui.carousel import render_carousel
from app.ui.categories import render_categories
from app.ui.filters import render_filters
from app.ui.footer import render_footer
from app.ui.header import render_header
from app.ui.hero import render_hero
from app.ui.membership import render_membership
from app.ui.product_detail import render_product_detail_picker
from app.ui.products import render_products
from app.ui.promo import render_promo
from app.ui.styles import GLOBAL_CSS
from app.ui.theme import render_theme_toggle
from app.ui.trust import render_trust_signals


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
                <h2>Filter, sort, and curate like a real commerce experience.</h2>
            </div>
            <p>Discovery improves when shoppers can narrow by category, collection signal, and rank products by relevance, rating, or price.</p>
        </div>
    </section>
    """)
    category, badge, sort_by, clear_filters = render_filters()
    filtered_gallery = gr.Gallery(
        value=get_all_products(),
        columns=3,
        label="Filtered Products",
        object_fit="cover",
        height="auto",
    )

    for component in (category, badge, sort_by):
        component.change(
            get_filtered_gallery,
            inputs=[category, badge, sort_by],
            outputs=filtered_gallery,
        )

    clear_filters.click(
        reset_filters,
        outputs=[category, badge, sort_by, filtered_gallery],
    )

    render_products(products)
    render_trust_signals(trust_signals)

    product_selector, detail_html = render_product_detail_picker(
        get_product_names(),
        render_product_detail_html(products[0]["name"]),
    )
    product_selector.change(
        render_product_detail_html,
        inputs=product_selector,
        outputs=detail_html,
    )

    render_promo()
    render_membership()

    gr.HTML("""
    <section class="section-block" id="sneakers">
        <div class="section-heading">
            <span class="eyebrow">Search</span>
            <h2>Search results should feel curated, consistent, and useful.</h2>
            <p>Even utility tools should keep the same design language so the store feels premium at every touchpoint.</p>
        </div>
    </section>
    """)
    result_gallery = gr.Gallery(
        columns=3,
        value=get_all_products(),
        label="Search Results",
        object_fit="cover",
        height="auto",
    )

    search.submit(
        search_products,
        inputs=search,
        outputs=result_gallery,
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
    server_port=port,
)
