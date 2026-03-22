import gradio as gr

def render_products(products):
    gr.Markdown("## Trending Products")

    with gr.Row():
        for p in products:
            gr.HTML(f"""
            <div class="product-card">
                <img src="{p['img']}" style="width:100%; border-radius:10px;" />
                <h4>{p['name']}</h4>
                <p>{p['price']}</p>
            </div>
            """)