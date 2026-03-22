import gradio as gr


def render_membership():
    gr.HTML("""
    <section class="membership-panel" id="membership">
        <div class="membership-panel__copy">
            <span class="eyebrow">Membership</span>
            <h2>Join NAVES Club for premium benefits.</h2>
            <p>
                Free delivery thresholds, launch-day notifications, exclusive style edits,
                and members-only pricing on selected collections.
            </p>
            <div class="membership-benefits">
                <span>Priority access</span>
                <span>Members-only offers</span>
                <span>Event invitations</span>
            </div>
        </div>
        <div class="membership-panel__card">
            <div class="membership-tier">Club Black</div>
            <strong>Designed for customers who come back for every drop.</strong>
            <p>Earn points on every order and unlock elevated rewards as you shop.</p>
            <a class="btn btn-dark" href="#top">Join Now</a>
        </div>
    </section>
    """)
