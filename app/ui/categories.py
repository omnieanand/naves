import gradio as gr

def render_categories():
    gr.Markdown("## Shop By Category")

    with gr.Row():
        for cat in ["Running", "Sneakers", "Football"]:
            gr.HTML(f"""
            <div style="text-align:center;">
                <img src="https://picsum.photos/300" 
                     style="border-radius:12px;" />
                <h3>{cat}</h3>
            </div>
            """)