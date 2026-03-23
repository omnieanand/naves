import gradio as gr


def render_header(utility_links, primary_nav):
    utility_targets = {
        "Store Finder": "#footer",
        "Help": "#footer",
        "Orders and Returns": "#trust",
        "Sign Up": "#signup",
        "Log In": "#membership",
    }
    utility_items = "".join(
        f"<a href='{utility_targets.get(item, '#top')}'>{item}</a>"
        for item in utility_links
    )

    gr.HTML(f"""
    <section class="utility-nav">
        <div class="utility-nav__links">{utility_items}</div>
    </section>
    """)

    nav_buttons = {}

    with gr.Row(elem_classes="site-header"):
        nav_buttons["NAVES"] = gr.Button("NAVES", elem_classes="brand-button")

        with gr.Row(elem_classes="main-nav-buttons"):
            for item in primary_nav:
                nav_buttons[item] = gr.Button(item, elem_classes="nav-button")

        with gr.Row(elem_classes="header-tools"):
            search = gr.Textbox(
                placeholder="Search",
                container=False,
                elem_classes="header-search",
                show_label=False,
            )
            gr.HTML("""
            <div class="header-icons">
                <a href="#membership">Profile</a>
                <a href="#product-detail">Wishlist</a>
                <a href="#product-detail">Bag (0)</a>
            </div>
            """)

    return search, nav_buttons
