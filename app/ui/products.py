import gradio as gr
from app.services.product_service import get_all_products

def render_products():
    gr.Markdown("## Trending Products")

    return gr.Gallery(
        get_all_products(),
        columns=4,
        height=300
    )