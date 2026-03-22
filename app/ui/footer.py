import gradio as gr

def render_footer():
    gr.HTML("""
    <hr>
    <div style="display:flex; justify-content:space-around;">
        <div>Help</div>
        <div>Returns</div>
        <div>Privacy</div>
    </div>
    <p style="text-align:center;">© 2026 NAVES</p>
    """)