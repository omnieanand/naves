import gradio as gr


def render_promo():
    gr.HTML("""
    <section class="promo-banner" id="spotlight">
        <div>
            <span class="eyebrow">Editorial Spotlight</span>
            <h2>Design the homepage like a merchandised story, not a pile of sections.</h2>
        </div>
        <div class="promo-banner__aside">
            <p>Feature one campaign, one reason to browse, and one clear route into the catalog. That simplicity makes premium brands feel intentional.</p>
            <a class="btn btn-dark" href="#membership">See Membership Benefits</a>
        </div>
    </section>
    """)
