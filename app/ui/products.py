import gradio as gr


def render_products(products):
    cards = []
    for product in products:
        cards.append(f"""
        <article class="product-card">
            <div class="product-card__image-wrap">
                <img src="{product['img']}" alt="{product['name']}" />
                <span class="product-badge">{product['badge']}</span>
            </div>
            <div class="product-card__body">
                <div class="product-card__meta">
                    <span>{product['category']}</span>
                    <span>{product['colors']} colours</span>
                </div>
                <h3>{product['name']}</h3>
                <div class="product-rating">{product['rating']} stars • {product['reviews']} reviews</div>
                <div class="product-card__footer">
                    <strong>{product['price_label']}</strong>
                    <button>Add to Bag</button>
                </div>
            </div>
        </article>
        """)

    gr.HTML(f"""
    <section class="section-block" id="new">
        <div class="section-heading split">
            <div>
                <span class="eyebrow">Trending Now</span>
                <h2>Best-selling picks from the latest drop</h2>
            </div>
            <p>Elevated product cards, stronger data, and retail-style hierarchy instantly make the page feel more premium.</p>
        </div>
        <div class="products-grid">
            {''.join(cards)}
        </div>
    </section>
    """)
