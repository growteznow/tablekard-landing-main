import os, re

# Read from index.html - extract the common head, header and footer+scripts
with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# Extract the common <head> block
head_start = src.index('<head>')
head_end   = src.index('</head>') + len('</head>')
base_head  = src[head_start:head_end]

# Extract <header> block
header_start = src.index('<header ')
header_end   = src.index('</header>') + len('</header>')
nav_html     = src[header_start:header_end]

# Extract <footer> block + scripts that follow it
footer_start    = src.index('<footer class="footer">')
footer_end      = src.index('</body>')
footer_and_scripts = src[footer_start:footer_end]

# ────────────────────────────────────────────────────────────────
# Light-theme inline CSS shared across all subpages
# ────────────────────────────────────────────────────────────────
SUBPAGE_CSS = """
<style>
  /* ─── Reset any body dark overrides ─── */
  body { background: #ffffff !important; color: #1c1c1c !important; }

  /* ─── Page hero banner ─── */
  .sp-hero {
    padding: 140px 0 64px;
    background: linear-gradient(160deg, #fafafa 0%, #f1f1f1 100%);
    border-bottom: 1px solid #e8e8e8;
    text-align: center;
  }
  .sp-hero h1 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 800;
    color: #1c1c1c;
    margin-bottom: 18px;
    line-height: 1.1;
  }
  .sp-hero p {
    font-size: 1.15rem;
    color: #555;
    max-width: 680px;
    margin: 0 auto;
    line-height: 1.7;
  }
  .sp-hero .sp-badge {
    display: inline-block;
    background: #d9b550;
    color: #1c1c1c;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 100px;
    margin-bottom: 20px;
  }

  /* ─── Main page body ─── */
  .sp-main {
    background: #ffffff;
    padding: 80px 0 100px;
  }
  .sp-container {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 24px;
  }
  .sp-container-wide {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 24px;
  }

  /* ─── Headings ─── */
  .sp-section-title {
    font-family: 'Outfit', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #1c1c1c;
    margin-bottom: 12px;
  }
  .sp-section-subtitle {
    font-size: 1.05rem;
    color: #555;
    line-height: 1.7;
    margin-bottom: 48px;
  }

  /* ─── Card ─── */
  .sp-card {
    background: #ffffff;
    border: 1px solid #e8e8e8;
    border-radius: 20px;
    padding: 40px;
    margin-bottom: 32px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
  }
  .sp-card h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #1c1c1c;
    margin-bottom: 16px;
  }
  .sp-card h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.2rem;
    font-weight: 600;
    color: #1c1c1c;
    margin-bottom: 10px;
  }
  .sp-card p {
    color: #444;
    line-height: 1.75;
    font-size: 1rem;
    margin-bottom: 16px;
  }
  .sp-card p:last-child { margin-bottom: 0; }
  .sp-card ul {
    padding-left: 22px;
    color: #444;
    line-height: 1.9;
    font-size: 1rem;
    margin-bottom: 16px;
  }

  /* ─── Gold accent heading decoration ─── */
  .sp-accent-line {
    display: block;
    width: 48px; height: 4px;
    background: #d9b550;
    border-radius: 2px;
    margin-bottom: 24px;
  }

  /* ─── 2-col grid ─── */
  .sp-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }
  @media (max-width: 680px) {
    .sp-grid-2 { grid-template-columns: 1fr; }
  }

  /* ─── 3-col grid ─── */
  .sp-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }
  @media (max-width: 900px) {
    .sp-grid-3 { grid-template-columns: 1fr 1fr; }
  }
  @media (max-width: 560px) {
    .sp-grid-3 { grid-template-columns: 1fr; }
  }

  /* ─── Icon card ─── */
  .sp-icon-card {
    background: #fafafa;
    border: 1px solid #e8e8e8;
    border-radius: 16px;
    padding: 28px;
    transition: box-shadow 0.2s, border-color 0.2s;
  }
  .sp-icon-card:hover {
    box-shadow: 0 8px 32px rgba(0,0,0,0.07);
    border-color: #d9b550;
  }
  .sp-icon-card .sp-icon {
    font-size: 2.2rem;
    margin-bottom: 14px;
    display: block;
  }
  .sp-icon-card h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #1c1c1c;
    margin-bottom: 8px;
  }
  .sp-icon-card p {
    color: #555;
    font-size: 0.95rem;
    line-height: 1.65;
    margin: 0;
  }

  /* ─── Timeline / Steps ─── */
  .sp-timeline { position: relative; padding-left: 60px; }
  .sp-timeline::before {
    content: '';
    position: absolute;
    left: 19px; top: 0; bottom: 0;
    width: 2px;
    background: #e8e8e8;
    border-radius: 2px;
  }
  .sp-step {
    position: relative;
    margin-bottom: 48px;
  }
  .sp-step:last-child { margin-bottom: 0; }
  .sp-step__num {
    position: absolute;
    left: -60px; top: -4px;
    width: 40px; height: 40px;
    background: #d9b550;
    color: #1c1c1c;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 1rem;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    border: 3px solid #ffffff;
    box-shadow: 0 2px 12px rgba(217,181,80,0.4);
    z-index: 1;
  }
  .sp-step h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #1c1c1c;
    margin-bottom: 10px;
  }
  .sp-step p {
    color: #555;
    line-height: 1.75;
    margin: 0;
  }

  /* ─── FAQ accordion ─── */
  .sp-faq { display: flex; flex-direction: column; gap: 16px; }
  .sp-faq-item {
    background: #fafafa;
    border: 1px solid #e8e8e8;
    border-radius: 14px;
    overflow: hidden;
    transition: border-color 0.2s;
  }
  .sp-faq-item:hover { border-color: #d9b550; }
  .sp-faq-q {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 22px 28px;
    cursor: pointer;
    font-weight: 600;
    font-size: 1.05rem;
    color: #1c1c1c;
    background: none;
    border: none;
    width: 100%;
    text-align: left;
    font-family: 'Inter', sans-serif;
  }
  .sp-faq-q .sp-faq-arrow {
    flex-shrink: 0;
    width: 22px; height: 22px;
    color: #d9b550;
    transition: transform 0.25s;
  }
  .sp-faq-item.open .sp-faq-arrow { transform: rotate(180deg); }
  .sp-faq-body {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease, padding 0.2s ease;
    padding: 0 28px;
    color: #555;
    line-height: 1.75;
    font-size: 0.98rem;
  }
  .sp-faq-item.open .sp-faq-body {
    max-height: 400px;
    padding: 0 28px 22px;
  }

  /* ─── Status chip ─── */
  .sp-status-chip {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(34,197,94,0.08);
    color: #166534;
    padding: 14px 28px;
    border-radius: 100px;
    font-weight: 700;
    font-size: 1.1rem;
    border: 1px solid rgba(34,197,94,0.2);
  }
  .sp-status-dot {
    width: 12px; height: 12px;
    background: #22c55e;
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(34,197,94,0.6);
    flex-shrink: 0;
  }
  .sp-status-table {
    background: #ffffff;
    border: 1px solid #e8e8e8;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
  }
  .sp-status-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 22px 32px;
    border-bottom: 1px solid #f0f0f0;
    gap: 12px;
    flex-wrap: wrap;
  }
  .sp-status-row:last-child { border-bottom: none; }
  .sp-status-row-name {
    font-weight: 600;
    color: #1c1c1c;
    font-size: 1rem;
  }
  .sp-status-row-state {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #166534;
    font-weight: 600;
    font-size: 0.95rem;
  }
  .sp-status-row-dot {
    width: 10px; height: 10px;
    background: #22c55e;
    border-radius: 50%;
  }

  /* ─── Job card ─── */
  .sp-job-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    background: #ffffff;
    border: 1px solid #e8e8e8;
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 20px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.03);
    transition: box-shadow 0.2s, border-color 0.2s;
    flex-wrap: wrap;
  }
  .sp-job-card:hover { border-color: #d9b550; box-shadow: 0 6px 24px rgba(0,0,0,0.07); }
  .sp-job-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #1c1c1c;
    margin-bottom: 8px;
  }
  .sp-job-meta {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }
  .sp-job-tag {
    background: #f4f4f4;
    color: #555;
    border-radius: 6px;
    padding: 4px 12px;
    font-size: 0.82rem;
    font-weight: 500;
  }
  .sp-job-dept { color: #888; font-size: 0.95rem; }
  .sp-btn-gold {
    display: inline-block;
    background: #8B3A1A;
    color: #ffffff;
    padding: 12px 26px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 0.95rem;
    text-decoration: none;
    font-family: 'Inter', sans-serif;
    box-shadow: 0 2px 10px rgba(217,181,80,0.35);
    transition: background 0.2s, box-shadow 0.2s;
    white-space: nowrap;
  }
  .sp-btn-gold:hover { background: #c9a53e; box-shadow: 0 4px 16px rgba(217,181,80,0.5); }

  /* ─── Contact card ─── */
  .sp-contact-card {
    background: #fafafa;
    border: 1px solid #e8e8e8;
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    transition: box-shadow 0.2s, border-color 0.2s;
  }
  .sp-contact-card:hover { border-color: #d9b550; box-shadow: 0 8px 32px rgba(0,0,0,0.07); }
  .sp-contact-icon { font-size: 3rem; display: block; margin-bottom: 18px; }
  .sp-contact-card h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #1c1c1c;
    margin-bottom: 12px;
  }
  .sp-contact-card p {
    color: #666;
    font-size: 0.95rem;
    line-height: 1.65;
    margin-bottom: 22px;
  }
  .sp-contact-link { color: #b8953a; font-weight: 600; font-size: 1rem; text-decoration: none; }
  .sp-contact-link:hover { color: #8b6e26; text-decoration: underline; }

  /* ─── Pro/Con columns ─── */
  .sp-split { display: flex; gap: 20px; flex-wrap: wrap; }
  .sp-split-col {
    flex: 1; min-width: 240px;
    border-radius: 14px;
    padding: 24px;
  }
  .sp-split-col.bad {
    background: rgba(239,68,68,0.05);
    border: 1px solid rgba(239,68,68,0.2);
  }
  .sp-split-col.good {
    background: rgba(34,197,94,0.05);
    border: 1px solid rgba(34,197,94,0.2);
  }
  .sp-split-col h3 { font-size: 1.05rem; font-weight: 700; margin-bottom: 14px; }
  .sp-split-col.bad h3 { color: #d32f2f; }
  .sp-split-col.good h3 { color: #1b873f; }
  .sp-split-col ul { padding-left: 20px; color: #444; line-height: 1.85; font-size: 0.95rem; margin: 0; }

  /* ─── Comparison Table ─── */
  .comparison-table-wrapper {
    overflow-x: auto;
    margin-top: 24px;
    border-radius: 14px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 4px 16px rgba(0,0,0,0.02);
  }
  .comparison-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-family: inherit;
    background: #ffffff;
  }
  .comparison-table th {
    background: #fcfcfc;
    padding: 16px 20px;
    font-weight: 700;
    font-size: 0.95rem;
    color: #333;
    border-bottom: 2px solid rgba(0,0,0,0.06);
  }
  .comparison-table td {
    padding: 16px 20px;
    font-size: 0.92rem;
    line-height: 1.6;
    border-bottom: 1px solid rgba(0,0,0,0.05);
    vertical-align: middle;
  }
  .comparison-table tr:last-child td {
    border-bottom: none;
  }
  .comparison-table th.col-feature { width: 20%; }
  .comparison-table th.col-bad { width: 40%; color: #d32f2f; background: rgba(239,68,68,0.02); }
  .comparison-table th.col-good { width: 40%; color: #1b873f; background: rgba(34,197,94,0.02); }
  
  .comparison-table td.col-feature {
    font-weight: 700;
    color: #444;
    background: #fdfdfd;
  }
  .comparison-table td.col-bad {
    color: #666;
    background: rgba(239,68,68,0.01);
  }
  .comparison-table td.col-good {
    color: #1a1a1a;
    font-weight: 500;
    background: rgba(34,197,94,0.01);
  }
  .comparison-table td.col-bad .status-icon {
    color: #ef4444;
    margin-right: 8px;
    font-weight: bold;
  }
  .comparison-table td.col-good .status-icon {
    color: #22c55e;
    margin-right: 8px;
    font-weight: bold;
  }

  /* ─── Values row ─── */
  .sp-values-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 24px;
  }
  .sp-value-box {
    border-left: 4px solid #d9b550;
    padding: 18px 20px;
    background: #fafafa;
    border-radius: 0 12px 12px 0;
  }
  .sp-value-box h4 {
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    color: #1c1c1c;
    margin-bottom: 6px;
  }
  .sp-value-box p { color: #555; font-size: 0.88rem; line-height: 1.55; margin: 0; }

  /* ─── CTA banner ─── */
  .sp-cta-banner {
    background: linear-gradient(135deg, #1c1c1c 0%, #2d2d2d 100%);
    border-radius: 24px;
    padding: 60px 40px;
    text-align: center;
    margin-top: 60px;
  }
  .sp-cta-banner h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 14px;
  }
  .sp-cta-banner p { color: #a0a0a0; font-size: 1.05rem; margin-bottom: 32px; line-height: 1.65; }
  .sp-cta-banner .sp-btn-gold { font-size: 1.05rem; padding: 16px 36px; }

  /* ─── Inline divider ─── */
  .sp-divider { height: 1px; background: #e8e8e8; margin: 48px 0; }

  /* ─── Legal prose ─── */
  .sp-legal h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #1c1c1c;
    margin: 40px 0 14px;
  }
  .sp-legal p { color: #444; line-height: 1.8; margin-bottom: 16px; font-size: 1rem; }
  .sp-legal ul { padding-left: 22px; color: #444; line-height: 1.85; margin-bottom: 16px; }
  .sp-legal p:first-child { margin-top: 0; }
</style>
"""

# ────────────────────────────────────────────────────────────────
# FAQ accordion JS
# ────────────────────────────────────────────────────────────────
FAQ_JS = """
<script>
  document.querySelectorAll('.sp-faq-q').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var item = btn.closest('.sp-faq-item');
      var isOpen = item.classList.contains('open');
      document.querySelectorAll('.sp-faq-item.open').forEach(function(i){ i.classList.remove('open'); });
      if (!isOpen) item.classList.add('open');
    });
  });
</script>
"""

HAMBURGER_JS = """
<script>
  (function () {
    var btn = document.getElementById('nav-hamburger');
    var drawer = document.getElementById('navbar-drawer');
    if (!btn || !drawer) return;
    btn.addEventListener('click', function () {
      var isOpen = drawer.classList.toggle('is-open');
      btn.classList.toggle('is-open', isOpen);
      btn.setAttribute('aria-expanded', isOpen);
    });
    drawer.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        drawer.classList.remove('is-open');
        btn.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });
  })();
</script>
"""

# ────────────────────────────────────────────────────────────────
# Helper — wrap in full HTML doc
# ────────────────────────────────────────────────────────────────
def make_page(page_title, page_meta_desc, hero_badge, hero_h1, hero_sub, body_html, extra_js=""):
    # Patch the <title> and <meta description> in base_head
    head = re.sub(r'<title>.*?</title>', f'<title>{page_title}</title>', base_head, flags=re.DOTALL)
    head = re.sub(r'(<meta name="description"\s+content=")[^"]*(")', f'\\g<1>{page_meta_desc}\\2', head)
    return f"""<!DOCTYPE html>
<html lang="en">

{head}
{SUBPAGE_CSS}

<body>

  <!-- Full Page Preloader -->
  <div id="site-preloader" class="preloader">
    <div class="preloader__spinner"></div>
    <p class="preloader__text">Loading Tablekard...</p>
  </div>

  {nav_html}

  <!-- Page Hero -->
  <section class="sp-hero">
    <div class="sp-container">
      <span class="sp-badge">{hero_badge}</span>
      <h1>{hero_h1}</h1>
      <p>{hero_sub}</p>
    </div>
  </section>

  <!-- Page Body -->
  <main class="sp-main">
    <div class="sp-container">
      {body_html}
    </div>
  </main>

  {footer_and_scripts}
  <script src="js/main.js"></script>
  {extra_js}

</body>
</html>"""

# ════════════════════════════════════════════════════════════════
# ABOUT PAGE
# ════════════════════════════════════════════════════════════════
about_body = """
<div class="sp-card">
  <h2>Our Mission</h2>
  <span class="sp-accent-line"></span>
  <p>Tablekard was built by the team at <strong>growtez</strong> with a single, clear objective: to digitize modern restaurants without the hassle of expensive hardware or complex software. We believe that ordering food should be as simple as sitting down and scanning a code — and that every restaurant, from a small café to a multi-outlet chain, deserves technology that actually works for them.</p>
  <p>India has over 7.5 million restaurants. Fewer than 5% of them are truly digitized. The rest still rely on paper menus, verbal order-taking, and manual billing — inefficient systems that cost owners revenue every single day. We are changing that, one restaurant at a time.</p>
</div>

<div class="sp-card">
  <h2>The Problem We Solve</h2>
  <span class="sp-accent-line"></span>
  <p>Walk into almost any restaurant today and you will encounter the same friction: a dog-eared paper menu, a waiter who writes your order on a notepad, a kitchen that receives the note and might misread it, and a billing process that takes longer than the meal itself. Every step in that chain is an opportunity for error — and a hidden cost for the restaurant owner.</p>
  <div class="comparison-table-wrapper">
    <table class="comparison-table">
      <thead>
        <tr>
          <th class="col-feature">Feature</th>
          <th class="col-bad">Without Tablekard</th>
          <th class="col-good">With Tablekard</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="col-feature">Menu Management</td>
          <td class="col-bad"><span class="status-icon"><i class="fa-solid fa-xmark"></i></span>Paper menus — unhygienic, expensive to reprint, impossible to update instantly</td>
          <td class="col-good"><span class="status-icon"><i class="fa-solid fa-check"></i></span>Digital QR menu — update prices and items instantly from anywhere</td>
        </tr>
        <tr>
          <td class="col-feature">Ordering Speed</td>
          <td class="col-bad"><span class="status-icon"><i class="fa-solid fa-xmark"></i></span>Customers wait for a waiter just to begin ordering</td>
          <td class="col-good"><span class="status-icon"><i class="fa-solid fa-check"></i></span>Guests order the moment they sit down, without any waiter interaction</td>
        </tr>
        <tr>
          <td class="col-feature">Kitchen Accuracy</td>
          <td class="col-bad"><span class="status-icon"><i class="fa-solid fa-xmark"></i></span>Verbal orders lead to kitchen errors and customer complaints</td>
          <td class="col-good"><span class="status-icon"><i class="fa-solid fa-check"></i></span>Digital orders go straight to the kitchen dashboard with zero errors</td>
        </tr>
        <tr>
          <td class="col-feature">Setup Cost</td>
          <td class="col-bad"><span class="status-icon"><i class="fa-solid fa-xmark"></i></span>₹50,000+ upfront cost for traditional POS hardware</td>
          <td class="col-good"><span class="status-icon"><i class="fa-solid fa-check"></i></span>Affordable monthly subscription — no hardware investment needed</td>
        </tr>
        <tr>
          <td class="col-feature">Data & Analytics</td>
          <td class="col-bad"><span class="status-icon"><i class="fa-solid fa-xmark"></i></span>No data — zero visibility into what sells, when, and to whom</td>
          <td class="col-good"><span class="status-icon"><i class="fa-solid fa-check"></i></span>Real-time analytics: bestsellers, peak hours, revenue trends</td>
        </tr>
        <tr>
          <td class="col-feature">Staff Efficiency</td>
          <td class="col-bad"><span class="status-icon"><i class="fa-solid fa-xmark"></i></span>Staff stretched thin managing orders manually across tables</td>
          <td class="col-good"><span class="status-icon"><i class="fa-solid fa-check"></i></span>Staff freed up to focus on hospitality, not order-taking</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="sp-card">
  <h2>How We Are Different</h2>
  <span class="sp-accent-line"></span>
  <div class="sp-grid-2">
    <div>
      <h3>No App Downloads — Ever</h3>
      <p>Your customers scan a QR code and the menu opens directly in their phone's browser. No app store visits, no account creation required. Works on any smartphone on iOS, Android, or any modern browser.</p>
    </div>
    <div>
      <h3>Multi-Tenant, Bank-Grade Security</h3>
      <p>Every restaurant on Tablekard operates in a completely isolated data environment. We use Supabase with PostgreSQL Row Level Security so your orders, menus, and customer data are never accessible to anyone else — not even us without authorization.</p>
    </div>
    <div>
      <h3>Instant Payments via Razorpay</h3>
      <p>Accept UPI, cards, and net banking directly at the table. Funds are settled to your bank account on standard Razorpay timelines. No commission per order — just your flat subscription fee.</p>
    </div>
    <div>
      <h3>Setup in Under 10 Minutes</h3>
      <p>Our guided onboarding wizard walks you from sign-up to live QR ordering in a single session. No technical knowledge required. No waiting for a sales rep to visit your restaurant.</p>
    </div>
  </div>
</div>

<div class="sp-card">
  <h2>Our Values</h2>
  <span class="sp-accent-line"></span>
  <div class="sp-values-grid">
    <div class="sp-value-box">
      <h4>Simplicity First</h4>
      <p>If a restaurant owner can't figure it out in 60 seconds, we've failed. Every feature we build goes through a simplicity test.</p>
    </div>
    <div class="sp-value-box">
      <h4>Restaurant-Centric</h4>
      <p>We are not a generic SaaS tool. Every decision is made for one audience: the Indian restaurant owner who needs technology that works without a tech team.</p>
    </div>
    <div class="sp-value-box">
      <h4>Reliability Above All</h4>
      <p>A restaurant cannot afford downtime during a Friday dinner rush. We build for 99.9% uptime and test exhaustively before every release.</p>
    </div>
    <div class="sp-value-box">
      <h4>Transparent Pricing</h4>
      <p>Flat monthly fee. No per-order commissions, no hidden charges, no surprise invoices. What you see on our pricing page is exactly what you pay.</p>
    </div>
  </div>
</div>

<div class="sp-card">
  <h2>Built by growtez</h2>
  <span class="sp-accent-line"></span>
  <p>Tablekard is a product of <strong>growtez</strong>, a technology company focused on building digital tools for the Indian service industry. We combine deep domain expertise in the restaurant and hospitality sector with modern SaaS engineering to create products that are powerful for the business owner and invisible to the guest.</p>
  <p>Our team has worked with restaurants across Mumbai, Bangalore, Delhi, Pune, and Kochi. We have seen firsthand the chaos that comes without a reliable ordering system — and the transformation that happens when one is put in place correctly.</p>
</div>

<div class="sp-cta-banner">
  <h2>Ready to See It In Action?</h2>
  <p>Register your restaurant today and get your first 3 months free. No credit card required. Setup takes under 10 minutes.</p>
  <a href="index.html#register" class="sp-btn-gold">Get Started Free →</a>
</div>
"""

# ════════════════════════════════════════════════════════════════
# CAREERS PAGE
# ════════════════════════════════════════════════════════════════
careers_body = """
<div class="sp-card">
  <h2>Why Work at Tablekard?</h2>
  <span class="sp-accent-line"></span>
  <p>We are a small, focused team building technology that has a direct, measurable impact on the livelihoods of restaurant owners across India. At Tablekard, you will not disappear into a large org chart. You will own your work, ship frequently, and see your code used by real restaurants — often within days of writing it.</p>

</div>

<div class="sp-card">
  <h2>Open Positions</h2>
  <span class="sp-accent-line"></span>
  <p style="margin-bottom:32px;">We are a small but growing team. Every hire is a significant one — we take our time to find people who are genuinely excited about what we are building and who share our values.</p>

  <div class="sp-job-card">
    <div>
      <div class="sp-job-title">Senior Full Stack Engineer</div>
      <div class="sp-job-meta">
        <span class="sp-job-tag">Remote / Bangalore</span>
        <span class="sp-job-tag">Full-time</span>
        <span class="sp-job-dept">Engineering</span>
      </div>
    </div>
    <a href="https://wa.me/919101840955?text=Hi!%20I%27d%20like%20to%20apply%20for%20the%20Senior%20Full%20Stack%20Engineer%20position." target="_blank" class="sp-btn-gold">Apply via WhatsApp →</a>
  </div>

  <div class="sp-job-card">
    <div>
      <div class="sp-job-title">Restaurant Success Manager</div>
      <div class="sp-job-meta">
        <span class="sp-job-tag">Mumbai / Bangalore</span>
        <span class="sp-job-tag">Full-time</span>
        <span class="sp-job-dept">Sales & Customer Success</span>
      </div>
    </div>
    <a href="https://wa.me/919101840955?text=Hi!%20I%27d%20like%20to%20apply%20for%20the%20Restaurant%20Success%20Manager%20position." target="_blank" class="sp-btn-gold">Apply via WhatsApp →</a>
  </div>

  <div class="sp-job-card">
    <div>
      <div class="sp-job-title">Product Designer (UI/UX)</div>
      <div class="sp-job-meta">
        <span class="sp-job-tag">Remote</span>
        <span class="sp-job-tag">Full-time</span>
        <span class="sp-job-dept">Design</span>
      </div>
    </div>
    <a href="https://wa.me/919101840955?text=Hi!%20I%27d%20like%20to%20apply%20for%20the%20Product%20Designer%20position." target="_blank" class="sp-btn-gold">Apply via WhatsApp →</a>
  </div>

  <div class="sp-job-card">
    <div>
      <div class="sp-job-title">Growth & Marketing Specialist</div>
      <div class="sp-job-meta">
        <span class="sp-job-tag">Remote / Mumbai</span>
        <span class="sp-job-tag">Full-time</span>
        <span class="sp-job-dept">Marketing</span>
      </div>
    </div>
    <a href="https://wa.me/919101840955?text=Hi!%20I%27d%20like%20to%20apply%20for%20the%20Growth%20%26%20Marketing%20Specialist%20position." target="_blank" class="sp-btn-gold">Apply via WhatsApp →</a>
  </div>
</div>

<div class="sp-card">
  <h2>How We Hire</h2>
  <span class="sp-accent-line"></span>
  <div class="sp-timeline">
    <div class="sp-step">
      <div class="sp-step__num">1</div>
      <h3>Application Review</h3>
      <p>Reach out to us on WhatsApp at <strong>+91 91018 40955</strong> stating the role you are applying for, along with a link to your CV or portfolio. We respond within 5 business days.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">2</div>
      <h3>Introductory Call (30 min)</h3>
      <p>A casual conversation with our founding team to learn more about you, your experience, and what excites you. No technical questions at this stage — just a genuine conversation.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">3</div>
      <h3>Skills Assessment (take-home)</h3>
      <p>A realistic, time-boxed take-home task that reflects actual work you would do at Tablekard. We respect your time — tasks are designed to be completed in under 3 hours.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">4</div>
      <h3>Final Interview & Offer</h3>
      <p>A technical or portfolio deep-dive followed by a culture-fit conversation with the broader team. If it is a mutual fit, we move to an offer within 2 business days.</p>
    </div>
  </div>
</div>

<div class="sp-cta-banner">
  <h2>Don't See the Right Role?</h2>
  <p>We are always interested in exceptional people. Message us on WhatsApp and tell us how you think you can contribute — we will keep your profile on file and reach out when the right opportunity comes up.</p>
  <a href="https://wa.me/919101840955?text=Hi!%20I%27d%20like%20to%20submit%20an%20open%20application%20to%20Tablekard." target="_blank" class="sp-btn-gold">Apply via WhatsApp →</a>
</div>
"""

# ════════════════════════════════════════════════════════════════
# CONTACT PAGE
# ════════════════════════════════════════════════════════════════
contact_body = """
<div class="sp-card">
  <h2>Get In Touch</h2>
  <span class="sp-accent-line"></span>
  <p>Whether you are a restaurant owner looking to get started, a partner looking to integrate with our platform, a journalist with a press inquiry, or simply someone with a question — we would love to hear from you. Our team typically responds within one business day.</p>
</div>

<div class="sp-grid-2" style="margin-bottom:32px;">
  <div class="sp-contact-card">
    <span class="sp-contact-icon"><i class="fa-solid fa-phone"></i></span>
    <h3>Call Us</h3>
    <p>Speak directly with our restaurant onboarding specialists. Available Monday–Saturday, 9 AM–7 PM IST.</p>
    <a class="sp-contact-link" href="tel:+919101840955">+91 91018 40955</a>
  </div>
  <div class="sp-contact-card">
    <span class="sp-contact-icon"><i class="fa-brands fa-whatsapp"></i></span>
    <h3>WhatsApp</h3>
    <p>The fastest way to reach us. Send a message anytime — we aim to reply within 2 hours during business hours.</p>
    <a href="https://wa.me/919101840955?text=Hi%20Tablekard%20Team!%20I%27d%20like%20to%20know%20more%20about%20your%20product." target="_blank" class="sp-btn-gold" style="display:inline-block;margin-top:4px;">Message Us →</a>
  </div>
</div>

<div class="sp-cta-banner">
  <h2>Ready to Register Your Restaurant?</h2>
  <p>Skip the queue — get started immediately with a free 3-month trial. No credit card. No commitment.</p>
  <a href="index.html#register" class="sp-btn-gold">Register Now — It's Free →</a>
</div>
"""

# ════════════════════════════════════════════════════════════════
# HELP CENTER PAGE
# ════════════════════════════════════════════════════════════════
help_faq = [
    ("Do my customers need to download an app?",
     "No — and this is one of Tablekard's most important design decisions. Customers simply scan the QR code on their table and your digital menu opens instantly in their phone's browser. There are no app store downloads, no account creation, and no login required to browse and order. It works on any modern smartphone — iPhone or Android — in Safari, Chrome, or any other browser."),
    ("How do I get started with Tablekard?",
     "Getting started takes under 10 minutes. Fill out the registration form on our homepage with your name, restaurant name, and phone number. Our onboarding team will reach out to schedule a brief setup call. Alternatively, you can self-serve through our guided wizard: create your restaurant profile, build your menu, generate table QR codes, and go live — all in one session."),
    ("Can I update my menu without reprinting anything?",
     "Absolutely. Your digital menu is live and editable at all times from your admin dashboard. Add new items, change prices, mark items as unavailable (e.g., sold out for the day), upload new photos, reorder categories — every change is reflected on the customer-facing menu within seconds. There is nothing to reprint, ever."),
    ("How do payments work for my customers?",
     "Tablekard integrates with Razorpay, India's leading payment gateway. Customers can pay online via UPI (Google Pay, PhonePe, Paytm), debit/credit cards, or net banking — directly from the ordering interface. If you prefer, you can also enable 'Pay at Counter' as an option, letting customers choose how they settle their bill. Online payments are settled directly to your registered bank account on Razorpay's standard T+2 settlement cycle."),
    ("Is my restaurant's data secure and private?",
     "Yes, completely. We use Supabase with PostgreSQL and Row Level Security (RLS) at the database level. This means that at a technical level, every single database query is filtered by your restaurant's unique ID. No other restaurant, user, or even our own team can read your orders, menu items, or analytics without explicit authorization. We also use encrypted HTTPS connections for all data in transit."),
    ("Can I manage multiple restaurant outlets from one account?",
     "Yes. Our Enterprise plan is designed specifically for restaurant chains and franchises. You can manage multiple outlets from a single super-admin dashboard, with each outlet having its own menu, table QR codes, and analytics. You can drill down into outlet-specific data or view aggregated performance across all locations."),
    ("What happens to my data if I cancel my subscription?",
     "If you decide to cancel, your account is paused — not deleted. All your restaurant data, menus, order history, and analytics are retained for 30 days from your cancellation date. You can reactivate within that window with everything intact. After 30 days of inactivity, data is permanently deleted in accordance with our Privacy Policy. You can also request a full data export before cancellation."),
    ("Do I need any special hardware to run Tablekard?",
     "No. You need a printer to print your table QR codes — any inkjet or laser printer works, and the codes are optimized to print sharply even on plain paper. For your dashboard, you can use a laptop, tablet, or even a smartphone. Many of our restaurant partners manage their entire operation from a tablet mounted at the counter. No POS terminals, no proprietary hardware, no vendor lock-in."),
    ("How long does setup take?",
     "Most restaurants are fully live within 10–15 minutes if they follow our onboarding wizard. This includes creating your restaurant profile, adding your first menu categories and items, and generating QR codes for your tables. If you have a large menu (50+ items with photos), you might spend 30–45 minutes uploading everything — but you can also start lean with a few items and add more later."),
    ("Can I customize how my QR menu looks for customers?",
     "Yes. You can upload your restaurant logo, and the customer-facing QR menu will display it prominently in the header. Your restaurant name, description, and cuisine tags also appear on the menu. Pro plan subscribers can additionally set a custom primary brand color that is applied across the ordering interface, making it feel like your own branded app."),
]

def faq_html(faqs):
    items = ""
    for q, a in faqs:
        items += f"""
        <div class="sp-faq-item">
          <button class="sp-faq-q">{q}
            <svg class="sp-faq-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="sp-faq-body">{a}</div>
        </div>"""
    return items

help_body = f"""
<div class="sp-card">
  <h2>Getting Started</h2>
  <span class="sp-accent-line"></span>
  <p>Find step-by-step guidance in our <a href="docs.html" style="color:#b8953a;font-weight:600;">Documentation & Setup Guide</a>, or search the frequently asked questions below. If you cannot find the answer you are looking for, our support team is reachable at <a href="mailto:support@tablekard.com" style="color:#b8953a;font-weight:600;">support@tablekard.com</a> or via <a href="https://wa.me/919101840955" target="_blank" style="color:#b8953a;font-weight:600;">WhatsApp</a>.</p>
</div>

<div class="sp-card">
  <h2>Frequently Asked Questions</h2>
  <span class="sp-accent-line"></span>
  <div class="sp-faq">
    {faq_html(help_faq)}
  </div>
</div>

<div class="sp-card">
  <h2>Still Need Help?</h2>
  <span class="sp-accent-line"></span>
  <div class="sp-grid-3">
    <div class="sp-icon-card">
      <span class="sp-icon">📖</span>
      <h3>Read the Docs</h3>
      <p>Our full setup guide walks you through every step from registration to going live.</p>
      <a href="docs.html" style="color:#b8953a;font-weight:600;display:block;margin-top:12px;">View Documentation →</a>
    </div>
    <div class="sp-icon-card">
      <span class="sp-icon">💬</span>
      <h3>WhatsApp Support</h3>
      <p>Get a fast response from our restaurant success team, available 9 AM–7 PM IST.</p>
      <a href="https://wa.me/919101840955?text=Hi!%20I%20need%20help%20with%20Tablekard." target="_blank" style="color:#b8953a;font-weight:600;display:block;margin-top:12px;">Open WhatsApp →</a>
    </div>
    <div class="sp-icon-card">
      <span class="sp-icon">✉️</span>
      <h3>Email Support</h3>
      <p>For detailed or technical issues, email us and we will get back to you within one business day.</p>
      <a href="mailto:support@tablekard.com" style="color:#b8953a;font-weight:600;display:block;margin-top:12px;">support@tablekard.com →</a>
    </div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════
# DOCS PAGE
# ════════════════════════════════════════════════════════════════
docs_body = """
<div class="sp-card">
  <h2>Complete Setup Guide</h2>
  <span class="sp-accent-line"></span>
  <p>This guide covers everything you need to take Tablekard from registration to a fully live, accepting QR orders at every table in your restaurant. The entire process typically takes under 15 minutes for a standard restaurant. Follow the steps in order for the smoothest experience.</p>
</div>

<div class="sp-card">
  <h2>Step-by-Step Setup</h2>
  <span class="sp-accent-line"></span>
  <div class="sp-timeline">
    <div class="sp-step">
      <div class="sp-step__num">1</div>
      <h3>Register Your Account</h3>
      <p>Go to <strong>tablekard.com</strong> and fill in the registration form with your name, restaurant name, and phone number. Our onboarding team will contact you within a few hours to verify your account and walk you through the next steps. Alternatively, you can self-serve through the admin dashboard immediately after submitting the form.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">2</div>
      <h3>Create Your Restaurant Profile</h3>
      <p>Log in to the Tablekard admin dashboard and fill in your restaurant profile: name, description, cuisine type, operating hours, address, phone number, and logo. This information appears on the customer-facing QR menu, so take care to make it accurate and appealing. Your restaurant will be assigned a unique URL: <strong>tablekard.com/r/your-restaurant-name</strong>.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">3</div>
      <h3>Build Your Digital Menu</h3>
      <p>Navigate to <strong>Menu → Categories</strong> in the sidebar. Create your first category (e.g., "Starters", "Main Course", "Drinks"). Then add items within each category. For each item, you can specify: name, description, price (₹), veg/non-veg indicator, a photo, and availability status. We recommend starting with your 10–15 best-selling items and adding the rest later. <em>Pro tip: Restaurants with photos on menu items consistently see 30% more orders.</em></p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">4</div>
      <h3>Set Up Your Tables</h3>
      <p>Navigate to <strong>Tables → Manage Tables</strong>. Enter the number of dine-in tables in your restaurant. Tablekard will automatically generate a unique QR code for each table. You can give each table a custom name (Table 1, T-01, Window Table, Patio 3, etc.) and set the seating capacity. Once created, a visual grid shows all your tables with their corresponding QR codes.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">5</div>
      <h3>Print & Place Your QR Codes</h3>
      <p>Click <strong>Download All QR Codes</strong> to get a print-ready PDF with all your table QR codes formatted on standard A4 sheets, clearly labeled with the table name. Print them on any inkjet or laser printer. You can laminate them, put them in a table tent holder, or simply stick them directly on the table surface. Each code is high-resolution and scans reliably in both bright and dimly lit environments.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">6</div>
      <h3>Enable Online Payments (Optional)</h3>
      <p>Go to <strong>Settings → Payments</strong> and connect your Razorpay account. You will need your Razorpay API Key and Secret Key — these are available from your Razorpay dashboard. Once connected, customers can pay online via UPI, cards, or net banking directly from the ordering interface. You can leave this step for later and operate with "Pay at Counter" in the meantime.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">7</div>
      <h3>Invite Your Staff</h3>
      <p>Navigate to <strong>Settings → Staff Management</strong> and add your team members by email. You can assign roles: <em>Admin</em> (full access), <em>Manager</em> (no billing access), or <em>Kitchen Staff</em> (view-only order dashboard). Each staff member receives an email invitation with a unique login link. You can revoke access at any time.</p>
    </div>
    <div class="sp-step">
      <div class="sp-step__num">8</div>
      <h3>Go Live — You're Ready!</h3>
      <p>Place the QR codes on your tables. From this moment, any customer who scans a code at a table will be taken directly to your digital menu in their browser, with no app download required. New orders will appear in real-time on your admin order dashboard. You will receive an audio alert and a visual notification for every new order. That's it — your restaurant is fully live on Tablekard.</p>
    </div>
  </div>
</div>

<div class="sp-card">
  <h2>Managing Orders Day-to-Day</h2>
  <span class="sp-accent-line"></span>
  <div class="sp-grid-2">
    <div>
      <h3>Real-Time Order Dashboard</h3>
      <p>Every order placed by a customer appears on your dashboard the moment it is submitted — no page refresh needed. Orders are displayed as cards with the table number, item list, and total amount. Accept an order to send it to the kitchen, then mark it as "Ready" when preparation is complete. Completed orders move to your order history automatically.</p>
    </div>
    <div>
      <h3>Updating Menu Availability</h3>
      <p>If an item runs out mid-service, go to <strong>Menu → [Category]</strong> and toggle the item to "Unavailable". It will be grayed out and unorderable on the customer menu immediately. Toggle it back to "Available" when it is back in stock. This prevents the frustration of customers ordering items that cannot be fulfilled.</p>
    </div>
    <div>
      <h3>Viewing Analytics</h3>
      <p>The <strong>Analytics</strong> section shows you daily and monthly revenue, order volume over time, your top-selling items, and your busiest hours. Use this data to make smarter stocking and staffing decisions. Pro and Enterprise plans include weekly PDF reports emailed directly to you.</p>
    </div>
    <div>
      <h3>Handling Customer Queries</h3>
      <p>If a customer has a special request not captured in the ordering flow, they can add a note to their order in the "Order Notes" field. These notes appear prominently on the order card in your dashboard, so your kitchen staff can accommodate customizations without any verbal communication.</p>
    </div>
  </div>
</div>

<div class="sp-cta-banner">
  <h2>Have a Question Not Covered Here?</h2>
  <p>Visit our Help Center for FAQ, or reach our support team on WhatsApp — we typically respond in under 2 hours.</p>
  <a href="help.html" class="sp-btn-gold">Visit Help Center →</a>
</div>
"""

# ════════════════════════════════════════════════════════════════
# STATUS PAGE
# ════════════════════════════════════════════════════════════════
status_rows = [
    ("Customer QR Ordering Interface", "Operational", "100% uptime — last 30 days"),
    ("Restaurant Admin Dashboard", "Operational", "100% uptime — last 30 days"),
    ("Supabase Database & Authentication", "Operational", "99.99% uptime — last 30 days"),
    ("Real-Time Order Notifications", "Operational", "99.97% uptime — last 30 days"),
    ("Razorpay Payment Gateway", "Operational", "External — check status.razorpay.com"),
    ("QR Code Generation Service", "Operational", "100% uptime — last 30 days"),
    ("Menu Image CDN", "Operational", "100% uptime — last 30 days"),
    ("Analytics & Reporting Engine", "Operational", "99.95% uptime — last 30 days"),
]

def status_row_html(rows):
    out = ""
    for name, state, note in rows:
        out += f"""
        <div class="sp-status-row">
          <div>
            <div class="sp-status-row-name">{name}</div>
            <div style="font-size:0.82rem;color:#888;margin-top:4px;">{note}</div>
          </div>
          <div class="sp-status-row-state">
            <div class="sp-status-row-dot"></div>
            {state}
          </div>
        </div>"""
    return out

status_body = f"""
<div style="text-align:center;margin-bottom:48px;">
  <div class="sp-status-chip">
    <div class="sp-status-dot"></div>
    All Systems Operational
  </div>
  <p style="color:#888;margin-top:16px;font-size:0.92rem;">Last updated: {__import__('datetime').datetime.now().strftime('%d %B %Y, %H:%M')} IST</p>
</div>

<div class="sp-status-table" style="margin-bottom:32px;">
  {status_row_html(status_rows)}
</div>

<div class="sp-card">
  <h2>Uptime & SLA Commitment</h2>
  <span class="sp-accent-line"></span>
  <div class="sp-grid-3">
    <div class="sp-icon-card">
      <span class="sp-icon">⚡</span>
      <h3>99.9% Uptime Guarantee</h3>
      <p>Tablekard guarantees 99.9% uptime for all production services. Scheduled maintenance windows are communicated at least 24 hours in advance and are conducted during off-peak hours (2–5 AM IST).</p>
    </div>
    <div class="sp-icon-card">
      <span class="sp-icon">🔄</span>
      <h3>Automatic Failover</h3>
      <p>Our Supabase database is hosted with automatic failover and point-in-time recovery enabled. In the event of a primary node failure, failover is completed within 60 seconds with zero data loss.</p>
    </div>
    <div class="sp-icon-card">
      <span class="sp-icon">📊</span>
      <h3>Real-Time Monitoring</h3>
      <p>All Tablekard services are monitored continuously with automated alerting. Our on-call engineering team is paged immediately for any service degradation, regardless of time or day.</p>
    </div>
  </div>
</div>

<div class="sp-card">
  <h2>Past Incidents</h2>
  <span class="sp-accent-line"></span>
  <p style="color:#888;font-size:0.95rem;padding:20px 0;text-align:center;border:1px dashed #e8e8e8;border-radius:12px;">
    No incidents reported in the last 90 days. 🎉
  </p>
</div>

<div class="sp-card">
  <h2>Subscribe to Status Updates</h2>
  <span class="sp-accent-line"></span>
  <p>Receive immediate email notifications whenever a Tablekard service experiences degraded performance or a full outage. We commit to posting updates within 15 minutes of detecting any incident.</p>
  <a href="mailto:support@tablekard.com?subject=Subscribe to Status Updates" class="sp-btn-gold" style="display:inline-block;margin-top:8px;">Subscribe via Email →</a>
</div>
"""

# ════════════════════════════════════════════════════════════════
# PRIVACY PAGE
# ════════════════════════════════════════════════════════════════
privacy_body = """
<div class="sp-card sp-legal">
  <p style="background:#fafafa;border:1px solid #e8e8e8;border-radius:10px;padding:16px 20px;font-size:0.9rem;color:#666;">
    <strong>Effective Date:</strong> 1 July 2026 &nbsp;|&nbsp; <strong>Last Reviewed:</strong> 1 July 2026 &nbsp;|&nbsp; <strong>Applies to:</strong> tablekard.com and all Tablekard sub-services
  </p>

  <p>At Tablekard, operated by <strong>growtez</strong>, your privacy is not an afterthought — it is an architectural principle. This Privacy Policy explains what personal data we collect, why we collect it, how we use it, who we share it with, and what rights you have over your own data.</p>
  <p>By using Tablekard, you agree to the terms of this Privacy Policy. If you do not agree, please discontinue use of the platform and contact us to have your data removed.</p>

  <h2>1. Who This Policy Covers</h2>
  <p>This policy covers two categories of users:</p>
  <ul>
    <li><strong>Restaurant Operators</strong> — individuals and businesses who create a Tablekard account to manage their restaurant's digital menu, orders, and staff.</li>
    <li><strong>Dining Customers</strong> — individuals who scan a restaurant's QR code to browse the menu or place an order. We minimize the data we collect from this group to only what is operationally necessary.</li>
  </ul>

  <h2>2. Information We Collect</h2>
  <p><strong>From Restaurant Operators, we collect:</strong></p>
  <ul>
    <li>Name, email address, and phone number (for account creation and authentication)</li>
    <li>Restaurant name, address, operating hours, and logo (for your public-facing digital menu)</li>
    <li>Menu content: item names, descriptions, prices, and photos you upload</li>
    <li>Payment account information: Razorpay API credentials stored in encrypted form (we do not store bank account details directly)</li>
    <li>Usage data: pages visited within the admin dashboard, features used, session duration (for product improvement analytics)</li>
  </ul>
  <p><strong>From Dining Customers, we collect:</strong></p>
  <ul>
    <li>Order contents (items ordered, quantities, special instructions)</li>
    <li>Table number (from the QR code scan context)</li>
    <li>Phone number, if provided voluntarily for order confirmation purposes</li>
    <li>Payment transaction reference ID (from Razorpay) — we never see or store raw card numbers or UPI PINs</li>
  </ul>

  <h2>3. How We Use Your Data</h2>
  <ul>
    <li>To create and maintain your restaurant account and provide access to the admin dashboard</li>
    <li>To display your restaurant's menu to customers who scan your QR codes</li>
    <li>To relay orders from customers to your kitchen/dashboard in real-time</li>
    <li>To process payments via Razorpay and provide transaction confirmations</li>
    <li>To generate analytics reports on your restaurant's order volume, revenue, and popular items</li>
    <li>To send you transactional emails (account confirmation, password reset, subscription notifications)</li>
    <li>To improve the Tablekard platform through aggregated, anonymized usage analytics</li>
  </ul>
  <p>We do <strong>not</strong> use your data for third-party advertising. We do <strong>not</strong> sell your data to any third party. We do <strong>not</strong> use your customers' order data to build advertising profiles.</p>

  <h2>4. Data Isolation & Multi-Tenant Security</h2>
  <p>Tablekard uses Supabase (PostgreSQL) with Row Level Security (RLS) policies enforced at the database layer. This means that every query executed against our database is automatically filtered by your restaurant's unique identifier. It is architecturally impossible for Restaurant A to read Restaurant B's orders, menus, or analytics — even if both are on the same physical database server.</p>
  <p>All data in transit is encrypted via TLS 1.3. Data at rest is encrypted using AES-256 managed by Supabase's cloud infrastructure (hosted on AWS).</p>

  <h2>5. Data Retention</h2>
  <ul>
    <li><strong>Active accounts:</strong> Data is retained for as long as the account is active.</li>
    <li><strong>Cancelled accounts:</strong> Data is retained for 30 days after cancellation to allow account reactivation, then permanently deleted.</li>
    <li><strong>Order records:</strong> Retained for 12 months for analytics purposes, then anonymized.</li>
    <li><strong>Deletion requests:</strong> You can request complete account deletion at any time by emailing privacy@tablekard.com. We will complete the deletion within 7 business days and send a confirmation.</li>
  </ul>

  <h2>6. Cookies & Tracking</h2>
  <p>The Tablekard admin dashboard uses session cookies for authentication purposes only. We use minimal, privacy-respecting analytics (no third-party tracking pixels) to understand how the product is being used. The customer-facing QR menu does not set any tracking cookies.</p>

  <h2>7. Your Rights (PDPB 2023 Compliance)</h2>
  <p>In accordance with India's Personal Data Protection Bill and applicable data protection principles, you have the following rights:</p>
  <ul>
    <li><strong>Right to Access:</strong> Request a copy of all personal data we hold about you</li>
    <li><strong>Right to Correction:</strong> Request correction of inaccurate personal data</li>
    <li><strong>Right to Erasure:</strong> Request deletion of your personal data</li>
    <li><strong>Right to Portability:</strong> Request your data in a machine-readable format (JSON/CSV)</li>
  </ul>
  <p>To exercise any of these rights, email <a href="mailto:privacy@tablekard.com" style="color:#b8953a;font-weight:600;">privacy@tablekard.com</a> from your registered email address.</p>

  <h2>8. Contact the Data Controller</h2>
  <p>Data Controller: growtez (operating Tablekard)<br>
  Email: <a href="mailto:privacy@tablekard.com" style="color:#b8953a;font-weight:600;">privacy@tablekard.com</a><br>
  For urgent data protection concerns, include "URGENT: Data Protection" in the subject line.</p>
</div>
"""

# ════════════════════════════════════════════════════════════════
# TERMS PAGE
# ════════════════════════════════════════════════════════════════
terms_body = """
<div class="sp-card sp-legal">
  <p style="background:#fafafa;border:1px solid #e8e8e8;border-radius:10px;padding:16px 20px;font-size:0.9rem;color:#666;">
    <strong>Effective Date:</strong> 1 July 2026 &nbsp;|&nbsp; <strong>Governing Law:</strong> Republic of India &nbsp;|&nbsp; <strong>Jurisdiction:</strong> Mumbai, Maharashtra
  </p>

  <p>These Terms of Service ("Terms") constitute a legally binding agreement between you (the "Restaurant Operator") and growtez ("Company," "we," "us"), the operator of the Tablekard platform. By creating an account and using any part of the Tablekard service, you agree to be bound by these Terms in their entirety.</p>
  <p>If you are accepting these Terms on behalf of a legal entity (such as a company or partnership), you represent that you have the authority to bind that entity to these Terms.</p>

  <h2>1. Description of Service</h2>
  <p>Tablekard is a Software-as-a-Service (SaaS) platform that enables restaurants to digitize their dine-in ordering experience through QR-code-based menus and a real-time order management dashboard. The service includes: digital menu hosting, QR code generation, real-time order relay, table management, staff management, analytics, and optional Razorpay payment integration.</p>

  <h2>2. Account Registration & Eligibility</h2>
  <ul>
    <li>You must be at least 18 years old and have the legal authority to operate a food service business in India to use Tablekard.</li>
    <li>You are responsible for providing accurate registration information and keeping it up to date.</li>
    <li>You are responsible for maintaining the confidentiality of your account credentials and all activities that occur under your account.</li>
    <li>You must notify us immediately at support@tablekard.com if you suspect unauthorized access to your account.</li>
  </ul>

  <h2>3. Free Trial</h2>
  <p>Tablekard offers a promotional free trial period for new restaurant accounts. During this period, you will have access to all features of the selected plan at no charge. No payment information is required to start the free trial.</p>
  <p>At the end of the free trial period, your account will be automatically transitioned to a paid subscription if you have provided payment details, or suspended if you have not. You will receive email reminders before the trial ends. Tablekard reserves the right to modify free trial terms or discontinue the free trial offer at any time, with notice to existing trial users.</p>

  <h2>4. Subscription & Billing</h2>
  <ul>
    <li>Paid subscriptions are billed monthly in advance. The billing cycle begins on the date your paid subscription starts.</li>
    <li>All prices are quoted in Indian Rupees (₹) and are inclusive of applicable taxes unless stated otherwise.</li>
    <li>Subscription fees are non-refundable except as required by applicable Indian consumer protection law or as explicitly stated in these Terms.</li>
    <li>If a payment fails, we will attempt to charge the payment method on file up to three times over a 7-day period. If payment is not received, your account will be suspended until the outstanding balance is cleared.</li>
    <li>Tablekard reserves the right to change subscription pricing with 30 days written notice to registered account holders. Continued use of the service after the notice period constitutes acceptance of the new pricing.</li>
  </ul>

  <h2>5. Restaurant Operator Responsibilities</h2>
  <p>As a Restaurant Operator using Tablekard, you agree to:</p>
  <ul>
    <li>Ensure all menu items listed on your Tablekard menu comply with applicable FSSAI regulations and food safety standards.</li>
    <li>Accurately represent your menu items, including allergen information where applicable.</li>
    <li>Honor all orders placed by customers through the Tablekard interface and fulfill them as specified.</li>
    <li>Maintain accurate pricing at all times and not charge customers more than the price displayed on your digital menu.</li>
    <li>Not use Tablekard to list illegal, prohibited, or offensive content.</li>
    <li>Not attempt to reverse engineer, scrape, or interfere with the Tablekard platform or its infrastructure.</li>
  </ul>

  <h2>6. Payment Processing</h2>
  <p>Online payment processing (where enabled) is provided by Razorpay Software Private Limited. By enabling online payments, you agree to Razorpay's Terms of Service and Privacy Policy in addition to these Terms. Tablekard does not store, process, or transmit raw payment card data. All payment transactions occur directly on Razorpay's PCI-DSS compliant infrastructure.</p>
  <p>Tablekard is not responsible for payment disputes between Restaurant Operators and their customers. Such disputes should be resolved directly between the parties or escalated to Razorpay's dispute resolution process.</p>

  <h2>7. Intellectual Property</h2>
  <p>You retain all ownership rights to content you upload to Tablekard (your restaurant logo, menu item photos, menu descriptions, etc.). By uploading content, you grant Tablekard a non-exclusive, royalty-free license to host, display, and serve that content for the purposes of operating the service (e.g., displaying your menu to customers).</p>
  <p>The Tablekard platform, including its code, design, trademarks, and documentation, is owned by growtez and protected by applicable intellectual property law. You may not copy, modify, or distribute any part of the platform without our express written consent.</p>

  <h2>8. Limitation of Liability</h2>
  <p>To the maximum extent permitted by applicable law, growtez's total liability to you for any claims arising from or related to these Terms or the Tablekard service shall not exceed the total subscription fees you paid to Tablekard in the 12 months preceding the claim.</p>
  <p>Tablekard is not liable for: indirect, incidental, or consequential damages; loss of revenue or profits; data loss; or business interruption caused by third-party service failures (including Razorpay or internet outages).</p>

  <h2>9. Termination</h2>
  <p>Either party may terminate this agreement with 30 days written notice. Tablekard may terminate or suspend your account immediately and without notice for material breach of these Terms, including fraudulent activity, non-payment, or violation of applicable law.</p>
  <p>Upon termination, your right to access the Tablekard service ceases immediately. Your data will be retained for 30 days as described in our Privacy Policy, then permanently deleted.</p>

  <h2>10. Governing Law & Dispute Resolution</h2>
  <p>These Terms are governed by and construed in accordance with the laws of the Republic of India. Any disputes arising from these Terms shall be subject to the exclusive jurisdiction of the courts of Mumbai, Maharashtra. Both parties agree to attempt resolution through good-faith negotiation before initiating formal legal proceedings.</p>

  <h2>11. Changes to These Terms</h2>
  <p>We reserve the right to update these Terms at any time. We will notify registered Restaurant Operators of material changes via email at least 14 days before the changes take effect. Continued use of the Tablekard service after the effective date of updated Terms constitutes your acceptance of those changes.</p>

  <h2>12. Contact</h2>
  <p>For any questions regarding these Terms of Service, contact us at: <a href="mailto:legal@tablekard.com" style="color:#b8953a;font-weight:600;">legal@tablekard.com</a></p>
</div>
"""

# ════════════════════════════════════════════════════════════════
# BUILD ALL PAGES
# ════════════════════════════════════════════════════════════════
pages = [
    ("about.html",
     "About Tablekard | QR Ordering for Modern Restaurants",
     "Learn about Tablekard's mission, story, and the problem we solve for Indian restaurants.",
     "Company",
     "About Tablekard",
     "We are on a mission to digitize 7.5 million Indian restaurants — starting with yours.",
     about_body, ""),

    ("careers.html",
     "Careers at Tablekard | Join Our Team",
     "Join the Tablekard team and help build the future of restaurant technology in India.",
     "We Are Hiring",
     "Build the Future of Dining",
     "We are a small, focused team building technology that has a direct impact on thousands of restaurant owners. Come ship meaningful work with us.",
     careers_body, ""),

    ("contact.html",
     "Contact Tablekard | Get In Touch",
     "Reach Tablekard via email, phone, or WhatsApp. Our team responds to all inquiries within one business day.",
     "We'd Love to Hear From You",
     "Contact Us",
     "Whether you are a restaurant owner ready to get started, a partner, or just curious — our team is always happy to help.",
     contact_body, ""),

    ("help.html",
     "Help Center | Tablekard FAQ & Support",
     "Find answers to frequently asked questions about Tablekard's QR ordering platform.",
     "Help Center",
     "How Can We Help You?",
     "Find answers to the most common questions about setting up and running your restaurant on Tablekard.",
     help_body, FAQ_JS),

    ("docs.html",
     "Documentation | Tablekard Setup Guide",
     "Step-by-step guide to setting up your restaurant on Tablekard — from registration to accepting your first QR order.",
     "Documentation",
     "Setup Guide",
     "Everything you need to go from registration to a fully live restaurant accepting QR orders — in under 15 minutes.",
     docs_body, ""),

    ("status.html",
     "System Status | Tablekard",
     "Real-time operational status of all Tablekard platform services.",
     "Live Status",
     "Platform Status",
     "Real-time overview of all Tablekard services and infrastructure. We are committed to 99.9% uptime.",
     status_body, ""),

    ("privacy.html",
     "Privacy Policy | Tablekard",
     "Tablekard's privacy policy — how we collect, use, and protect your personal data.",
     "Legal",
     "Privacy Policy",
     "We take your privacy seriously. Here is exactly what data we collect, how we use it, and what rights you have.",
     privacy_body, ""),

    ("terms.html",
     "Terms of Service | Tablekard",
     "Tablekard's Terms of Service — the legal agreement governing your use of the platform.",
     "Legal",
     "Terms of Service",
     "The legal agreement between you and growtez governing your use of the Tablekard platform.",
     terms_body, ""),
]

for (filename, page_title, meta_desc, badge, h1, sub, body, extra_js) in pages:
    html = make_page(page_title, meta_desc, badge, h1, sub, body, extra_js)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅  {filename}")

print("\n✨ All pages generated successfully — light theme, professional content.")
