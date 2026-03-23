import gradio as gr


def render_hero():
    gr.HTML("""
    <section class="hero-shell">
        <img
            class="hero-image"
            src="https://images.unsplash.com/photo-1491553895911-0055eca6402d?auto=format&fit=crop&w=1800&q=80"
            alt="Naves hero campaign"
        />
        <div class="hero-overlay">
            <span class="hero-kicker">New Campaign</span>
            <h1>Supernova Run</h1>
            <p>Precision cushioning, sharper traction, and daily speed for athletes who want clean performance.</p>
            <div class="hero-actions">
                <a class="btn btn-light" href="#new">Shop Men</a>
                <a class="btn btn-light" href="#new">Shop Women</a>
            </div>
        </div>
    </section>
    """)
