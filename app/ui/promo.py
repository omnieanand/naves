import gradio as gr


def render_promo():
    gr.HTML("""
    <section class="promo-banner">
        <div>
            <span class="eyebrow">Member Week</span>
            <h2>Unlock early access to limited drops and curated offers.</h2>
        </div>
        <div class="promo-banner__aside">
            <p>Members get launch alerts, priority access, and exclusive event invitations.</p>
            <a class="btn btn-dark" href="#membership">Become a Member</a>
        </div>
    </section>
    """)
