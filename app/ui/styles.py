GLOBAL_CSS = """
:root {
    --bg: #ffffff;
    --bg-soft: #f7f7f4;
    --surface: #ffffff;
    --surface-alt: #faf9f6;
    --text: #111111;
    --muted: #6c6c67;
    --line: #e8e6df;
    --line-strong: #d9d5cb;
    --accent: #111111;
    --accent-soft: #efe8db;
    --highlight: #a67c43;
    --shadow: 0 20px 50px rgba(17, 17, 17, 0.06);
    --radius-xl: 36px;
    --radius-lg: 26px;
    --radius-md: 18px;
    --radius-sm: 12px;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    background:
        radial-gradient(circle at top left, rgba(238, 228, 208, 0.55), transparent 22%),
        linear-gradient(180deg, #ffffff 0%, #fcfbf8 100%);
    color: var(--text);
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    transition: background 0.25s ease, color 0.25s ease;
}

.gradio-container {
    max-width: 1360px !important;
    margin: 0 auto !important;
    padding: 0 28px 56px !important;
    background: transparent !important;
}

.site-header {
    position: sticky;
    top: 16px;
    z-index: 50;
    align-items: center;
    justify-content: space-between;
    gap: 22px;
    margin: 10px 0 16px;
    padding: 16px 22px;
    border: 1px solid rgba(17, 17, 17, 0.06);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(18px);
    box-shadow: 0 12px 40px rgba(17, 17, 17, 0.05);
}

.brand-lockup {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-mark {
    width: 46px;
    height: 46px;
    display: grid;
    place-items: center;
    border-radius: 14px;
    background: #111111;
    color: white;
    font-weight: 800;
    letter-spacing: 0.08em;
}

.brand-name {
    font-size: 0.98rem;
    font-weight: 800;
    letter-spacing: 0.25em;
    color: var(--text);
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
.header-actions a,
.site-footer a {
    text-decoration: none;
}

.main-nav a {
    position: relative;
    color: var(--text);
    font-size: 0.92rem;
    font-weight: 700;
}

.main-nav a::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -6px;
    width: 0;
    height: 2px;
    border-radius: 999px;
    background: var(--text);
    transition: width 0.2s ease;
}

.main-nav a:hover::after {
    width: 100%;
}

.header-tools {
    align-items: center;
    gap: 12px;
}

.header-search {
    min-width: 320px;
    border-radius: 999px !important;
    border: 1px solid var(--line) !important;
    background: var(--surface-alt) !important;
    padding: 0 18px !important;
}

.header-search input {
    height: 48px !important;
    font-size: 0.95rem !important;
    background: transparent !important;
}

.header-actions {
    display: flex;
    align-items: center;
    gap: 10px;
}

.header-actions a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 46px;
    padding: 0 16px;
    border: 1px solid var(--line);
    border-radius: 999px;
    color: var(--text);
    font-size: 0.9rem;
    font-weight: 600;
    background: white;
}

.utility-bar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 12px;
}

.theme-toggle,
.btn,
.product-card button,
.detail-actions button {
    border: none;
    border-radius: 999px;
    cursor: pointer;
    font-weight: 700;
    transition: transform 0.2s ease, opacity 0.2s ease, background 0.2s ease;
}

.theme-toggle:hover,
.btn:hover,
.product-card button:hover,
.detail-actions button:hover {
    transform: translateY(-1px);
    opacity: 0.95;
}

.theme-toggle {
    padding: 10px 16px;
    border: 1px solid var(--line);
    background: white;
    color: var(--text);
}

.campaign-strip {
    position: relative;
    overflow: hidden;
    min-height: 58px;
    margin-bottom: 18px;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: white;
}

.campaign-strip__item {
    position: absolute;
    inset: 0;
    display: grid;
    place-items: center;
    padding: 0 16px;
    opacity: 0;
    transform: translateY(8px);
    transition: opacity 0.35s ease, transform 0.35s ease;
    color: var(--text);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-size: 0.78rem;
    font-weight: 700;
    text-align: center;
}

.campaign-strip__item.is-active {
    opacity: 1;
    transform: translateY(0);
}

.hero-shell {
    position: relative;
    overflow: hidden;
    min-height: 720px;
    margin-bottom: 40px;
    border-radius: var(--radius-xl);
    background: #f8f7f2;
    box-shadow: var(--shadow);
}

.hero-panel {
    position: relative;
    z-index: 2;
    max-width: 620px;
    padding: 64px;
}

.hero-shell::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.82) 42%, rgba(255, 255, 255, 0.1) 68%);
    z-index: 1;
}

.hero-image {
    position: absolute;
    top: 0;
    right: 0;
    width: 68%;
    height: 100%;
    object-fit: cover;
}

.eyebrow {
    display: inline-flex;
    margin-bottom: 16px;
    color: var(--highlight);
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 0.16em;
    text-transform: uppercase;
}

.hero-copy h1,
.section-heading h2,
.promo-banner h2,
.membership-panel h2,
.product-detail h2 {
    margin: 0;
    line-height: 0.95;
    letter-spacing: -0.05em;
}

.hero-copy h1 {
    font-size: clamp(3.2rem, 7vw, 6rem);
    max-width: 520px;
}

.hero-copy p,
.section-heading p,
.promo-banner p,
.membership-panel p,
.product-detail p,
.trust-card p,
.site-footer p,
.product-description,
.product-rating {
    color: var(--muted);
    font-size: 1rem;
    line-height: 1.7;
}

.hero-actions {
    display: flex;
    gap: 12px;
    margin-top: 28px;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 48px;
    padding: 0 22px;
    text-decoration: none;
}

.btn-dark {
    background: #111111;
    color: white;
}

.btn-outline {
    background: rgba(255, 255, 255, 0.82);
    color: var(--text);
    border: 1px solid var(--line);
}

.hero-note-card,
.hero-floating-metrics div {
    background: rgba(255, 255, 255, 0.88);
    border: 1px solid rgba(17, 17, 17, 0.08);
    box-shadow: 0 20px 50px rgba(17, 17, 17, 0.08);
    backdrop-filter: blur(10px);
}

.hero-note-card {
    max-width: 320px;
    margin-top: 28px;
    padding: 22px;
    border-radius: 24px;
}

.hero-note-card h3 {
    margin: 0 0 10px;
    font-size: 1.5rem;
    letter-spacing: -0.03em;
}

.hero-floating-metrics {
    position: absolute;
    left: 64px;
    bottom: 42px;
    z-index: 2;
    display: flex;
    gap: 14px;
}

.hero-floating-metrics div {
    min-width: 155px;
    padding: 18px;
    border-radius: 22px;
}

.hero-floating-metrics strong {
    display: block;
    margin-bottom: 6px;
    font-size: 1.4rem;
}

.hero-floating-metrics span {
    color: var(--muted);
    font-size: 0.88rem;
}

.section-block {
    margin: 48px 0;
}

.section-heading {
    max-width: 760px;
    margin-bottom: 24px;
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
.membership-panel h2,
.product-detail h2 {
    color: var(--text);
    font-size: clamp(2.1rem, 4vw, 3.6rem);
}

.category-grid,
.products-grid,
.trust-grid {
    display: grid;
    gap: 22px;
}

.category-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}

.products-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}

.trust-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
}

.category-card,
.product-card,
.trust-card,
.promo-banner,
.membership-panel,
.product-detail,
.site-footer {
    background: white;
    border: 1px solid rgba(17, 17, 17, 0.06);
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
    height: 340px;
}

.category-card__body {
    padding: 24px;
}

.category-card__body span {
    display: inline-flex;
    margin-bottom: 10px;
    color: var(--highlight);
    text-transform: uppercase;
    letter-spacing: 0.14em;
    font-size: 0.78rem;
    font-weight: 800;
}

.category-card__body h3,
.product-card h3 {
    margin: 0 0 10px;
    font-size: 1.5rem;
    letter-spacing: -0.03em;
}

.category-card p {
    color: var(--muted);
}

.product-card {
    transition: transform 0.28s ease, box-shadow 0.28s ease;
}

.product-card:hover,
.category-card:hover,
.trust-card:hover {
    transform: translateY(-5px);
}

.product-card__image-wrap {
    position: relative;
}

.product-card__image-wrap img {
    height: 420px;
}

.product-badge {
    position: absolute;
    left: 18px;
    top: 18px;
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.96);
    color: #111;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.product-card__body {
    padding: 22px;
}

.product-card__meta {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.73rem;
    font-weight: 800;
}

.product-description {
    min-height: 72px;
    margin: 0 0 8px;
}

.product-card__footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    margin-top: 18px;
}

.product-price-stack {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.product-card__footer strong {
    font-size: 1.2rem;
}

.product-original-price,
.detail-original-price {
    color: var(--muted);
    text-decoration: line-through;
    font-size: 0.9rem;
}

.product-card button,
.detail-actions button {
    min-height: 42px;
    padding: 0 18px;
    background: #111111;
    color: white;
}

.trust-card {
    padding: 22px;
    border-radius: 22px;
}

.trust-card strong {
    display: block;
    margin-bottom: 12px;
    font-size: 1.08rem;
    line-height: 1.4;
}

.detail-selector {
    margin-bottom: 18px;
}

.product-detail {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 26px;
    padding: 26px;
    border-radius: var(--radius-xl);
}

.product-detail__gallery {
    display: grid;
    gap: 16px;
}

.product-detail__hero {
    width: 100%;
    height: 500px;
    object-fit: cover;
    border-radius: 24px;
}

.product-detail__thumbs {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
}

.product-detail__thumbs img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 20px;
}

.product-detail__content {
    padding: 10px 8px;
}

.detail-rating,
.detail-note,
.detail-meta {
    color: var(--muted);
}

.detail-price-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 16px 0;
}

.detail-price-row strong {
    font-size: 1.8rem;
}

.detail-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 18px 0 24px;
}

.detail-meta span,
.detail-chip,
.detail-size {
    display: inline-flex;
    align-items: center;
    min-height: 40px;
    padding: 0 14px;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: var(--surface-alt);
    font-size: 0.92rem;
}

.detail-block {
    margin: 22px 0;
}

.detail-block h4 {
    margin: 0 0 12px;
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}

.detail-chip-row,
.detail-size-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.detail-block ul {
    margin: 0;
    padding-left: 20px;
    color: var(--muted);
    line-height: 1.8;
}

.detail-note {
    padding: 16px 18px;
    border: 1px solid var(--line);
    border-radius: 18px;
    background: var(--surface-alt);
}

.detail-actions {
    display: flex;
    gap: 12px;
    margin-top: 22px;
}

.detail-actions .secondary {
    background: white;
    color: var(--text);
    border: 1px solid var(--line);
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
    border: 1px solid var(--line);
    border-radius: var(--radius-lg);
    background: var(--surface-alt);
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
    background: white;
    font-weight: 700;
}

.membership-tier {
    display: inline-block;
    margin-bottom: 10px;
    color: var(--highlight);
    text-transform: uppercase;
    letter-spacing: 0.14em;
    font-size: 0.78rem;
    font-weight: 800;
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
    margin-top: 46px;
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

.filter-bar {
    align-items: end;
    gap: 14px;
}

.filter-dropdown,
.detail-selector {
    margin: 6px 0 18px;
}

.filter-dropdown .wrap,
.filter-dropdown input,
.detail-selector .wrap,
.detail-selector input {
    border-radius: 18px !important;
}

.filter-clear {
    min-height: 46px !important;
    padding: 0 18px !important;
    border: 1px solid var(--line) !important;
    border-radius: 999px !important;
    background: white !important;
    color: var(--text) !important;
}

.gr-gallery,
.gr-box,
.gr-panel {
    border-radius: var(--radius-lg) !important;
}

body.dark {
    --bg: #101112;
    --bg-soft: #17191c;
    --surface: #17191c;
    --surface-alt: #1d2024;
    --text: #f7f5f0;
    --muted: #b9b1a5;
    --line: rgba(255, 255, 255, 0.1);
    --line-strong: rgba(255, 255, 255, 0.16);
    background: linear-gradient(180deg, #121315 0%, #0d0e10 100%);
}

body.dark .site-header,
body.dark .campaign-strip,
body.dark .category-card,
body.dark .product-card,
body.dark .trust-card,
body.dark .promo-banner,
body.dark .membership-panel,
body.dark .product-detail,
body.dark .site-footer,
body.dark .header-search,
body.dark .theme-toggle,
body.dark .header-actions a,
body.dark .hero-note-card,
body.dark .hero-floating-metrics div,
body.dark .promo-banner__aside,
body.dark .membership-panel__card,
body.dark .detail-note,
body.dark .detail-meta span,
body.dark .detail-chip,
body.dark .detail-size,
body.dark .membership-benefits span {
    background: var(--surface) !important;
    color: var(--text) !important;
    border-color: var(--line) !important;
}

body.dark .section-heading h2,
body.dark .promo-banner h2,
body.dark .membership-panel h2,
body.dark .product-detail h2,
body.dark .category-card__body h3,
body.dark .product-card h3,
body.dark .brand-name,
body.dark .main-nav a,
body.dark .product-card__footer strong,
body.dark .trust-card strong {
    color: var(--text) !important;
}

body.dark .section-heading p,
body.dark .hero-copy p,
body.dark .hero-note-card p,
body.dark .product-description,
body.dark .product-rating,
body.dark .trust-card p,
body.dark .promo-banner p,
body.dark .membership-panel p,
body.dark .detail-rating,
body.dark .detail-note,
body.dark .detail-meta,
body.dark .site-footer p,
body.dark .site-footer a,
body.dark .footer-bar,
body.dark .brand-tagline {
    color: var(--muted) !important;
}

@media (max-width: 1180px) {
    .site-header,
    .section-heading.split,
    .promo-banner,
    .membership-panel,
    .product-detail,
    .site-footer {
        grid-template-columns: 1fr;
    }

    .site-header {
        border-radius: 28px;
    }

    .header-tools,
    .main-nav {
        flex-wrap: wrap;
    }

    .header-search {
        min-width: 100%;
    }

    .category-grid,
    .products-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .trust-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .hero-shell {
        min-height: 780px;
    }

    .hero-panel {
        padding: 38px;
    }

    .hero-image {
        width: 100%;
        opacity: 0.52;
    }

    .hero-shell::after {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.92) 0%, rgba(255, 255, 255, 0.72) 55%, rgba(255, 255, 255, 0.48) 100%);
    }

    .hero-floating-metrics {
        left: 38px;
        bottom: 32px;
        flex-wrap: wrap;
    }
}

@media (max-width: 720px) {
    .gradio-container {
        padding: 0 14px 36px !important;
    }

    .site-header {
        top: 8px;
        padding: 16px;
    }

    .brand-lockup,
    .header-actions,
    .hero-actions,
    .hero-floating-metrics,
    .detail-actions,
    .membership-benefits {
        flex-direction: column;
        align-items: stretch;
    }

    .main-nav {
        justify-content: flex-start;
        gap: 14px;
    }

    .campaign-strip {
        min-height: 72px;
        border-radius: 28px;
    }

    .hero-shell {
        min-height: 760px;
    }

    .hero-panel {
        padding: 24px;
    }

    .hero-copy h1 {
        font-size: 2.8rem;
    }

    .hero-floating-metrics {
        position: relative;
        left: auto;
        bottom: auto;
        padding: 0 24px 24px;
    }

    .category-grid,
    .products-grid,
    .trust-grid,
    .product-detail__thumbs {
        grid-template-columns: 1fr;
    }

    .category-card img,
    .product-card__image-wrap img,
    .product-detail__hero,
    .product-detail__thumbs img {
        height: 300px;
    }

    .promo-banner,
    .membership-panel,
    .product-detail,
    .site-footer {
        padding: 22px;
    }

    .filter-bar {
        gap: 0;
    }
}
"""
