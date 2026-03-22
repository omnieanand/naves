import gradio as gr

import gradio as gr

def render_theme_toggle():
    gr.HTML("""
    <div style="text-align:right; padding:10px;">
        <button onclick="toggleDarkMode()" 
            style="padding:8px 16px; cursor:pointer;">
            🌙 Toggle Dark Mode
        </button>
    </div>
    """)
