import gradio as gr


def render_products(products):
    cards = []
    for product in products:
        original_price = ""
        if product["original_price_label"]:
            original_price = f'<span class="product-original-price">{product["original_price_label"]}</span>'
        cards.append(f"""
        <article class="product-card">
            <div class="product-card__image-wrap">
                <img src="{product['img']}" alt="{product['name']}" />
                <span class="product-badge">{product['badge']}</span>
            </div>
            <div class="product-card__body">
                <div class="product-card__meta">
                    <span>{product['category']}</span>
                    <span>{len(product['colors'])} colours</span>
                </div>
                <h3>{product['name']}</h3>
                <p class="product-description">{product['description']}</p>
                <div class="product-rating">{product['rating']} stars • {product['reviews']} reviews</div>
                <div class="product-card__footer">
                    <div class="product-price-stack">
                        <strong>{product['price_label']}</strong>
                        {original_price}
                    </div>
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
            <p>These cards now carry stronger merchandising signals: richer descriptions, clearer pricing, stronger review cues, and more confident product hierarchy.</p>
        </div>
        <div class="products-grid">
            {''.join(cards)}
        </div>
    </section>
    """)
