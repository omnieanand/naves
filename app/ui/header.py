import gradio as gr


def render_header():
    with gr.Row(elem_classes="site-header"):
        gr.HTML("""
        <div class="brand-lockup">
            <div class="brand-mark">N</div>
            <div>
                <div class="brand-name">NAVES</div>
                <div class="brand-tagline">Performance and street essentials</div>
            </div>
        </div>
        """)

        gr.HTML("""
        <nav class="main-nav">
            <a href="#new">New In</a>
            <a href="#running">Running</a>
            <a href="#sneakers">Sneakers</a>
            <a href="#spotlight">Spotlight</a>
            <a href="#membership">Membership</a>
        </nav>
        """)

        with gr.Row(elem_classes="header-tools"):
            search = gr.Textbox(
                placeholder="Search shoes, collections, categories...",
                container=False,
                elem_classes="header-search",
                show_label=False,
            )
            gr.HTML("""
            <div class="header-actions">
                <a href="#top">Account</a>
                <a href="#top">Wishlist</a>
                <a href="#top">Bag (0)</a>
            </div>
            """)

    return search
