import gradio as gr

def render_theme_toggle():
    gr.HTML("""
    <div class="utility-bar">
        <button class="theme-toggle" onclick="toggleDarkMode()">
            Toggle Contrast Mode
        </button>
    </div>
    """)
