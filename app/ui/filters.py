import gradio as gr


def render_filters():
    category = gr.Dropdown(
        ["All", "Running", "Sneakers", "Football", "Lifestyle"],
        value="All",
        label="Filter by Category",
        elem_classes="filter-dropdown",
    )
    return category
