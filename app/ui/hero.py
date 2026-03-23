# import gradio as gr
#
#
# def render_hero():
#     gr.HTML("""
#     <section class="hero-shell">
#         <img
#             class="hero-image"
#             src="https://images.unsplash.com/photo-1491553895911-0055eca6402d?auto=format&fit=crop&w=1800&q=80"
#             alt="Naves hero campaign"
#         />
#         <div class="hero-overlay">
#             <span class="hero-kicker">New Campaign</span>
#             <h1>Supernova Run</h1>
#             <p>Precision cushioning, sharper traction, and daily speed for athletes who want clean performance.</p>
#             <div class="hero-actions">
#                 <a class="btn btn-light" href="#new">Shop Men</a>
#                 <a class="btn btn-light" href="#new">Shop Women</a>
#             </div>
#         </div>
#     </section>
#     """)
import gradio as gr

css = """
.hero-shell {
    position: relative;
    height: 400px;
    overflow: hidden;
}

.hero-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Your overlay CSS */
.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background: rgba(0, 0, 0, 0.4);
    color: white;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;

    padding: 20px;
}

.hero-kicker {
    font-size: 14px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.hero-actions a {
    margin: 10px;
    padding: 10px 20px;
    background: white;
    color: black;
    text-decoration: none;
    border-radius: 5px;
}
"""

def render_hero():
    return """
    <section class="hero-shell">
        <img
            class="hero-image"
            src="https://images.unsplash.com/photo-1491553895911-0055eca6402d?auto=format&fit=crop&w=1800&q=80"
            alt="Hero image"
        />
        <div class="hero-overlay">
            <span class="hero-kicker">New Campaign</span>
            <h1>Supernova Run</h1>
            <p>Precision cushioning, sharper traction, and daily speed for athletes who want clean performance.</p>
            <div class="hero-actions">
                <a href="#">Shop Men</a>
                <a href="#">Shop Women</a>
            </div>
        </div>
    </section>
    """

with gr.Blocks(css=css) as demo:
    gr.HTML(render_hero())

demo.launch()