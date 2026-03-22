import gradio as gr


def render_filters():
    with gr.Row(elem_classes="filter-bar"):
        category = gr.Dropdown(
            ["All", "Running", "Sneakers", "Football", "Lifestyle"],
            value="All",
            label="Category",
            elem_classes="filter-dropdown",
        )
        badge = gr.Dropdown(
            ["All", "New Arrival", "Best Seller", "Performance", "Icon", "Lightweight", "Limited"],
            value="All",
            label="Collection Tag",
            elem_classes="filter-dropdown",
        )
        sort_by = gr.Dropdown(
            ["Featured", "Newest", "Top Rated", "Price: Low to High", "Price: High to Low"],
            value="Featured",
            label="Sort By",
            elem_classes="filter-dropdown",
        )
        clear = gr.Button("Clear Filters", elem_classes="filter-clear")

    return category, badge, sort_by, clear
