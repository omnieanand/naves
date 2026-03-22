import gradio as gr


def render_hero():
    gr.HTML("""
    <section class="hero-shell">
        <div class="hero-panel">
            <div class="hero-copy">
                <span class="eyebrow">Spring / Summer 2026</span>
                <h1>Performance, styled with restraint.</h1>
                <p>
                    A cleaner white-first storefront, sharper product storytelling,
                    and premium essentials built for movement across sport and city life.
                </p>
                <div class="hero-actions">
                    <a class="btn btn-dark" href="#new">Shop New Arrivals</a>
                    <a class="btn btn-outline" href="#product-detail">Explore Product Detail</a>
                </div>
            </div>
            <div class="hero-note-card">
                <span class="eyebrow">Editor's Note</span>
                <h3>Make the product the hero.</h3>
                <p>
                    The strongest retail homepages use space, image quality, and typography
                    to create confidence before users ever touch a filter.
                </p>
            </div>
        </div>
        <div class="hero-floating-metrics">
            <div>
                <strong>4.8/5</strong>
                <span>average product rating</span>
            </div>
            <div>
                <strong>14 days</strong>
                <span>free returns window</span>
            </div>
            <div>
                <strong>48 hrs</strong>
                <span>priority dispatch</span>
            </div>
        </div>
        <img
            class="hero-image"
            src="https://images.unsplash.com/photo-1491553895911-0055eca6402d?auto=format&fit=crop&w=1800&q=80"
            alt="Naves campaign hero"
        />
    </section>
    """)
