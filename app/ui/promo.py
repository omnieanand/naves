import gradio as gr

def render_promo():
    gr.HTML("""
    <div style="background:black; color:white; padding:40px; text-align:center;">
        <h2>🔥 END OF SEASON SALE</h2>
        <p>UP TO 50% OFF</p>
    </div>
    """)