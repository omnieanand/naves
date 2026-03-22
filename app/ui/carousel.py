import gradio as gr

def render_carousel():
    gr.HTML("""
    <div class="carousel">
        <img id="carousel-img" src="https://picsum.photos/1400/500?1"/>
    </div>

    <script>
    let images = [
        "https://picsum.photos/1400/500?1",
        "https://picsum.photos/1400/500?2",
        "https://picsum.photos/1400/500?3"
    ];

    let index = 0;

    setInterval(() => {
        index = (index + 1) % images.length;
        document.getElementById("carousel-img").src = images[index];
    }, 3000);
    </script>
    """)