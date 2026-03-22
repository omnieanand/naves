import gradio as gr


def render_hero():
    gr.HTML("""
    <section class="hero-shell">
        <div class="hero-copy">
            <span class="eyebrow">New season / high performance</span>
            <h1>Built like a flagship launch, not a prototype.</h1>
            <p>
                Premium footwear, sharp editorial storytelling, and a store experience
                that feels fast, credible, and brand-led from the first scroll.
            </p>
            <div class="hero-actions">
                <a class="btn btn-light" href="#new">Shop New Arrivals</a>
                <a class="btn btn-ghost" href="#membership">Join Membership</a>
            </div>
        </div>
        <div class="hero-metrics">
            <div>
                <strong>250+</strong>
                <span>style variants</span>
            </div>
            <div>
                <strong>48h</strong>
                <span>dispatch promise</span>
            </div>
            <div>
                <strong>4.8/5</strong>
                <span>community rating</span>
            </div>
        </div>
        <div class="hero-spotlight">
            <span>Featured drop</span>
            <h3>Naves Adrenaline Pro</h3>
            <p>Race-inspired cushioning with a street-ready silhouette.</p>
        </div>
        <img
            class="hero-image"
            src="https://images.unsplash.com/photo-1518002171953-a080ee817e1f?auto=format&fit=crop&w=1600&q=80"
            alt="Naves campaign hero"
        />
    </section>
    """)
