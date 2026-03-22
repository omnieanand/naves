GLOBAL_CSS = """
body {
    font-family: Arial, sans-serif;
    background: #fff;
}

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

.nav button {
    background:none;
    border:none;
    font-weight:600;
    cursor:pointer;
}

.nav button:hover {
    text-decoration: underline;
}

.hero-text {
    position:absolute;
    top:30%;
    left:5%;
    color:white;
}

.product-card img:hover {
    transform: scale(1.05);
    transition: 0.3s;
}
"""