import gradio as gr


def render_hot_stories(stories):
    cards = []
    for story in stories:
        cards.append(f"""
        <article class="story-card">
            <img src="{story['img']}" alt="{story['title']}" />
            <div class="story-card__body">
                <h3>{story['title']}</h3>
                <p>{story['copy']}</p>
                <a href="#new">{story['cta']}</a>
            </div>
        </article>
        """)

    gr.HTML(f"""
    <section class="section-block" id="hot">
        <h2 class="section-title">WHAT'S HOT</h2>
        <div class="story-grid">
            {''.join(cards)}
        </div>
    </section>
    """)


def render_style_shortcuts(items):
    links = "".join(f"<a href='#running'>{item}</a>" for item in items)
    gr.HTML(f"""
    <section class="section-block" id="style">
        <h2 class="section-title">Your Style. Your Sneakers.</h2>
        <div class="shortcut-row">
            {links}
        </div>
    </section>
    """)


def render_sport_tiles(items):
    tiles = []
    for item in items:
        tiles.append(f"""
        <article class="sport-tile">
            <img src="{item['img']}" alt="{item['name']}" />
            <span>{item['name']}</span>
        </article>
        """)

    gr.HTML(f"""
    <section class="section-block" id="sports">
        <div class="section-heading">
            <span class="eyebrow">Sports & Lifestyle</span>
            <h2>Select your sport, find your gear, and get in the game.</h2>
        </div>
        <div class="sport-grid">
            {''.join(tiles)}
        </div>
    </section>
    """)


def render_link_groups(groups):
    cols = []
    for group in groups:
        items = "".join(f"<a href='#top'>{item}</a>" for item in group["items"])
        cols.append(f"""
        <div class="link-group">
            <h3>{group['title']}</h3>
            {items}
        </div>
        """)

    gr.HTML(f"""
    <section class="section-block" id="links">
        <div class="link-groups">
            {''.join(cols)}
        </div>
    </section>
    """)


def render_signup_banner():
    gr.HTML("""
    <section class="signup-banner" id="signup">
        <div>
            <h2>Join NAVES and get 10% off</h2>
            <p>Sign up for free to unlock launch alerts, early access, and member-only offers.</p>
        </div>
        <a class="btn btn-dark" href="#membership">Sign Up For Free</a>
    </section>
    """)
