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

from app.data.dummy_data import products
from app.services.product_service import search_products


# -------------------------
# APP UI
# -------------------------
with gr.Blocks(css=GLOBAL_CSS) as demo:

    # HEADER
    search = render_header()

    # HERO (Premium)
    render_hero()

    # CATEGORIES
    render_categories()

    # PRODUCTS
    render_products(products)

    # PROMO BANNER
    render_promo()

    # MEMBERSHIP
    render_membership()

    # SEARCH RESULTS (kept at bottom)
    gr.Markdown("## 🔍 Search Results")
    result_gallery = gr.Gallery(columns=4)

    search.submit(
        search_products,
        inputs=search,
        outputs=result_gallery
    )

    # FOOTER
    render_footer()


# -------------------------
# RUN APP
# -------------------------
port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)