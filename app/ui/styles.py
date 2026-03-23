GLOBAL_CSS = """
:root {
    --bg: #ffffff;
    --surface: #ffffff;
    --surface-soft: #f7f7f7;
    --text: #111111;
    --muted: #666666;
    --line: #e5e5e5;
    --line-strong: #cfcfcf;
    --accent: #111111;
    --shadow: 0 16px 36px rgba(17, 17, 17, 0.06);
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    background: #ffffff !important;
    color: var(--text);
    font-family: Arial, Helvetica, sans-serif;
    transition: background 0.2s ease, color 0.2s ease;
}

.gradio-container {
    max-width: 1440px !important;
    margin: 0 auto !important;
    padding: 0 20px 48px !important;
    background: #ffffff !important;
}

.utility-nav {
    display: flex;
    justify-content: flex-end;
    padding: 10px 0 4px;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

.utility-nav__links {
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
}

.utility-nav a,
.header-icons a,
.story-card a,
.link-group a,
.site-footer a {
    color: var(--text);
    text-decoration: none;
}

.site-header {
    align-items: center;
    justify-content: space-between;
    gap: 18px;
    padding: 14px 0 18px;
    border-bottom: 1px solid var(--line);
    background: #ffffff;
}

.brand-button,
.nav-button {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
    color: var(--text) !important;
    min-height: auto !important;
    padding: 0 !important;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

.brand-button {
    font-size: 2rem !important;
    font-weight: 900 !important;
}

.main-nav-buttons {
    align-items: center;
    gap: 22px;
    flex-wrap: wrap;
}

.nav-button {
    font-size: 0.95rem !important;
    font-weight: 800 !important;
}

.header-tools {
    align-items: center;
    gap: 10px;
}

.header-search {
    min-width: 160px;
    border: 1px solid var(--line) !important;
    border-radius: 0 !important;
    background: white !important;
    padding: 0 10px !important;
}

.header-search input {
    height: 42px !important;
    background: transparent !important;
    font-size: 0.95rem !important;
}

.header-icons {
    display: flex;
    gap: 14px;
    font-size: 0.85rem;
    text-transform: uppercase;
}

.utility-bar {
    display: flex;
    justify-content: flex-end;
    margin: 10px 0;
}

.theme-toggle,
.btn,
.product-card button,
.detail-actions button,
.filter-clear {
    border: 1px solid var(--text);
    border-radius: 0;
    background: white;
    color: var(--text);
    cursor: pointer;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    transition: background 0.2s ease, color 0.2s ease, transform 0.2s ease;
}

.theme-toggle:hover,
.btn:hover,
.product-card button:hover,
.detail-actions button:hover,
.filter-clear:hover {
    transform: translateY(-1px);
}

.theme-toggle,
.btn,
.filter-clear {
    min-height: 44px;
    padding: 0 16px;
}

.hero-shell {
    position: relative;
    overflow: hidden;
    min-height: 640px;
    margin-bottom: 44px;
    background: #ffffff;
    border: 1px solid var(--line);
}

.hero-image {
    width: 100%;
    height: 640px;
    object-fit: cover;
    display: block;
    filter: brightness(1.08) saturate(1.02);
}

.hero-overlay {
    position: absolute;
    left: 48px;
    bottom: 48px;
    max-width: 520px;
    color: var(--text);
    background: rgba(255, 255, 255, 0.96);
    padding: 24px 28px;
    border: 1px solid rgba(17, 17, 17, 0.08);
}

.hero-kicker,
.eyebrow {
    display: inline-flex;
    margin-bottom: 12px;
    font-size: 0.8rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.hero-overlay h1,
.section-heading h2,
.section-title,
.signup-banner h2,
.membership-panel h2,
.product-detail h2 {
    margin: 0;
    font-size: clamp(2.4rem, 5vw, 4.4rem);
    line-height: 0.95;
    letter-spacing: -0.03em;
    text-transform: uppercase;
}

.hero-overlay p,
.section-heading p,
.story-card p,
.category-card p,
.product-description,
.product-rating,
.trust-card p,
.signup-banner p,
.membership-panel p,
.product-detail p,
.site-footer p {
    margin: 10px 0 0;
    color: var(--muted);
    line-height: 1.6;
}

.hero-overlay p {
    color: var(--muted);
    max-width: 420px;
}

.hero-actions {
    display: flex;
    gap: 12px;
    margin-top: 24px;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
}

.btn-light {
    background: white;
    color: var(--text);
    border-color: var(--text);
}

.btn-dark {
    background: var(--text);
    color: white;
}

.section-block {
    margin: 44px 0;
}

.catalog-heading {
    margin: 28px 0 18px;
}

.catalog-heading h2 {
    margin: 0;
    font-size: clamp(2rem, 4vw, 3.4rem);
    line-height: 0.95;
    letter-spacing: -0.03em;
    text-transform: uppercase;
}

.catalog-heading p {
    margin: 10px 0 0;
    color: var(--muted);
    line-height: 1.6;
    max-width: 760px;
}

.section-title {
    font-size: 1.8rem;
    margin-bottom: 18px;
}

.section-heading {
    max-width: 840px;
    margin-bottom: 22px;
}

.section-heading.split {
    max-width: 100%;
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 24px;
    align-items: end;
}

.story-grid,
.category-grid,
.products-grid,
.trust-grid,
.sport-grid,
.link-groups,
.site-footer {
    display: grid;
    gap: 20px;
}

.story-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}

.story-card,
.category-card,
.product-card,
.trust-card,
.sport-tile,
.signup-banner,
.membership-panel,
.product-detail {
    background: white;
    border: 1px solid var(--line);
    box-shadow: 0 10px 24px rgba(17, 17, 17, 0.03);
}

.story-card img,
.category-card img,
.product-card img,
.sport-tile img {
    width: 100%;
    display: block;
    object-fit: cover;
}

.story-card img {
    height: 320px;
}

.story-card__body {
    padding: 14px 0 0;
}

.story-card h3,
.category-card__body h3,
.product-card h3,
.link-group h3 {
    margin: 0 0 8px;
    font-size: 1.2rem;
    text-transform: uppercase;
}

.story-card a {
    display: inline-flex;
    margin-top: 12px;
    font-weight: 800;
    text-transform: uppercase;
    border-bottom: 2px solid var(--text);
}

.shortcut-row {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--line);
}

.shortcut-row a {
    color: var(--text);
    font-weight: 800;
    font-size: 1rem;
    text-transform: uppercase;
    text-decoration: none;
}

.category-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}

.category-card img {
    height: 420px;
}

.category-card__body {
    padding: 12px 0 0;
}

.category-card__body span {
    display: inline-flex;
    margin-bottom: 10px;
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--muted);
}

.sport-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
}

.sport-tile {
    position: relative;
    overflow: hidden;
}

.sport-tile img {
    height: 260px;
    filter: brightness(1.02);
}

.sport-tile span {
    position: absolute;
    left: 18px;
    bottom: 18px;
    color: var(--text);
    font-size: 1.1rem;
    font-weight: 900;
    text-transform: uppercase;
    background: rgba(255, 255, 255, 0.92);
    padding: 8px 12px;
}

.link-groups {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    padding: 24px 0;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
}

.link-group a {
    display: block;
    margin-bottom: 8px;
    color: var(--muted);
}

.filter-bar {
    align-items: end;
    gap: 12px;
}

.filter-dropdown {
    margin: 0 0 18px;
}

.filter-dropdown .wrap,
.filter-dropdown input,
.detail-selector .wrap,
.detail-selector input {
    border-radius: 0 !important;
}

.products-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}

.product-card {
    border: 1px solid var(--line);
}

.product-card__image-wrap {
    position: relative;
}

.product-card__image-wrap img {
    height: 400px;
}

.product-badge {
    position: absolute;
    left: 12px;
    top: 12px;
    padding: 6px 10px;
    background: white;
    color: var(--text);
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
}

.product-card__body {
    padding: 16px;
}

.product-card__meta {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 8px;
    font-size: 0.72rem;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 800;
}

.product-description {
    min-height: 64px;
}

.product-card__footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-top: 14px;
}

.product-price-stack {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.product-card__footer strong,
.detail-price-row strong {
    font-size: 1.3rem;
}

.product-original-price,
.detail-original-price {
    font-size: 0.9rem;
    color: var(--muted);
    text-decoration: line-through;
}

.trust-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
}

.trust-card {
    padding: 18px;
    border: 1px solid var(--line);
}

.trust-card strong {
    display: block;
    margin-bottom: 10px;
    text-transform: uppercase;
}

.detail-selector {
    margin-bottom: 16px;
}

.product-detail {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 24px;
    padding: 24px;
    border: 1px solid var(--line);
}

.product-detail__hero {
    width: 100%;
    height: 520px;
    object-fit: cover;
}

.product-detail__thumbs {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
    margin-top: 12px;
}

.product-detail__thumbs img {
    width: 100%;
    height: 180px;
    object-fit: cover;
}

.detail-price-row,
.detail-meta,
.detail-chip-row,
.detail-size-row,
.detail-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.detail-price-row,
.detail-meta,
.detail-actions {
    margin-top: 16px;
}

.detail-meta span,
.detail-chip,
.detail-size {
    display: inline-flex;
    align-items: center;
    min-height: 38px;
    padding: 0 12px;
    border: 1px solid var(--line);
    font-size: 0.88rem;
}

.detail-block {
    margin-top: 22px;
}

.detail-block h4 {
    margin: 0 0 10px;
    font-size: 0.9rem;
    text-transform: uppercase;
}

.detail-block ul {
    margin: 0;
    padding-left: 18px;
    color: var(--muted);
    line-height: 1.7;
}

.detail-note {
    margin-top: 18px;
    padding: 14px;
    border: 1px solid var(--line);
}

.detail-actions .secondary {
    background: white;
    color: var(--text);
}

.signup-banner,
.membership-panel {
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 20px;
    padding: 28px;
    border: 1px solid var(--line);
}

.membership-benefits {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 16px;
}

.membership-benefits span {
    display: inline-flex;
    align-items: center;
    min-height: 36px;
    padding: 0 12px;
    border: 1px solid var(--line);
    font-size: 0.86rem;
    text-transform: uppercase;
    font-weight: 700;
}

.membership-tier {
    display: inline-flex;
    margin-bottom: 10px;
    font-size: 0.76rem;
    font-weight: 800;
    text-transform: uppercase;
}

.membership-panel__card {
    padding: 20px;
    border: 1px solid var(--line);
}

.membership-panel__card strong {
    display: block;
    margin-bottom: 10px;
}

.site-footer {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 28px;
    margin-top: 44px;
    padding: 32px 0;
    border-top: 1px solid var(--line);
    background: #ffffff;
}

.footer-group h4 {
    margin: 0 0 12px;
    font-size: 0.9rem;
    text-transform: uppercase;
}

.site-footer a {
    display: block;
    margin-bottom: 8px;
    color: var(--muted);
}

.footer-bar {
    padding: 18px 0;
    border-top: 1px solid var(--line);
    color: var(--muted);
    font-size: 0.9rem;
}

.gr-gallery,
.gr-box,
.gr-panel {
    border-radius: 0 !important;
    background: #ffffff !important;
}

@media (max-width: 1100px) {
    .site-header,
    .section-heading.split,
    .signup-banner,
    .membership-panel,
    .product-detail,
    .site-footer {
        grid-template-columns: 1fr;
    }

    .story-grid,
    .category-grid,
    .products-grid,
    .trust-grid,
    .sport-grid,
    .link-groups {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .header-tools,
    .main-nav-buttons {
        flex-wrap: wrap;
    }

    .header-search {
        min-width: 100%;
    }
}

@media (max-width: 720px) {
    .gradio-container {
        padding: 0 12px 32px !important;
    }

    .hero-image {
        height: 520px;
    }

    .hero-overlay {
        left: 20px;
        right: 20px;
        bottom: 20px;
    }

    .hero-actions,
    .detail-actions,
    .membership-benefits {
        flex-direction: column;
        align-items: stretch;
    }

    .story-grid,
    .category-grid,
    .products-grid,
    .trust-grid,
    .sport-grid,
    .link-groups,
    .product-detail__thumbs {
        grid-template-columns: 1fr;
    }

    .story-card img,
    .category-card img,
    .product-card__image-wrap img,
    .sport-tile img,
    .product-detail__hero,
    .product-detail__thumbs img {
        height: 280px;
    }
}
"""
