import gradio as gr

def render_filters():
    category = gr.Dropdown(
        ["All", "Running", "Sneakers", "Football"],
        value="All",
        label="Filter by Category"
    )
    return category