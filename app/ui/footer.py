import gradio as gr


def render_footer():
    gr.HTML("""
    <footer class="site-footer" id="footer">
        <div class="footer-group">
            <h4>PRODUCTS</h4>
            <a href="#top">Footwear</a>
            <a href="#top">Clothing</a>
            <a href="#top">Accessories</a>
            <a href="#top">New Arrivals</a>
            <a href="#top">Outlet</a>
        </div>
        <div class="footer-group">
            <h4>SPORTS</h4>
            <a href="#top">Running</a>
            <a href="#top">Football</a>
            <a href="#top">Cricket</a>
            <a href="#top">Training</a>
            <a href="#top">Basketball</a>
        </div>
        <div class="footer-group">
            <h4>COLLECTIONS</h4>
            <a href="#top">Supernova Run</a>
            <a href="#top">Metro Classic</a>
            <a href="#top">Forum Edge</a>
            <a href="#top">Naves Club</a>
            <a href="#top">Season Edit</a>
        </div>
        <div class="footer-group">
            <h4>SUPPORT</h4>
            <a href="#top">Help</a>
            <a href="#top">Returns & Exchanges</a>
            <a href="#top">Shipping</a>
            <a href="#top">Order Tracker</a>
            <a href="#top">Store Finder</a>
        </div>
    </footer>
    <div class="footer-bar">© 2026 NAVES. Performance, style, and innovation.</div>
    """)
