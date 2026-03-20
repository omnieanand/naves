import gradio as gr
from app.ui.header import render_header
from app.ui.hero import render_hero
from app.ui.products import render_products
from app.ui.footer import render_footer
from app.services.product_service import search_products

with gr.Blocks(css="""
body {background-color: #ffffff;}
.header {display:flex; justify-content:space-between; align-items:center;}
.nav {gap:20px; display:flex;}
""") as demo:

    # HEADER
    search = render_header()

    # HERO
    render_hero()

    # PRODUCTS
    render_products()

    # SEARCH RESULTS
    gr.Markdown("## Search Results")
    result_gallery = gr.Gallery(columns=4)

    search.submit(search_products, inputs=search, outputs=result_gallery)

    # FOOTER
    render_footer()

demo.launch(server_name="0.0.0.0", server_port=7860)


