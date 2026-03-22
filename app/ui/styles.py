GLOBAL_CSS = """
:root {
    --bg: #f5f1e8;
    --surface: #fffdf8;
    --surface-strong: #ffffff;
    --text: #171717;
    --muted: #6f6a63;
    --line: rgba(23, 23, 23, 0.08);
    --accent: #111111;
    --accent-soft: #d9c7aa;
    --highlight: #b98b52;
    --shadow: 0 24px 70px rgba(23, 23, 23, 0.08);
    --radius-xl: 32px;
    --radius-lg: 24px;
    --radius-md: 18px;
    --radius-sm: 12px;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    background:
        radial-gradient(circle at top left, rgba(185, 139, 82, 0.18), transparent 28%),
        linear-gradient(180deg, #fbf7ef 0%, #f1ece2 100%);
    color: var(--text);
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    transition: background 0.3s ease, color 0.3s ease;
}

.gradio-container {
    max-width: 1320px !important;
    margin: 0 auto !important;
    padding: 0 28px 48px !important;
    background: transparent !important;
}

.site-header {
    position: sticky;
    top: 16px;
    z-index: 50;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin: 10px 0 18px;
    padding: 16px 22px;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: rgba(255, 253, 248, 0.82);
    backdrop-filter: blur(18px);
    box-shadow: 0 18px 40px rgba(23, 23, 23, 0.06);
}

.brand-lockup {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-mark {
    width: 44px;
    height: 44px;
    display: grid;
    place-items: center;
    border-radius: 14px;
    background: var(--accent);
    color: white;
    font-weight: 800;
    letter-spacing: 0.08em;
}

.brand-name {
    font-size: 1rem;
    font-weight: 800;
    letter-spacing: 0.24em;
}

.brand-tagline {
    color: var(--muted);
    font-size: 0.78rem;
}

.main-nav {
    display: flex;
    align-items: center;
    gap: 28px;
}

.main-nav a,
.site-footer a {
    color: var(--text);
    text-decoration: none;
}

.main-nav a {
    position: relative;
    font-size: 0.95rem;
    font-weight: 600;
}

.main-nav a:hover::after {
    width: 100%;
}

.main-nav a::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -6px;
    width: 0;
    height: 2px;
    border-radius: 999px;
    background: var(--accent);
    transition: width 0.2s ease;
}

.header-search {
    min-width: 320px;
    border-radius: 999px !important;
    border: 1px solid var(--line) !important;
    background: rgba(255, 255, 255, 0.8) !important;
    padding: 0 18px !important;
}

.header-search input {
    height: 48px !important;
    font-size: 0.96rem !important;
    background: transparent !important;
}

.utility-bar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
}

.theme-toggle,
.btn,
.product-card button {
    border: none;
    border-radius: 999px;
    cursor: pointer;
    font-weight: 700;
    transition: transform 0.2s ease, opacity 0.2s ease, background 0.2s ease;
}

.theme-toggle:hover,
.btn:hover,
.product-card button:hover {
    transform: translateY(-1px);
    opacity: 0.94;
}

.theme-toggle {
    padding: 10px 16px;
    background: rgba(255, 255, 255, 0.85);
    border: 1px solid var(--line);
}

.campaign-strip {
    position: relative;
    overflow: hidden;
    min-height: 54px;
    margin-bottom: 18px;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: linear-gradient(90deg, #111 0%, #27211b 100%);
    color: white;
}

.campaign-strip__item {
    position: absolute;
    inset: 0;
    display: grid;
    place-items: center;
    opacity: 0;
    transform: translateY(10px);
    transition: opacity 0.35s ease, transform 0.35s ease;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    font-size: 0.82rem;
}

.campaign-strip__item.is-active {
    opacity: 1;
    transform: translateY(0);
}

.hero-shell {
    position: relative;
    min-height: 680px;
    overflow: hidden;
    margin-bottom: 34px;
    padding: 64px;
    border-radius: var(--radius-xl);
    background: linear-gradient(135deg, rgba(17, 17, 17, 0.82), rgba(17, 17, 17, 0.32));
    box-shadow: var(--shadow);
}

.hero-shell::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, rgba(14, 14, 14, 0.76) 0%, rgba(14, 14, 14, 0.28) 45%, transparent 100%);
    z-index: 1;
}

.hero-image {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.hero-copy,
.hero-metrics,
.hero-spotlight {
    position: relative;
    z-index: 2;
}

.hero-copy {
    max-width: 560px;
    color: white;
}

.eyebrow {
    display: inline-flex;
    margin-bottom: 16px;
    color: var(--highlight);
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
}

.hero-copy h1,
.section-heading h2,
.promo-banner h2,
.membership-panel h2 {
    margin: 0;
    line-height: 0.96;
    letter-spacing: -0.04em;
}

.hero-copy h1 {
    font-size: clamp(3rem, 7vw, 5.6rem);
}

.hero-copy p,
.section-heading p,
.promo-banner p,
.membership-panel p,
.site-footer p,
.product-rating,
.category-card p {
    color: rgba(255, 255, 255, 0.84);
    font-size: 1rem;
    line-height: 1.7;
}

.hero-actions {
    display: flex;
    gap: 14px;
    margin-top: 30px;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 48px;
    padding: 0 22px;
    text-decoration: none;
}

.btn-light {
    background: white;
    color: #111;
}

.btn-ghost {
    border: 1px solid rgba(255, 255, 255, 0.32);
    color: white;
    background: rgba(255, 255, 255, 0.08);
}

.btn-dark {
    background: #111;
    color: white;
}

.hero-metrics {
    position: absolute;
    left: 64px;
    bottom: 46px;
    display: flex;
    gap: 18px;
}

.hero-metrics div,
.hero-spotlight {
    border: 1px solid rgba(255, 255, 255, 0.16);
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
}

.hero-metrics div {
    min-width: 150px;
    padding: 18px;
    border-radius: 20px;
    color: white;
}

.hero-metrics strong {
    display: block;
    margin-bottom: 6px;
    font-size: 1.4rem;
}

.hero-metrics span {
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.72);
}

.hero-spotlight {
    position: absolute;
    right: 46px;
    bottom: 46px;
    max-width: 280px;
    padding: 24px;
    border-radius: 24px;
    color: white;
}

.hero-spotlight span,
.product-card__meta,
.membership-tier {
    display: inline-block;
    margin-bottom: 10px;
    color: var(--highlight);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.78rem;
    font-weight: 700;
}

.hero-spotlight h3 {
    margin: 0 0 10px;
    font-size: 1.5rem;
}

.hero-spotlight p {
    margin: 0;
    color: rgba(255, 255, 255, 0.74);
}

.section-block {
    margin: 40px 0;
}

.section-heading {
    max-width: 760px;
    margin-bottom: 22px;
}

.section-heading.split {
    max-width: 100%;
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 24px;
    align-items: end;
}

.section-heading h2,
.promo-banner h2,
.membership-panel h2 {
    font-size: clamp(2rem, 4vw, 3.4rem);
    color: var(--text);
}

.section-heading p,
.category-card p {
    color: var(--muted);
}

.category-grid,
.products-grid {
    display: grid;
    gap: 22px;
}

.category-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}

.products-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}

.category-card,
.product-card,
.membership-panel,
.promo-banner,
.site-footer {
    background: rgba(255, 253, 248, 0.88);
    border: 1px solid rgba(23, 23, 23, 0.06);
    box-shadow: var(--shadow);
}

.category-card,
.product-card {
    overflow: hidden;
    border-radius: var(--radius-lg);
}

.category-card img,
.product-card img {
    width: 100%;
    display: block;
    object-fit: cover;
}

.category-card img {
    height: 320px;
}

.category-card__body {
    padding: 24px;
}

.category-card__body span {
    display: inline-flex;
    margin-bottom: 10px;
    color: var(--highlight);
    font-size: 0.82rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.14em;
}

.category-card__body h3,
.product-card h3 {
    margin: 0 0 10px;
    font-size: 1.5rem;
}

.product-card {
    transition: transform 0.28s ease, box-shadow 0.28s ease;
}

.product-card:hover,
.category-card:hover {
    transform: translateY(-6px);
}

.product-card__image-wrap {
    position: relative;
}

.product-card__image-wrap img {
    height: 410px;
}

.product-badge {
    position: absolute;
    left: 18px;
    top: 18px;
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.92);
    color: #111;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.product-card__body {
    padding: 22px;
}

.product-card__meta {
    margin-bottom: 10px;
    color: var(--muted);
}

.product-rating {
    color: var(--muted);
}

.product-card__footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    margin-top: 18px;
}

.product-card__footer strong {
    font-size: 1.22rem;
}

.product-card button {
    min-height: 42px;
    padding: 0 18px;
    background: #111;
    color: white;
}

.promo-banner,
.membership-panel {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 30px;
    padding: 36px;
    border-radius: var(--radius-xl);
}

.promo-banner__aside,
.membership-panel__card {
    padding: 26px;
    border-radius: var(--radius-lg);
    background: linear-gradient(180deg, rgba(17, 17, 17, 0.04), rgba(17, 17, 17, 0.08));
}

.promo-banner p,
.membership-panel p {
    color: var(--muted);
}

.membership-benefits {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 22px;
}

.membership-benefits span {
    padding: 10px 14px;
    border-radius: 999px;
    border: 1px solid var(--line);
    background: rgba(255, 255, 255, 0.72);
    font-weight: 600;
}

.membership-panel__card strong {
    display: block;
    margin-bottom: 12px;
    font-size: 1.3rem;
    line-height: 1.35;
}

.site-footer {
    display: grid;
    grid-template-columns: 1.4fr 1fr 1fr 1fr;
    gap: 24px;
    margin-top: 42px;
    padding: 30px;
    border-radius: var(--radius-xl) var(--radius-xl) 0 0;
}

.site-footer h4 {
    margin: 0 0 12px;
}

.site-footer a {
    display: block;
    margin-bottom: 10px;
    color: var(--muted);
}

.footer-bar {
    margin-bottom: 12px;
    padding: 18px 24px;
    border-top: 1px solid var(--line);
    color: var(--muted);
    text-align: center;
    font-size: 0.92rem;
}

.filter-dropdown {
    margin: 8px 0 18px;
}

.filter-dropdown .wrap,
.filter-dropdown input {
    border-radius: 18px !important;
}

.gr-gallery,
.gr-box,
.gr-panel {
    border-radius: var(--radius-lg) !important;
}

body.dark {
    --bg: #111214;
    --surface: #16181b;
    --surface-strong: #1b1e22;
    --text: #f3efe8;
    --muted: #b9b0a4;
    --line: rgba(255, 255, 255, 0.1);
    --accent: #f3efe8;
    --accent-soft: #25292f;
    background:
        radial-gradient(circle at top left, rgba(185, 139, 82, 0.2), transparent 28%),
        linear-gradient(180deg, #151617 0%, #0f1011 100%);
}

body.dark .gradio-container,
body.dark .category-card,
body.dark .product-card,
body.dark .membership-panel,
body.dark .promo-banner,
body.dark .site-footer,
body.dark .header-search,
body.dark .theme-toggle {
    background: rgba(22, 24, 27, 0.88) !important;
    color: var(--text) !important;
    border-color: var(--line) !important;
}

body.dark .section-heading h2,
body.dark .promo-banner h2,
body.dark .membership-panel h2,
body.dark .category-card__body h3,
body.dark .product-card h3,
body.dark .brand-name,
body.dark .main-nav a,
body.dark .site-footer a,
body.dark .site-footer h4,
body.dark .product-card__footer strong {
    color: var(--text) !important;
}

body.dark .section-heading p,
body.dark .category-card p,
body.dark .promo-banner p,
body.dark .membership-panel p,
body.dark .product-rating,
body.dark .brand-tagline,
body.dark .site-footer p,
body.dark .site-footer a,
body.dark .footer-bar,
body.dark .product-card__meta {
    color: var(--muted) !important;
}

body.dark .product-badge,
body.dark .membership-benefits span {
    background: #23272d;
    color: var(--text);
}

@media (max-width: 1100px) {
    .site-header,
    .section-heading.split,
    .promo-banner,
    .membership-panel,
    .site-footer {
        grid-template-columns: 1fr;
    }

    .site-header {
        border-radius: 28px;
    }

    .main-nav {
        flex-wrap: wrap;
        gap: 16px;
    }

    .header-search {
        min-width: 100%;
    }

    .category-grid,
    .products-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .hero-shell {
        min-height: 760px;
        padding: 34px;
    }

    .hero-metrics,
    .hero-spotlight {
        position: relative;
        left: auto;
        right: auto;
        bottom: auto;
        margin-top: 24px;
    }

    .hero-metrics {
        flex-wrap: wrap;
    }
}

@media (max-width: 720px) {
    .gradio-container {
        padding: 0 14px 32px !important;
    }

    .site-header {
        top: 8px;
        padding: 16px;
    }

    .brand-lockup {
        width: 100%;
    }

    .main-nav {
        justify-content: flex-start;
    }

    .campaign-strip {
        min-height: 68px;
        border-radius: 28px;
    }

    .campaign-strip__item {
        padding: 0 18px;
        text-align: center;
        line-height: 1.5;
    }

    .hero-shell {
        min-height: 640px;
        padding: 26px;
    }

    .hero-copy h1 {
        font-size: 2.7rem;
    }

    .hero-actions,
    .hero-metrics,
    .membership-benefits {
        flex-direction: column;
    }

    .category-grid,
    .products-grid {
        grid-template-columns: 1fr;
    }

    .category-card img,
    .product-card__image-wrap img {
        height: 300px;
    }

    .promo-banner,
    .membership-panel,
    .site-footer {
        padding: 22px;
    }
}
"""
