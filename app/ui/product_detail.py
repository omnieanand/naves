import gradio as gr


def render_product_detail_picker(product_names, default_html):
    gr.HTML("""
    <section class="section-block" id="product-detail">
        <div class="section-heading split">
            <div>
                <span class="eyebrow">Product Detail</span>
                <h2>Let shoppers inspect one product deeply before they commit.</h2>
            </div>
            <p>A premium store needs more than a grid. Product detail is where trust, sizing, delivery, and conversion come together.</p>
        </div>
    </section>
    """)

    selector = gr.Dropdown(
        choices=product_names,
        value=product_names[0],
        label="Select a product to inspect",
        elem_classes="detail-selector",
    )
    detail_html = gr.HTML(default_html)
    return selector, detail_html
