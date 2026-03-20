import gradio as gr

def render_hero():
    gr.Markdown("## 🔥 Welcome to NAVES")
    gr.Image("https://picsum.photos/1200/400", show_label=False)

    with gr.Row():
        gr.Button("Shop Men")
        gr.Button("Shop Women")
        gr.Button("Shop Kids")