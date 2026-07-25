# -*- coding: utf-8 -*-
import json, os
M = json.load(open("/home/claude/drift-ia-site/manifest.json"))
OUT = "/home/claude/drift-ia-site"

PHONE="425-478-0327"; EMAIL="jen@drift-ia.com"
ADDR="14526 107th St NE &middot; Lake Stevens, WA 98258"
STAGING_URL="https://www.driftdesignandco.com"

FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com">'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
'<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400;1,6..96,500&family=Archivo:wght@300;400;500;600&display=swap" rel="stylesheet">')

def header(active, mode):
    def a(href,label,key,ext=False):
        cls=' class="active"' if key==active else ''
        tgt=' target="_blank" rel="noopener"' if ext else ''
        arrow=' &nearr;' if ext else ''
        return f'<a href="{href}"{cls}{tgt}>{label}{arrow}</a>'
    return f'''<header class="site-header {mode}">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="mark">Drift</span>
      <span class="sub">Interiors + Architecture</span>
    </a>
    <button class="nav-toggle" onclick="document.querySelector('nav.main').classList.toggle('show')">Menu</button>
    <nav class="main">
      {a("work.html","Select Work","work")}
      {a("plans.html","Plans","plans")}
      {a("journal.html","Journal","journal")}
      {a("services.html","Services","services")}
      {a("about.html","About","about")}
      {a("connect.html","Connect","connect")}
      {a("contact.html","Contact","contact")}
      {a(STAGING_URL,"Home Staging","staging",ext=True)}
    </nav>
  </div>
</header>'''

FOOTER=f'''<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="mark">Drift</div>
        <div class="sub">Interiors + Architecture</div>
        <p style="margin-top:22px;max-width:340px;font-size:14px;color:rgba(255,255,255,.6);">
          An architecture and interior design studio designing intentional residential and multifamily spaces across the Seattle area.</p>
        <div class="footer-social">
          <a data-social="instagram" href="#" target="_blank" rel="noopener" hidden>Instagram</a>
          <a data-social="facebook" href="#" target="_blank" rel="noopener" hidden>Facebook</a>
          <a data-social="pinterest" href="#" target="_blank" rel="noopener" hidden>Pinterest</a>
          <a data-social="houzz" href="#" target="_blank" rel="noopener" hidden>Houzz</a>
          <a data-social="linkedin" href="#" target="_blank" rel="noopener" hidden>LinkedIn</a>
          <a data-social="archipro" href="#" target="_blank" rel="noopener" hidden>ArchiPro</a>
          <a data-social="adpro" href="#" target="_blank" rel="noopener" hidden>AD PRO</a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <a href="work.html">Work</a>
        <a href="upcoming.html">Upcoming Work</a>
        <a href="journal.html">Journal</a>
        <a href="plans.html">Home Plans</a>
        <a href="services.html">Services</a>
        <a href="about.html">The Studio</a>
        <a href="contact.html">Contact</a>
        <a href="{STAGING_URL}" target="_blank" rel="noopener">Home Staging &nearr;</a>
        <a href="{STAGING_URL}/staged-to-live.html" target="_blank" rel="noopener">Staged to Live &nearr;</a>
      </div>
      <div>
        <h4>Studio</h4>
        <a data-cms="phone" href="tel:{PHONE.replace('-','')}">{PHONE}</a>
        <a data-cms="email" href="mailto:{EMAIL}">{EMAIL}</a>
        <a data-cms="address" href="contact.html">{ADDR}</a>
      </div>
    </div>
    <div class="bottom">
      <span>&copy; 2026 Drift Interiors + Architecture</span>
      <span>Lake Stevens &middot; Greater Seattle &middot; Puget Sound</span>
    </div>
  </div>
</footer>'''

SCRIPT='<script src="assets/js/app.js" defer></script>'

SITE_URL="https://www.drift-ia.com"
OG_IMG=SITE_URL+"/assets/img/work/gala/gala-01.jpg"
JSONLD=('<script type="application/ld+json">'
'{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness",'
'"name":"Drift Interiors + Architecture","alternateName":"Drift IA",'
'"description":"Boutique interior design and licensed architecture studio serving the greater Seattle and Puget Sound region.",'
f'"image":"{OG_IMG}","@id":"{SITE_URL}","url":"{SITE_URL}","telephone":"+1-425-478-0327","email":"jen@drift-ia.com",'
'"address":{"@type":"PostalAddress","streetAddress":"14526 107th St NE","addressLocality":"Lake Stevens","addressRegion":"WA","postalCode":"98258","addressCountry":"US"},'
'"areaServed":["Seattle","Bellevue","Kirkland","Sammamish","Snohomish County","King County","Puget Sound"],'
'"knowsAbout":["interior design","residential architecture","kitchen design","bathroom design","multifamily architecture","home remodeling"],'
'"priceRange":"$$$"}'
'</script>')
def page(title,active,mode,body,desc,fn="index.html"):
    canon=f"{SITE_URL}/{fn}"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow">
<meta name="author" content="Drift Interiors + Architecture">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Drift Interiors + Architecture">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{OG_IMG}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMG}">
<meta name="theme-color" content="#26231e">
{JSONLD}
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{header(active,mode)}
{body}
{FOOTER}
{SCRIPT}
<script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
<script>if(window.netlifyIdentity){{netlifyIdentity.on("init",function(u){{if(!u){{netlifyIdentity.on("login",function(){{document.location.href="/admin/";}});}}}});}}</script>
</body>
</html>'''

def first(slug): return M[slug]["images"][0]["full"]
def nth(slug,n): return M[slug]["images"][min(n,len(M[slug]['images'])-1)]["full"]

CROSSLINK=f'''
<section class="crosslink pad-sm">
  <div class="wrap">
    <div class="txt">
      <p class="eyebrow">Also from Drift</p>
      <h3>Selling a home? Meet our staging studio.</h3>
      <p>Drift Staging &amp; Design Studio brings the same eye for space and detail to market-ready staging across the Puget Sound region.</p>
    </div>
    <a class="btn" href="{STAGING_URL}" target="_blank" rel="noopener">Visit Drift Staging &nearr;</a>
  </div>
</section>'''

# ---------------- HOME ----------------
home=f'''
<section class="hero">
  <div class="bg"><img src="{nth("solinsky",1)}" alt="Sycamore Lane living and dining"></div>
  <div class="wrap inner">
    <p class="eyebrow light reveal">Interiors + Architecture &middot; Seattle Area</p>
    <h1 class="reveal">a boutique studio for<br><em>luxurious, livable</em> spaces</h1>
    <p class="lede reveal">Full-service interior design and licensed architecture — thoughtfully designed homes, kitchens, and spaces made for the way you actually live.</p>
    <div class="reveal" style="margin-top:38px;"><a class="tlink light" href="work.html">Explore Our Work</a></div>
  </div>
  <div class="scmark">Drift &middot; Design With Intent</div>
</section>

<section class="statement pad">
  <div class="wrap">
    <p class="reveal" data-cms="statement">&ldquo;We design spaces where good ideas — and good coffee — flow freely: intentional, fluid, and made for the way you actually live.&rdquo;</p>
    <div class="sig reveal">Drift Interiors + Architecture</div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="section-head center reveal">
      <hr class="rule"><p class="eyebrow">Studio Services</p>
      <h2>Architecture &amp; interior design, under one roof</h2>
      <p>A licensed architect&rsquo;s rigor paired with an interior designer&rsquo;s eye — for residential and multifamily projects alike.</p>
    </div>
    <div class="svc-grid reveal">
      <div class="svc-card"><span class="num">01</span><h3>Interior Design</h3><p>Full-house interior design and luxury interiors — space planning, finishes, and furnishings curated into a cohesive whole.</p></div>
      <div class="svc-card"><span class="num">02</span><h3>Architecture</h3><p>Residential and multifamily architecture from a Washington-licensed architect, designed around site, light, and how you live.</p></div>
      <div class="svc-card"><span class="num">03</span><h3>Kitchens &amp; Baths</h3><p>Considered, hard-working renovations — custom kitchens and spa-like baths designed down to the last detail.</p></div>
    </div>
    <div class="center reveal" style="margin-top:46px;"><a class="btn" href="services.html">All Services</a></div>
  </div>
</section>

<section class="split reverse">
  <div class="media"><img src="{first("bowen")}" alt="Custom marble kitchen"></div>
  <div class="body reveal">
    <p class="eyebrow">The Approach</p>
    <h2>Intentional by design</h2>
    <p>Every project begins with how a space will be lived in. From there we shape light, flow, and material into rooms that feel effortless — dynamic where they should be, calm where they need to be.</p>
    <p>The result is design that works as hard as it looks: beautiful, functional, and unmistakably yours.</p>
    <a class="btn" href="about.html" style="margin-top:8px;">Meet the Studio</a>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="section-head center reveal"><hr class="rule"><p class="eyebrow">Selected Work</p><h2>Recent projects</h2></div>
    <div class="trio">
      <figure class="reveal"><img src="{first("slossen")}" alt="Issaquah primary bath"><figcaption>Issaquah Primary Bath</figcaption></figure>
      <figure class="reveal"><img src="{first("haber")}" alt="Haber kitchen"><figcaption>Haber Kitchen</figcaption></figure>
      <figure class="reveal"><img src="{nth('bowen',1)}" alt="Sammamish residence"><figcaption>Sammamish Residence</figcaption></figure>
    </div>
    <div class="center reveal" style="margin-top:48px;"><a class="btn" href="work.html">Explore the Portfolio</a></div>
  </div>
</section>

<section class="cta pad">
  <div class="wrap">
    <p class="eyebrow light reveal">Start Here</p>
    <h2 class="reveal">Have a project in mind?</h2>
    <p class="reveal">Tell us about your space and your goals. We&rsquo;ll help you design it with intent.</p>
    <div class="reveal"><a class="btn light" href="contact.html">Start a Project</a></div>
  </div>
</section>
{CROSSLINK}
'''

# ---------------- WORK ----------------
def tiles(images):
    n=len(images)
    if n==0: return []
    if n==1: return [('half',images[0]),('half',images[0])]
    t=[('big',images[0]),('small',images[1])]
    rest=images[2:]; i=0
    while i < len(rest):
        remain=len(rest)-i
        if remain==1:
            t.append(('full',rest[i])); i+=1
        elif remain==2 or remain==4:
            t.append(('half',rest[i])); t.append(('half',rest[i+1])); i+=2
        else:
            t.append(('third',rest[i])); t.append(('third',rest[i+1])); t.append(('third',rest[i+2])); i+=3
    return t
order=["solinsky","bowen","strauss","gala","ashford","jade","michael-day","slossen","christenson","gig-harbor","haber","hakala"]
COMPACT={"haber","hakala"}   # de-emphasized: single image, no large grid
cats=[("all","All"),("Full Home","Homes"),("Kitchen","Kitchens"),("Bath","Baths"),("Interiors","Interiors"),("Hospitality","Hospitality")]
def fbtn(k,lbl):
    ac=' class="active"' if k=="all" else ''
    return f'<button data-filter="{k}"{ac}>{lbl}</button>'
filt="".join(fbtn(k,lbl) for k,lbl in cats)
proj=[]
for slug in order:
    d=M[slug]
    compact = slug in COMPACT
    pcls = "project compact reveal" if compact else "project reveal"
    if compact:
        # single wide image; still opens the lightbox (which pages through this project's shots)
        full=d["images"][0]["full"]; thumb=d["images"][0]["thumb"]
        others="".join(f'<span class="lb-src" data-full="{im["full"]}"></span>' for im in d["images"][1:])
        th=f'<div class="tile full" data-full="{full}"><img src="{thumb}" alt="{d["name"]}" loading="lazy"></div>{others}'
    else:
        th="".join(f'<div class="tile {c}" data-full="{im["full"]}"><img src="{im["thumb"]}" alt="{d["name"]}" loading="lazy"></div>' for c,im in tiles(d["images"]))
    proj.append(f'''
  <div class="{pcls}" data-cat="{d['cat']}">
    <div class="project-head"><h3>{d['name']}</h3><span class="loc"><span class="cat-tag">{d['cat']}</span> &nbsp;/&nbsp; {d['loc']}</span></div>
    <div class="grid-gallery">{th}</div>
  </div>''')
work=f'''
<section class="page-hero">
  <div class="wrap"><p class="eyebrow reveal">Work</p><h1 class="reveal">Selected projects</h1>
  <p class="reveal">Full-home interiors, custom kitchens and baths, and architecture across the greater Seattle area. Click any image to enlarge.</p></div>
</section>
<section class="pad-sm">
  <div class="wrap">
    <div class="filters reveal">{filt}</div>
    <div id="work-root"></div>
  </div>
</section>
<div class="lb" id="lb"><button class="close">Close &times;</button><button class="nav prev">&lsaquo;</button><img src="" alt=""><button class="nav next">&rsaquo;</button></div>
<section class="cta pad"><div class="wrap"><h2 class="reveal">Let&rsquo;s design yours</h2><p class="reveal">From a single room to a full build, we&rsquo;d love to hear about it.</p><div class="reveal"><a class="btn light" href="contact.html">Start a Project</a></div></div></section>
'''

# ---------------- UPCOMING WORK ----------------
RM=json.load(open("/home/claude/drift-ia-site/rend_manifest.json"))
up_cards=[]
for slug in RM["order"]:
    d=RM["projects"][slug]
    hero=d["images"][0]
    hidden="".join(f'<span class="lb-src" data-full="{im["full"]}"></span>' for im in d["images"][1:])
    up_cards.append(f'''
    <div class="up-card reveal">
      <div class="ph" data-full="{hero['full']}">
        <span class="status">{d['status']}</span>
        <img src="{hero['thumb']}" alt="{d['name']} rendering" loading="lazy">
        {hidden}
      </div>
      <div class="meta"><h3>{d['name']}</h3><div class="t">{d['type']}</div></div>
    </div>''')
upcoming=f'''
<section class="page-hero">
  <div class="wrap"><p class="eyebrow reveal">Upcoming Work</p><h1 class="reveal">On the boards</h1>
  <p class="reveal">A first look at projects currently in design and under construction. These are renderings and visualizations &mdash; finished photography to follow. Click any image to view it larger.</p></div>
</section>
<section class="pad-sm">
  <div class="wrap">
    <div class="up-grid" id="up-root"></div>
  </div>
</section>
<div class="lb" id="lb"><button class="close">Close &times;</button><button class="nav prev">&lsaquo;</button><img src="" alt=""><button class="nav next">&rsaquo;</button></div>
<section class="cta pad"><div class="wrap"><p class="eyebrow light reveal">Building Something?</p><h2 class="reveal">Let&rsquo;s add yours to the boards</h2><p class="reveal">Whether it&rsquo;s a new build, a remodel, or a room, we&rsquo;d love to design it with you.</p><div class="reveal"><a class="btn light" href="contact.html">Start a Project</a></div></div></section>
{CROSSLINK}
'''

# ---------------- SERVICES ----------------
services=f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow reveal">Services</p><h1 class="reveal">How we can help</h1>
<p class="reveal">A full-service studio spanning interior design and licensed architecture — for homeowners, builders, and developers.</p></div></section>

<section class="split">
  <div class="media"><img src="{first("gala")}" alt="Full home interior"></div>
  <div class="body reveal"><p class="eyebrow">01 &mdash; Interior Design</p><h2>Full-house &amp; luxury interiors</h2>
  <p>Whole-home interior design that brings space planning, finishes, lighting, and furnishings into one cohesive vision — tailored to how you live and built to last.</p>
  <p style="font-size:15px;color:var(--ink-soft);">Full-home design &middot; Luxury interiors &middot; Furnishings &amp; styling &middot; Finish selection</p></div>
</section>
<section class="split reverse">
  <div class="media"><img src="{first("solinsky")}" alt="Residential architecture"></div>
  <div class="body reveal"><p class="eyebrow">02 &mdash; Architecture</p><h2>Residential &amp; multifamily</h2>
  <p>Licensed architectural design for new homes, additions, and multifamily developments — thoughtful, code-savvy, and grounded in 11+ years of high-end residential and multifamily experience.</p>
  <p style="font-size:15px;color:var(--ink-soft);">New construction &middot; Additions &middot; Multifamily &middot; Space planning</p></div>
</section>
<section class="split">
  <div class="media"><img src="{first("haber")}" alt="Custom kitchen"></div>
  <div class="body reveal"><p class="eyebrow">03 &mdash; Kitchens &amp; Baths</p><h2>Renovations, refined</h2>
  <p>Kitchens and baths designed to work beautifully every day — from layout and cabinetry to tile, stone, and fixtures, coordinated with our trusted trades.</p>
  <p style="font-size:15px;color:var(--ink-soft);">Kitchen design &middot; Bath design &middot; Cabinetry &middot; Material selection</p></div>
</section>
<section class="split reverse">
  <div class="media"><img src="{first("gig-harbor")}" alt="Hospitality design"></div>
  <div class="body reveal"><p class="eyebrow">04 &mdash; Hospitality &amp; Consultation</p><h2>Short-term rental &amp; advisory</h2>
  <p>Design for short-term rentals and hospitality spaces that photograph beautifully and earn their keep — plus real-estate market consultation and remodeling assessments for buyers and investors.</p>
  <p style="font-size:15px;color:var(--ink-soft);">Hospitality &amp; STR design &middot; Market consultation &middot; Remodel assessment</p></div>
</section>

<section class="pad-sm"><div class="wrap"><div class="section-head center reveal"><hr class="rule"><p class="eyebrow">Getting Started</p>
<h2 style="font-size:clamp(26px,3.4vw,40px);">Design packages &amp; consultations</h2>
<p>Not sure where to begin? Book a consultation or a design package and we&rsquo;ll map the right scope for your project and budget.</p></div>
<div class="center reveal" style="margin-top:36px;"><a class="btn solid" href="contact.html">Book a Consultation</a></div></div></section>
{CROSSLINK}
'''

# ---------------- ABOUT ----------------
about=f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow reveal">The Studio</p><h1 class="reveal">Design with intent</h1>
<p class="reveal">Drift is an architecture and interior design creative studio based in Lake Stevens, serving the greater Seattle area.</p></div></section>

<section class="split">
  <div class="media"><img src="{nth('solinsky',0)}" alt="Designed living space"></div>
  <div class="body reveal"><p class="eyebrow">Our Philosophy</p><h2>Good ideas, good coffee, good design</h2>
  <p>We believe the best spaces come from intention — a clear understanding of how a room will be used, then design that makes it feel effortless. Our work is fluid and dynamic, balancing architectural rigor with warmth and livability.</p>
  <p>Whether it&rsquo;s a single kitchen or a ground-up multifamily building, we bring the same care to every square foot.</p></div>
</section>

<section class="split reverse">
  <div class="media"><img src="{nth('bowen',1)}" alt="Kitchen by Jen"></div>
  <div class="body reveal"><p class="eyebrow">Founder &amp; Principal</p><h2>Meet Jen</h2>
  <p>Jen is the founder and principal of Drift — a Washington State&ndash;licensed architect and Syracuse University graduate with more than a decade of experience in multifamily and high-end residential design, including six-plus years in New York City.</p>
  <p>An IIDA member who has built interior design departments from the ground up, she leads every project with a rare dual fluency: the technical precision of architecture and the curatorial eye of interior design.</p></div>
</section>

<section class="pad"><div class="wrap"><div class="section-head center reveal"><hr class="rule"><p class="eyebrow">What Guides Us</p><h2>Three principles</h2></div>
<div class="values">
  <div class="reveal"><span class="num">I.</span><h3>Intention first</h3><p>Design decisions follow function. We start with how you&rsquo;ll live, then shape space, light, and material around it.</p></div>
  <div class="reveal"><span class="num">II.</span><h3>Architectural depth</h3><p>A licensed architect&rsquo;s understanding of structure and code, applied even to interiors, kitchens, and baths.</p></div>
  <div class="reveal"><span class="num">III.</span><h3>Livable beauty</h3><p>Rooms that are as easy to live in as they are to love — refined, durable, and personal.</p></div>
</div></div></section>
{CROSSLINK}
'''

# ---------------- CONTACT ----------------
def opts(name, items, req=True):
    o='<option value="" disabled selected>Select&hellip;</option>'+"".join(f'<option>{i}</option>' for i in items)
    return f'<select name="{name}"{" required" if req else ""}>{o}</select>'
contact=f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow reveal">Start a Project</p><h1 class="reveal">Let&rsquo;s begin</h1>
<p class="reveal">Share a few details about your project and we&rsquo;ll follow up to talk through the right approach, scope, and next steps. Every field but name and email is optional.</p></div></section>
<section class="pad-sm"><div class="wrap" style="max-width:900px;">
  <form class="lead-form reveal" name="design-inquiry" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thank-you">
    <input type="hidden" name="form-name" value="design-inquiry">
    <p class="hp"><label>Leave blank: <input name="bot-field"></label></p>
    <div class="frow">
      <div class="field"><label>Name <span>*</span></label><input name="name" required></div>
      <div class="field"><label>Email <span>*</span></label><input type="email" name="email" required></div>
    </div>
    <div class="frow">
      <div class="field"><label>Phone</label><input type="tel" name="phone"></div>
      <div class="field"><label>Project Address / City</label><input name="address"></div>
    </div>
    <div class="frow">
      <div class="field"><label>Type of Project</label>{opts("project_type",["Full-home interior design","Kitchen remodel","Bathroom remodel","New construction / architecture","Build from a library plan","Addition or remodel","Multifamily development","Hospitality / short-term rental","Not sure yet"],req=False)}</div>
      <div class="field"><label>Approx. Size (sq ft)</label>{opts("size",["Under 1,000","1,000–2,500","2,500–4,000","4,000–6,000","6,000+","Unknown"],req=False)}</div>
    </div>
    <div class="frow">
      <div class="field"><label>Design Services Budget</label>{opts("design_budget",["Under $10k","$10k–$25k","$25k–$50k","$50k–$100k","$100k+","Unknown / need guidance"],req=False)}</div>
      <div class="field"><label>Construction Budget</label>{opts("construction_budget",["Under $100k","$100k–$300k","$300k–$600k","$600k–$1M","$1M+","Unknown / TBD"],req=False)}</div>
    </div>
    <div class="frow">
      <div class="field"><label>Style / Inspiration</label><input name="style" placeholder="e.g. warm modern, transitional, not sure"></div>
      <div class="field"><label>Ideal Timeline</label>{opts("timeline",["Ready to start","1–3 months","3–6 months","6–12 months","Just exploring"],req=False)}</div>
    </div>
    <div class="field"><label>Tell us about your project</label><textarea name="message" rows="4" placeholder="What are you dreaming up?"></textarea></div>
    <div class="form-actions">
      <button class="btn solid" type="submit">Submit Inquiry</button>
      <p class="form-note">Prefer to reach us directly? <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="tel:{PHONE.replace('-','')}">{PHONE}</a></p>
    </div>
  </form>
  <div class="form-success" hidden><h2>Thank you &mdash; we&rsquo;ll be in touch.</h2><p>Your inquiry is on its way to the studio. We typically reply within one to two business days.</p></div>
</div></section>
<section class="crosslink pad-sm"><div class="wrap">
  <div class="txt"><p class="eyebrow">The Studio</p><h3>Drift Interiors + Architecture</h3>
  <p>{ADDR} &middot; Serving Lake Stevens, Greater Seattle &amp; the Puget Sound region.</p></div>
  <div style="text-align:right;"><a href="mailto:{EMAIL}" class="tlink">{EMAIL}</a><br><br><a href="tel:{PHONE.replace('-','')}" class="tlink">{PHONE}</a></div>
</div></section>
'''

# ---------------- PLANS LIBRARY ----------------
# NOTE: sqft / beds / baths below are placeholders — replace with real specs per plan.
PLANS=[
 dict(slug="si-plan",  name="The Si Plan",     type="Modern Farmhouse", sqft=2650, beds=4, baths="2.5", approved=True,  status="Approved &mdash; City of Everett (Basic Plan)"),
 dict(slug="sansoni",  name="The Sansoni",     type="Contemporary",     sqft=3200, beds=4, baths="3.5", approved=False, status="Library Plan"),
 dict(slug="yadi",     name="The Yadi",        type="Modern",           sqft=2900, beds=4, baths="3",   approved=False, status="Library Plan"),
 dict(slug="elenes",   name="The Elenes",      type="Contemporary",     sqft=3400, beds=5, baths="3.5", approved=False, status="Library Plan"),
 dict(slug="marysville",name="Blake Lot",      type="Modern Farmhouse", sqft=2500, beds=4, baths="2.5", approved=False, status="Library Plan"),
 dict(slug="farmhouse",name="The Farmhouse",   type="Modern Farmhouse", sqft=2800, beds=4, baths="2.5", approved=False, status="Library Plan"),
 dict(slug="craftsman",name="The Craftsman",   type="Craftsman",        sqft=2600, beds=4, baths="3",   approved=False, status="Library Plan"),
 dict(slug="bothell",  name="The Bothell",     type="Modern Farmhouse", sqft=3100, beds=4, baths="3.5", approved=False, status="Library Plan"),
]
def plan_img(slug): return f"assets/img/upcoming/{slug}/{slug}-01-t.jpg"
_ptypes=sorted(set(p["type"] for p in PLANS))
type_opts='<option value="">All Styles</option>'+"".join(f'<option>{t}</option>' for t in _ptypes)
size_opts=('<option value="">Any Size</option>'
 '<option value="0-2500">Under 2,500 sq ft</option>'
 '<option value="2500-3000">2,500 – 3,000 sq ft</option>'
 '<option value="3000-3500">3,000 – 3,500 sq ft</option>'
 '<option value="3500-99999">3,500+ sq ft</option>')
plan_cards=[]
for p in PLANS:
    badge=f'<span class="badge">Approved &middot; Everett</span>' if p["approved"] else ''
    status_cls="pstatus approved" if p["approved"] else "pstatus"
    plan_cards.append(f'''
      <article class="plan-card" data-type="{p['type']}" data-size="{p['sqft']}" data-name="{p['name'].lower()}">
        <div class="ph">{badge}<img src="{plan_img(p['slug'])}" alt="{p['name']} rendering" loading="lazy"></div>
        <div class="pmeta">
          <h3>{p['name']}</h3>
          <div class="ptype">{p['type']}</div>
          <div class="specs">{p['sqft']:,} sq ft &middot; {p['beds']} bd &middot; {p['baths']} ba</div>
          <div class="{status_cls}">{p['status']}</div>
          <a class="tlink" href="contact.html">Inquire on Pricing &nearr;</a>
        </div>
      </article>''')
plans=f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow reveal">Home Plans</p><h1 class="reveal">The plans library</h1>
<p class="reveal">Thoughtfully designed homes, ready to build &mdash; available as-drawn or tailored to your site. Browse by size and style below. Square footages are approximate and confirmed on inquiry.</p></div></section>

<section class="pad-sm" style="padding-top:0;"><div class="wrap">
  <div class="approved-note reveal">
    <p class="eyebrow">Pre-Approved &amp; Permit-Ready</p>
    <h2>Some plans are already approved to build</h2>
    <p>In select jurisdictions, our designs are pre-approved for construction. In the <strong>City of Everett</strong>, <strong>The Si Plan</strong> is approved as a <strong>Basic Plan</strong> &mdash; cleared to build on an <strong>expedited permit with no modifications required</strong>. Ask us which plans are approved in your jurisdiction.</p>
  </div>
</div></section>

<section class="pad-sm" style="padding-top:0;"><div class="wrap">
  <div class="plan-filters reveal">
    <input id="plan-q" type="search" placeholder="Search plans by name&hellip;" aria-label="Search plans">
    <select id="plan-type" aria-label="Filter by style">{type_opts}</select>
    <select id="plan-size" aria-label="Filter by size">{size_opts}</select>
  </div>
  <div class="plan-count" id="plan-count"></div>
  <div class="plan-grid" id="plan-grid"></div>
  <p class="plan-empty" id="plan-empty" hidden>No plans match those filters &mdash; <a href="contact.html">tell us what you&rsquo;re looking for</a> and we&rsquo;ll design it.</p>
</div></section>

<section class="pad-sm"><div class="wrap"><div class="section-head center reveal"><hr class="rule"><p class="eyebrow">Pricing</p>
<h2 style="font-size:clamp(26px,3.4vw,42px);">As-drawn, or tailored to you</h2>
<p>Every plan can be built as-is or adjusted with modifications. We&rsquo;ll work through pricing for the plan as-drawn and for any changes you have in mind &mdash; reach out and we&rsquo;ll put the details together.</p></div>
<div class="center reveal" style="margin-top:36px;"><a class="btn solid" href="contact.html">Request Plan Pricing</a></div></div></section>
{CROSSLINK}
'''

# ---------------- CONNECT / SOCIAL ----------------
def soc(name, key, desc):
    return (f'<a class="soc-card" data-social="{key}" href="#" target="_blank" rel="noopener" hidden>'
            f'<span class="soc-name">{name}</span><span class="soc-h">{desc}</span></a>')
connect=f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow reveal">Connect</p><h1 class="reveal">Follow along</h1>
<p class="reveal">See the studio&rsquo;s latest work, works-in-progress, and inspiration &mdash; and find us across the platforms where design lives.</p></div></section>

<section class="pad-sm" style="padding-top:0;"><div class="wrap">
  <div class="section-head center reveal"><hr class="rule"><p class="eyebrow" data-social="instagram-eyebrow">On Instagram</p>
  <h2 style="font-size:clamp(28px,3.6vw,46px);">The latest from the studio</h2></div>
  <div id="ig-embed" class="ig-embed reveal">
    <div><p style="margin:0 0 14px;">Our Instagram feed appears here once connected.</p>
    <a class="btn solid" data-social="instagram" href="#" target="_blank" rel="noopener">Follow on Instagram</a></div>
  </div>
</div></section>

<section class="pad-sm"><div class="wrap">
  <div class="section-head center reveal"><hr class="rule"><p class="eyebrow">Find Us</p>
  <h2 style="font-size:clamp(26px,3.4vw,42px);">Across the web</h2>
  <p>Explore our profiles, portfolios, and saved inspiration.</p></div>
  <div class="soc-grid reveal">
    {soc("Instagram","instagram","Daily work &amp; process")}
    {soc("Facebook","facebook","News &amp; projects")}
    {soc("Pinterest","pinterest","Inspiration boards")}
    {soc("Houzz","houzz","Portfolio &amp; reviews")}
    {soc("ArchiPro","archipro","Architecture profile")}
    {soc("AD PRO","adpro","Directory listing")}
    {soc("LinkedIn","linkedin","The studio")}
  </div>
  <p class="soc-empty reveal" id="soc-empty">Add your profile links in the admin (Site Text &amp; Social) and they&rsquo;ll appear here.</p>
</div></section>

<section class="crosslink pad-sm"><div class="wrap">
  <div class="txt"><p class="eyebrow">Recognition</p><h3>Members &amp; listed with</h3>
  <p>Drift is proud to be part of the professional design community &mdash; find our work and profiles on AD&nbsp;PRO, ArchiPro, Houzz, and as an IIDA member.</p></div>
  <a class="btn" href="contact.html">Work With Us</a>
</div></section>
'''

# ---------------- JOURNAL (blog) ----------------
journal=f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow reveal">Journal</p><h1 class="reveal">Notes from the studio</h1>
<p class="reveal">Design thinking, project stories, and the ideas behind our work &mdash; across interiors, architecture, and staging.</p></div></section>
<section class="pad-sm"><div class="wrap">
  <div class="journal-grid" id="journal-root"></div>
</div></section>
<div class="reader" id="reader"><button class="reader-close" aria-label="Close">Close &times;</button><article class="reader-inner"></article></div>
<section class="cta pad"><div class="wrap"><p class="eyebrow light reveal">Stay in Touch</p><h2 class="reveal">Follow along on Instagram &amp; LinkedIn</h2>
<p class="reveal">New projects, process, and journal entries as they happen.</p>
<div class="reveal"><a class="btn light" href="connect.html">Connect With Us</a></div></div></section>
'''

pages={
 "index.html":("Drift Interiors + Architecture &mdash; Design With Intent","home","on-dark",home,"Architecture and interior design studio serving the greater Seattle area. Design with intent."),
 "connect.html":("Connect &mdash; Drift Interiors + Architecture","connect","on-light",connect,"Follow Drift Interiors + Architecture on Instagram, Facebook, Pinterest, Houzz, ArchiPro, LinkedIn, and AD PRO."),
 "journal.html":("Journal &mdash; Drift Interiors + Architecture","journal","on-light",journal,"Design thinking, project stories, and studio notes on interiors, architecture, and home staging from Drift."),
 "plans.html":("Home Plans &amp; Pre-Approved Designs &mdash; Drift Interiors + Architecture","plans","on-light",plans,"Browse Drift's library of ready-to-build home plans by size and style — including The Si Plan, pre-approved as a Basic Plan in the City of Everett for expedited permitting."),
 "work.html":("Work &mdash; Drift Interiors + Architecture","work","on-light",work,"Selected interior design and architecture projects across the Seattle area."),
 "upcoming.html":("Upcoming Work &mdash; Drift Interiors + Architecture","upcoming","on-light",upcoming,"Projects on the boards — renderings of homes and spaces in design and under construction."),
 "services.html":("Services &mdash; Drift Interiors + Architecture","services","on-light",services,"Interior design, residential and multifamily architecture, kitchens, baths, and hospitality design."),
 "about.html":("The Studio &mdash; Drift Interiors + Architecture","about","on-light",about,"Meet Jen and the Drift studio — a licensed architect and interior designer in Lake Stevens, WA."),
 "contact.html":("Contact &mdash; Drift Interiors + Architecture","contact","on-light",contact,"Start an interior design or architecture project with Drift."),
}
for fn,(t,a,mo,b,d) in pages.items():
    open(os.path.join(OUT,fn),"w").write(page(t,a,mo,b,d,fn)); print("wrote",fn)


# ---- data files for the admin CMS (galleries render from these) ----
import json as _json
os.makedirs(os.path.join(OUT,"data"),exist_ok=True)
_projects=[{"name":M[s]["name"],"category":M[s]["cat"],"location":M[s]["loc"],
            "compact":(s in COMPACT),"images":[im["full"] for im in M[s]["images"]]} for s in order]
_json.dump({"projects":_projects}, open(os.path.join(OUT,"data","projects.json"),"w"), indent=2)
_up=[{"name":RM["projects"][s]["name"],"type":RM["projects"][s]["type"],"status":RM["projects"][s]["status"],
      "images":[im["full"] for im in RM["projects"][s]["images"]]} for s in RM["order"]]
_json.dump({"upcoming":_up}, open(os.path.join(OUT,"data","upcoming.json"),"w"), indent=2)
_pl=[{"name":p["name"],"type":p["type"],"sqft":p["sqft"],"beds":p["beds"],"baths":p["baths"],
      "approved":p["approved"],"status":p["status"],"image":plan_img(p["slug"])} for p in PLANS]
_json.dump({"plans":_pl}, open(os.path.join(OUT,"data","plans.json"),"w"), indent=2)
_content={"statement":"\u201cWe design spaces where good ideas \u2014 and good coffee \u2014 flow freely: intentional, fluid, and made for the way you actually live.\u201d","email":"jen@drift-ia.com","phone":"425-478-0327","address":"14526 107th St NE \u00b7 Lake Stevens, WA 98258","instagramHandle":"","instagramEmbed":"","social":{"instagram":"","facebook":"","pinterest":"","houzz":"","linkedin":"","archipro":"","adpro":""}}
_json.dump(_content, open(os.path.join(OUT,"data","content.json"),"w"), indent=2)
print("wrote data/*.json + content.json")

# sitemap + robots
SITE=SITE_URL
urls="".join(f"<url><loc>{SITE}/{fn}</loc><changefreq>monthly</changefreq></url>" for fn in pages)
open(os.path.join(OUT,"sitemap.xml"),"w").write(
    f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("done")
