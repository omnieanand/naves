import gradio as gr
import os

# UI Components
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

# DATA + SERVICES
from app.data.dummy_data import products
from app.services.product_service import search_products, filter_products


# -------------------------
# APP UI
# -------------------------
with gr.Blocks(css=GLOBAL_CSS) as demo:

    # HEADER
    search = render_header()

    # 🌙 DARK MODE
    render_theme_toggle()

    # 🔄 CAROUSEL
    render_carousel()

    # HERO
    render_hero()

    # CATEGORIES
    render_categories()

    # 🧠 FILTERS
    category = render_filters()
    filtered_gallery = gr.Gallery(columns=4, label="Filtered Products")

    category.change(
        lambda c: [(p["img"], f"{p['name']} - {p['price']}")
                   for p in filter_products(products, c)],
        inputs=category,
        outputs=filtered_gallery
    )

    # PRODUCTS
    render_products(products)

    # PROMO
    render_promo()

    # MEMBERSHIP
    render_membership()

    # 🔍 SEARCH
    gr.Markdown("## 🔍 Search Results")
    result_gallery = gr.Gallery(columns=4)

    search.submit(
        search_products,
        inputs=search,
        outputs=result_gallery
    )

    # 🌙 DARK MODE SCRIPT
    gr.HTML("""
    <script>
    function toggleDarkMode() {
        const app = document.querySelector('body');
        app.classList.toggle("dark");
    }
    </script>
    """)
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