import gradio as gr


def render_hero():
    gr.HTML("""
    <div style="position:relative; margin-bottom:40px;">

        <!-- Background Image -->
        <img src="https://picsum.photos/1400/500"
             style="width:100%; height:500px; object-fit:cover; border-radius:12px;" />

        <!-- Overlay -->
        <div style="
            position:absolute;
            top:0;
            left:0;
            width:100%;
            height:100%;
            background:rgba(0,0,0,0.3);
            border-radius:12px;
        "></div>

        <!-- Text Content -->
        <div style="
            position:absolute;
            top:30%;
            left:5%;
            color:white;
        ">
            <h1 style="font-size:52px; font-weight:800; margin-bottom:10px;">
                IMPOSSIBLE IS NOTHING
            </h1>
            <p style="font-size:18px; margin-bottom:20px;">
                Step into NAVES — redefine your performance
            </p>

            <button style="
                padding:12px 28px;
                background:white;
                color:black;
                border:none;
                font-weight:bold;
                cursor:pointer;
                border-radius:5px;
            ">
                SHOP NOW
            </button>
        </div>

    </div>
    """)