#!/usr/bin/env python3
"""Builds website/*.html from page bodies below so header/footer stay identical. Run: python3 build.py"""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "website")
NAV = [("services.html","Services"),("process.html","How it works"),("security.html","Security"),("partners.html","Our partner"),("industries.html","Industries")]

def shell(fn, title, desc, body, active=""):
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h==active else ""}>{t}</a>' for h,t in NAV)
    foot = "".join(f'<a href="{h}">{t}</a>' for h,t in NAV)
    js = JS if fn=="contact.html" else ""
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" href="assets/phd-logo.png"><link rel="stylesheet" href="styles.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<header><div class="wrap bar">
<a class="logo" href="index.html" aria-label="PHD Computing home"><img src="assets/phd-logo.png" alt="" width="44" height="44"><span>PHD Computing<small>IT Asset Disposition</small></span></a>
<button class="menu" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
<nav id="nav">{nav}<a class="btn sm" href="contact.html">Request a quote</a></nav></div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><div class="cols">
<div><div class="logo" style="margin-bottom:12px"><img src="assets/phd-logo.png" alt="" width="36" height="36"><span>PHD Computing</span></div><p>Secure IT asset disposition and electronics recycling for businesses across New England and the Northeast.</p></div>
<div><h4>Company</h4>{foot}</div>
<div><h4>Contact</h4><a href="contact.html">Request a quote</a><a href="#">Privacy Policy</a><a href="#">Terms of Service</a></div></div>
<div class="fine">&copy; 2026 PHD Computing. All rights reserved.</div></div></footer>{js}<script>(function(){{var b=document.querySelector('.menu'),n=document.getElementById('nav');b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.classList.toggle('x',o)}});n.addEventListener('click',function(e){{if(e.target.tagName=='A'){{n.classList.remove('open');b.classList.remove('x');b.setAttribute('aria-expanded',false)}}}})}})()</script><script>(function(){{var d=document.documentElement;d.classList.add('js');var rm=matchMedia('(prefers-reduced-motion:reduce)').matches;var els=document.querySelectorAll('.rv,.steps');if(rm){{els.forEach(function(e){{e.classList.add('in')}});return}}els.forEach(function(e,i){{e.style.transitionDelay=(e.classList.contains('rv')?(i%3)*80:0)+'ms'}});function chk(){{var h=innerHeight*.92;els.forEach(function(e){{if(!e.classList.contains('in')&&e.getBoundingClientRect().top<h)e.classList.add('in')}})}}addEventListener('scroll',chk,{{passive:true}});addEventListener('resize',chk);chk();setTimeout(chk,150);setTimeout(function(){{els.forEach(function(e){{e.classList.add('in')}})}},6000);if(matchMedia('(hover:hover)').matches){{document.querySelectorAll('.hero,.cta-band').forEach(function(h){{h.addEventListener('mousemove',function(e){{var r=h.getBoundingClientRect();h.style.setProperty('--mx',(e.clientX-r.left)+'px');h.style.setProperty('--my',(e.clientY-r.top)+'px')}})}})}}}})()</script></body></html>'''

def hero(eyebrow, h1, lead, cta=True, big=False):
    c = '<div class="cta"><a class="btn" href="contact.html">Request a quote</a></div>' if cta else ""
    return f'<div class="hero{" big" if big else ""}"><div class="hero-art" aria-hidden="true"></div><div class="wrap hin"><div class="eyebrow">{eyebrow}</div><h1>{h1}</h1><p class="lead">{lead}</p>{c}</div></div>'

def head(e, h, p=""):
    return f'<div class="head"><div class="eyebrow">{e}</div><h2>{h}</h2>{"<p>"+p+"</p>" if p else ""}</div>'

def ico(path): return f'<div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{path}</svg></div>'
I = dict(
 lock='<rect x="4" y="11" width="16" height="9" rx="2"/><path d="M8 11V7a4 4 0 018 0v4"/>',
 truck='<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/>',
 cycle='<path d="M12 3a9 9 0 109 9"/><path d="M12 3v5l3-2"/><path d="M8 13l3 3 5-6"/>',
 doc='<path d="M5 4h14v16H5z"/><path d="M9 9h6M9 13h6M9 17h3"/>',
 dollar='<path d="M12 2v20M17 6.5C17 4.6 14.8 4 12 4S7 5 7 7s2 3 5 3 5 1 5 3.5S14.8 20 12 20s-5-.8-5-2.8"/>',
 bars='<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>')

def icard(i, h, p):
    return f'<a class="icard rv" href="contact.html"><div class="im" style="background-image:url(assets/card-{i}.svg)"></div><div class="tx"><h3>{h}</h3><p>{p}</p><span class="pill">Request a quote</span></div></a>'

def card(i, h, p, href=None):
    a = f'<p style="margin-top:14px"><a class="more" href="{href}">Learn more &rarr;</a></p>' if href else ""
    return f'<div class="card rv">{ico(I[i])}<h3>{h}</h3><p>{p}</p>{a}</div>'

SERV = [("lock","Data destruction","Hard drives and storage media sanitized or physically destroyed to your requirements, with a certificate for each job."),
 ("truck","Pickup &amp; logistics","Scheduled, secure collection from single offices to multi-site rollouts, with every item counted and logged."),
 ("cycle","Electronics recycling","Computers, servers, networking gear and peripherals recycled responsibly, with nothing sent to landfill by design."),
 ("doc","Asset reporting","Itemized inventories by serial number and asset tag, delivered in a format your audit team can use."),
 ("dollar","Value recovery","Equipment with resale value is evaluated, so your retirement program can offset its own cost where possible."),
 ("bars","Program planning","Office moves, data-center cleanouts and refresh cycles planned with a timeline, a scope and a named contact.")]

pages = {}
pages["index.html"] = ("PHD Computing | Secure IT Asset Disposition &amp; Electronics Recycling, New England",
 "Secure IT asset retirement, NIST-compliant data destruction and responsible electronics recycling for businesses across New England and the Northeast.", "",
 hero("Massachusetts &middot; New England &middot; Northeast","Retire IT equipment securely.<br>Prove it was done.","We collect, track and responsibly dispose of your retired computers, servers and electronics, and give you the documentation your auditors and compliance team ask for. Trusted by Fortune 500 enterprises across New England.",big=True).replace('</div></div></div>','<a class="btn ghost" href="process.html" style="margin-left:0">See how it works</a></div></div></div>',1) +
 '''<div class="trust"><div class="wrap"><div><b>Fortune 500 trusted</b>enterprise IT asset management</div><div><b>NIST-compliant</b>data destruction</div><div><b>Chain of custody</b>pickup to final disposition</div><div><b>Certificate of destruction</b>for every job</div></div></div>
<section><div class="wrap">''' + head("What we do","Everything between &ldquo;retired&rdquo; and &ldquo;documented&rdquo;","One point of contact for the full lifecycle of end-of-use technology.") +
 '<div class="grid g3">' + "".join(icard(i,h,p) for i,h,p in SERV[:3]) + '</div><p style="margin-top:28px"><a class="more" href="services.html">All services &rarr;</a></p></div></section>' +
 '''<section class="alt"><div class="wrap">''' + head("Explore","Built for enterprise buyers") + '''<div class="grid g3">
<div class="card rv"><h3>How it works</h3><p>Scope, collect, process, document. A simple process with a paper trail.</p><p style="margin-top:14px"><a class="more" href="process.html">See the process &rarr;</a></p></div>
<div class="card rv"><h3>Security &amp; compliance</h3><p>NIST-compliant destruction and documentation built around your requirements.</p><p style="margin-top:14px"><a class="more" href="security.html">Security details &rarr;</a></p></div>
<div class="card rv"><h3>Our processing partner</h3><p>Final processing at a certified recycling and destruction facility.</p><p style="margin-top:14px"><a class="more" href="partners.html">About our partner &rarr;</a></p></div></div></div></section>
<section class="cta-band"><div class="wrap"><h2>Ready to retire equipment the right way?</h2><p>Tell us what you have. A person will reply, usually within one business day.</p><a class="btn" href="contact.html">Request a quote</a></div></section>''', "")

pages["services.html"] = ("Services | PHD Computing","IT asset disposition services: data destruction, secure pickup, electronics recycling, asset reporting, value recovery and program planning.","",
 hero("Services","One partner for the full lifecycle","From secure collection to final certificate, every step is tracked and documented.") +
 '<section><div class="wrap"><div class="grid g3">' + "".join(icard(*s) for s in SERV) + '</div></div></section>' +
 '<section class="cta-band"><div class="wrap"><h2>Not sure what you need?</h2><p>Describe the equipment and we will scope it with you.</p><a class="btn" href="contact.html">Request a quote</a></div></section>', "services.html")

pages["process.html"] = ("How it works | PHD Computing","Our four-step process: scope, collect, process and document, with a paper trail for every job.","",
 hero("How it works","A simple process with a paper trail","Four steps, one point of contact, and documentation you can hand to an auditor.") +
 '''<section><div class="wrap"><div class="steps">
<div class="step rv"><h3>Scope</h3><p>Tell us what you have, where it is, and what your policy requires. We record your requirements, including your state's rules.</p></div>
<div class="step rv"><h3>Collect</h3><p>Secure pickup scheduled around your operations. Items are counted and logged at handover.</p></div>
<div class="step rv"><h3>Process</h3><p>Data is destroyed and equipment is recycled or remarketed at our certified processing partner.</p></div>
<div class="step rv"><h3>Document</h3><p>You receive the itemized asset report and certificate for your records.</p></div></div></div></section>
<section class="cta-band"><div class="wrap"><h2>Start with a scope</h2><p>No obligation. Clear pricing before we begin.</p><a class="btn" href="contact.html">Request a quote</a></div></section>''', "process.html")

pages["security.html"] = ("Security &amp; compliance | PHD Computing","NIST-compliant data destruction, itemized inventories, certificates of destruction and state-aware compliance across the Northeast.","",
 hero("Security &amp; compliance","Built around your requirements, not ours","Different customers need different proof. We record your requirements up front and deliver the documentation that matches.") +
 '''<section><div class="wrap split"><div>''' + head("Our approach","Documentation that matches your policy") + '''<p style="color:var(--muted)">Our records follow the rules of the state where you operate, from New York through New England.</p></div>
<ul class="tick"><li>NIST-compliant data destruction</li><li>Itemized serial-number inventory for every job</li><li>Certificate of destruction issued per job</li><li>Customer-specific requirements recorded and followed</li><li>Compliance with the laws of your state, across the Northeast</li><li>Records retained and available for your audits</li></ul></div></section>
<section class="cta-band"><div class="wrap"><h2>Questions from your compliance team?</h2><p>Send them our way.</p><a class="btn" href="contact.html">Contact us</a></div></section>''', "security.html")

pages["partners.html"] = ("Our certified processing partner | PHD Computing","Final data destruction and recycling are performed by our certified processing partner, documented end to end.","",
 hero("Processing partner","Certified processing,<br>documented end to end.","Final data destruction and recycling are performed by our certified processing partner, so every job ends with proof, not promises.") +
 '''<!-- TODO(Matt): add partner's legal name, certifications and facility photos once confirmed. Do not invent them. -->
<section><div class="wrap">''' + head("What happens at the facility","From receiving dock to certificate") + '''<div class="grid g2">
<div class="card rv"><h3>1. Receiving &amp; inventory</h3><p>Your equipment is received, counted and itemized against the list from pickup.</p></div>
<div class="card rv"><h3>2. Data destruction</h3><p>Storage media is sanitized or physically destroyed to your requirements.</p></div>
<div class="card rv"><h3>3. Recycling &amp; recovery</h3><p>Equipment is dismantled and recycled responsibly. Items with resale value are evaluated.</p></div>
<div class="card rv"><h3>4. Documentation</h3><p>You receive the asset report and certificate for your audit file.</p></div></div></div></section>
<section class="alt"><div class="wrap split"><div>''' + head("Why it matters","Your risk does not end at pickup") + '''</div><ul class="tick"><li>One accountable contact from pickup to certificate</li><li>Controlled, certified processing</li><li>Records available for your audits</li></ul></div></section>''', "partners.html")

pages["industries.html"] = ("Industries | PHD Computing","Experience with regulated environments: financial services, healthcare, government, legal, technology and manufacturing.","",
 hero("Industries","Experience with regulated environments","Enterprise and regulated customers need proof. We build the paper trail around their rules.") +
 '<section><div class="wrap"><div class="sectors">' + "".join(f"<span>{s}</span>" for s in ["Financial services","Healthcare","Government &amp; education","Legal","Technology","Manufacturing","Professional services"]) + '</div></div></section>' +
 '<section class="cta-band"><div class="wrap"><h2>Tell us your requirements</h2><p>We will match the documentation to your industry and state.</p><a class="btn" href="contact.html">Request a quote</a></div></section>', "industries.html")

pages["contact.html"] = ("Request a quote | PHD Computing","Request a quote for secure IT asset disposition and electronics recycling in New England.","",
 '''<section style="padding-top:150px"><div class="wrap split"><div><div class="eyebrow">Get started</div><h1 style="font-size:clamp(2rem,4vw,3rem)">Request a quote</h1>
<p style="color:var(--muted)">Tell us about the equipment and any compliance requirements. A person will reply, usually within one business day.</p>
<ul class="tick"><li>No obligation</li><li>Clear scope and pricing before we start</li><li>Pickup scheduled around your operations</li></ul></div>
<form id="quote" action="#" method="post">
<div class="row"><label>First name<input required name="first" autocomplete="given-name"></label><label>Last name<input required name="last" autocomplete="family-name"></label></div>
<div class="row"><label>Work email<input required type="email" name="email" autocomplete="email"></label><label>Phone<input type="tel" name="phone" autocomplete="tel"></label></div>
<div class="row"><label>Company<input name="company" autocomplete="organization"></label><label>State<input name="state" placeholder="e.g. MA, NY, CT" autocomplete="address-level1"></label></div>
<label>I am inquiring as<select name="type"><option>Business</option><option>Enterprise</option><option>Government / education</option><option>Healthcare</option><option>Other</option></select></label>
<label>What needs to be retired?<textarea rows="4" name="msg" placeholder="Approximate quantity, locations, any compliance or certificate requirements"></textarea></label>
<input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px">
<button class="btn" type="submit">Send request</button><p class="note" id="status" role="status" aria-live="polite">We use your details only to respond to this request.</p></form></div></section>''', "")

JS = '''<script>
document.getElementById('quote').addEventListener('submit',async e=>{
 e.preventDefault();const f=e.target,b=f.querySelector('button'),st=document.getElementById('status');
 b.disabled=true;st.textContent='Sending...';
 try{const r=await fetch('/api/inquiries',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.fromEntries(new FormData(f)))});
  const j=await r.json();
  if(r.ok){f.reset();st.textContent='Thank you. We received your request and will reply soon.';}
  else{st.textContent=j.error||'Could not send. Please try again.';}
 }catch(x){st.textContent='Could not send. Please try again.';}
 b.disabled=false;});
</script>'''

for fn,(t,d,_,body,act) in pages.items():
    open(os.path.join(OUT,fn),"w").write(shell(fn,t,d,body,act))
print("built", ", ".join(pages))
