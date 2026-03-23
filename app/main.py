import os

import gradio as gr

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
from app.services.product_service import (
    get_all_products,
    get_filtered_gallery,
    get_nav_gallery,
    get_product_names,
    render_product_detail_html,
    reset_filters,
    search_products,
)
from app.ui.categories import render_categories
from app.ui.discovery import (
    render_hot_stories,
    render_link_groups,
    render_signup_banner,
    render_sport_tiles,
    render_style_shortcuts,
)
from app.ui.filters import render_filters
from app.ui.footer import render_footer
from app.ui.header import render_header
from app.ui.hero import render_hero
from app.ui.membership import render_membership
from app.ui.product_detail import render_product_detail_picker
from app.ui.products import render_products
from app.ui.styles import GLOBAL_CSS
from app.ui.trust import render_trust_signals


with gr.Blocks(css=GLOBAL_CSS) as demo:
    gr.HTML('<div id="top"></div>')

    search, nav_buttons = render_header(utility_links, primary_nav)
    render_hero()

    gr.HTML('<div id="catalog"></div>')
    initial_catalog_heading, initial_catalog_items = get_nav_gallery("NAVES")
    nav_catalog_heading = gr.HTML(initial_catalog_heading)
    nav_catalog_gallery = gr.Gallery(
        value=initial_catalog_items,
        columns=3,
        label="Catalog",
        object_fit="cover",
        height="auto",
    )

    for label, button in nav_buttons.items():
        button.click(
            lambda selected=label: get_nav_gallery(selected),
            outputs=[nav_catalog_heading, nav_catalog_gallery],
        )

    render_hot_stories(hot_stories)
    render_style_shortcuts(style_shortcuts)
    render_categories(categories)
    render_sport_tiles(sport_tiles)
    render_link_groups(link_groups)

    gr.HTML("""
    <section class="section-block" id="running">
        <div class="section-heading split">
            <div>
                <span class="eyebrow">Discover</span>
                <h2>Browse by category, collection tag, and merchandising priority.</h2>
            </div>
            <p>Adidas is stronger here because users get many fast paths into the catalog. NAVES now needs the same depth and clarity.</p>
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

    render_signup_banner()
    render_membership()

    gr.HTML("""
    <section class="section-block" id="search">
        <div class="section-heading">
            <span class="eyebrow">Search</span>
            <h2>Search is another entry point into the catalog.</h2>
            <p>It should feel like part of the same retail system, not a separate tool.</p>
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
    render_footer()


port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port,
)
