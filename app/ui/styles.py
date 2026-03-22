GLOBAL_CSS = """
/* RESET */
body {
    font-family: Arial, sans-serif;
    background: #ffffff;
    color: #000;
    margin: 0;
    transition: all 0.3s ease;
}

/* GRADIO ROOT FIX */
.gradio-container {
    background: #ffffff;
    color: #000;
    transition: all 0.3s ease;
}

/* HEADER */
.header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:15px 40px;
    border-bottom:1px solid #eee;
    position:sticky;
    top:0;
    background:white;
    z-index:1000;
}

/* NAV */
.nav button {
    background:none;
    border:none;
    font-weight:600;
    cursor:pointer;
}

.nav button:hover {
    text-decoration: underline;
}

/* HERO */
.hero-text {
    position:absolute;
    top:30%;
    left:5%;
    color:white;
}

/* PRODUCT CARDS */
.product-card img:hover {
    transform: scale(1.05);
    transition: 0.3s;
}

/* HOVER LIFT */
.product-card:hover {
    transform: translateY(-5px);
    transition: 0.3s;
}

/* BUTTON */
button {
    transition: all 0.3s ease;
}

button:hover {
    opacity: 0.85;
}

/* FADE ANIMATION */
.fade-in {
    animation: fadeIn 1s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* MOBILE */
@media (max-width: 768px) {
    .header {
        flex-direction: column;
    }

    .hero-text h1 {
        font-size: 28px;
    }

    img {
        width: 100%;
    }
}

/* ========================= */
/* 🌙 DARK MODE (FINAL FIX) */
/* ========================= */

/* Apply to whole app */
.dark,
.dark body,
.dark .gradio-container {
    background: #111 !important;
    color: #fff !important;
}

/* Header */
.dark .header {
    background: #111 !important;
    border-bottom: 1px solid #333;
}

/* Buttons */
.dark button {
    background: #222 !important;
    color: #fff !important;
    border: 1px solid #444;
}

/* Inputs */
.dark input,
.dark textarea {
    background: #222 !important;
    color: #fff !important;
    border: 1px solid #444;
}

/* Cards / sections */
.dark .product-card,
.dark .gr-box,
.dark .gr-panel {
    background: #1a1a1a !important;
    color: #fff !important;
}

/* Gallery fix */
.dark .gr-gallery {
    background: #111 !important;
}
"""