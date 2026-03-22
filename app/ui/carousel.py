import gradio as gr


def render_carousel():
    gr.HTML("""
    <section class="campaign-strip">
        <div class="campaign-strip__item">Free shipping over ₹7,500</div>
        <div class="campaign-strip__item">Members get early access to every launch</div>
        <div class="campaign-strip__item">New season styles live now</div>
    </section>

    <script>
    const items = document.querySelectorAll(".campaign-strip__item");
    let activeIndex = 0;

    if (items.length) {
        items[activeIndex].classList.add("is-active");
        setInterval(() => {
            items[activeIndex].classList.remove("is-active");
            activeIndex = (activeIndex + 1) % items.length;
            items[activeIndex].classList.add("is-active");
        }, 2400);
    }
    </script>
    """)
