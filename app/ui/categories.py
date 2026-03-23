import gradio as gr


def render_categories(categories):
    cards = []
    for category in categories:
        cards.append(f"""
        <article class="category-card">
            <img src="{category['img']}" alt="{category['name']}" />
            <div class="category-card__body">
                <span>Shop now</span>
                <h3>{category['name']}</h3>
                <p>{category['caption']}</p>
            </div>
        </article>
        """)

    gr.HTML(f"""
    <section class="section-block" id="categories">
        <div class="section-heading">
            <span class="eyebrow">Categories</span>
            <h2>Find your lane</h2>
            <p>Discover collections tailored for performance, sport, and everyday rotation.</p>
        </div>
        <div class="category-grid">
            {''.join(cards)}
        </div>
    </section>
    """)
