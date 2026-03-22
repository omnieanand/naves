import gradio as gr

def render_header():
    with gr.Row(elem_classes="header"):
        gr.Markdown("## NAVES")
        with gr.Row(elem_classes="nav"):
            gr.Markdown("## 🚀 NAVES CI/CD LIVE SUCCESS")
            gr.Markdown("## 🚀 FINAL DEPLOY SUCCESS")
            gr.Button("Home")
            gr.Button("Men")
            gr.Button("Women")
            gr.Button("Kids")
            gr.Button("Sale")

        search = gr.Textbox(placeholder="Search products...")

    return search