import gradio as gr

def render_membership():
    gr.HTML("""
    <div style="background:#f5f5f5; padding:50px; text-align:center;">
        <h2>JOIN NAVES CLUB</h2>
        <p>Get exclusive deals</p>
        <button style="padding:12px 30px; background:black; color:white;">
            JOIN NOW
        </button>
    </div>
    """)