import gradio as gr


def render_footer():
    gr.HTML("""
    <footer class="site-footer">
        <div>
            <div class="brand-name">NAVES</div>
            <p>Premium footwear and apparel for movement, sport, and everyday style.</p>
        </div>
        <div>
            <h4>Support</h4>
            <a href="#top">Help</a>
            <a href="#top">Shipping</a>
            <a href="#top">Returns</a>
        </div>
        <div>
            <h4>Company</h4>
            <a href="#top">About</a>
            <a href="#top">Careers</a>
            <a href="#top">Stores</a>
        </div>
        <div>
            <h4>Legal</h4>
            <a href="#top">Privacy</a>
            <a href="#top">Terms</a>
            <a href="#top">Cookies</a>
        </div>
    </footer>
    <div class="footer-bar">© 2026 NAVES. Crafted for a more premium storefront experience.</div>
    """)
