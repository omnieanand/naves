import gradio as gr


def render_trust_signals(items):
    cards = []
    for item in items:
        cards.append(f"""
        <div class="trust-card">
            <strong>{item}</strong>
            <p>Visible trust cues reduce hesitation and make premium storefronts feel safer to buy from.</p>
        </div>
        """)

    gr.HTML(f"""
    <section class="section-block">
        <div class="section-heading">
            <span class="eyebrow">Why Buy Here</span>
            <h2>Trust signals should be visible before the customer has questions.</h2>
            <p>Shipping, returns, and payment confidence should support browsing instead of hiding in the footer.</p>
        </div>
        <div class="trust-grid">
            {''.join(cards)}
        </div>
    </section>
    """)
