import gradio as gr


def render_membership():
    gr.HTML("""
    <section class="membership-panel" id="membership">
        <div class="membership-panel__copy">
            <span class="eyebrow">Membership</span>
            <h2>Join NAVES Club for benefits that actually improve conversion and retention.</h2>
            <p>
                Free delivery thresholds, launch-day notifications, exclusive drops,
                members-only pricing, and loyalty rewards designed to bring customers back.
            </p>
            <div class="membership-benefits">
                <span>Priority access</span>
                <span>Members-only offers</span>
                <span>Event invitations</span>
                <span>Loyalty rewards</span>
            </div>
        </div>
        <div class="membership-panel__card">
            <div class="membership-tier">Club Black</div>
            <strong>Built for customers who return for every launch and expect premium service.</strong>
            <p>Earn points on every order, unlock faster support, and get earlier access to limited releases.</p>
            <a class="btn btn-dark" href="#top">Join Now</a>
        </div>
    </section>
    """)
