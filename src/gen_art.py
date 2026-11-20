#!/usr/bin/env python3
"""Generates original abstract SVG art into website/assets (no third-party imagery). Run: python3 gen_art.py"""
import os, math
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "website", "assets")
DEFS = '''<defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#d11a1a" stop-opacity=".85"/><stop offset=".5" stop-color="#8B0000" stop-opacity=".35"/><stop offset="1" stop-color="#8B0000" stop-opacity="0"/></radialGradient>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b0b0b"/><stop offset="1" stop-color="#2a1212"/></linearGradient>
<linearGradient id="r" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff5a5a" stop-opacity="0"/><stop offset=".5" stop-color="#ff5a5a"/><stop offset="1" stop-color="#ff5a5a" stop-opacity="0"/></linearGradient>
<linearGradient id="m" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8e8e8"/><stop offset="1" stop-color="#6b6b6b"/></linearGradient></defs>'''
def svg(w,h,body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">{DEFS}<rect width="{w}" height="{h}" fill="url(#bg)"/>{body}</svg>'
def dots(cx,cy,r,n,size=2,op=.5,col="#ff7a7a"):
    return "".join(f'<circle cx="{cx+r*math.cos(2*math.pi*i/n):.1f}" cy="{cy+r*math.sin(2*math.pi*i/n):.1f}" r="{size}" fill="{col}" opacity="{op}"/>' for i in range(n))
def rings(cx,cy,rs,col="#ff6a6a",op=.25,sw=1.2): return "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="{sw}"/>' for r in rs)
def w(name,s): open(os.path.join(A,name),"w").write(s)

# Hero: glowing platter (hard-drive disc) with arc and dotted rings, right-weighted
cx,cy=1180,430
hero = f'<circle cx="{cx}" cy="{cy}" r="520" fill="url(#g)"/>' + rings(cx,cy,[90,150,210,270,330,390],op=.22) + dots(cx,cy,450,90) + dots(cx,cy,510,120,1.6,.3)
hero += f'<circle cx="{cx}" cy="{cy}" r="280" fill="#141414" stroke="url(#m)" stroke-opacity=".5" stroke-width="2"/>' + rings(cx,cy,[110,150,190,230,260],col="#ffffff",op=.08,sw=1)
hero += f'<circle cx="{cx}" cy="{cy}" r="46" fill="#0b0b0b" stroke="#ff5a5a" stroke-opacity=".7" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="10" fill="#ff5a5a"/>'
hero += f'<path d="M{cx+330},{cy-250} A 420 420 0 0 1 {cx+360},{cy+210}" fill="none" stroke="#ff5a5a" stroke-width="3" stroke-opacity=".9"/><path d="M{cx-420},{cy+230} A 520 520 0 0 0 {cx+120},{cy+470}" fill="none" stroke="url(#r)" stroke-width="2"/>'
# tonearm
hero += f'<path d="M{cx+420},{cy-300} L{cx+90},{cy-40}" stroke="url(#m)" stroke-width="12" stroke-linecap="round" opacity=".8"/><circle cx="{cx+420}" cy="{cy-300}" r="22" fill="#1d1d1d" stroke="#8a8a8a" stroke-width="3"/>'
w("hero.svg", svg(1600,860,hero))

# Card art 640x360
def c(body): return svg(640,360,f'<circle cx="320" cy="180" r="300" fill="url(#g)" opacity=".7"/>'+body)
cards = {
 "lock": rings(320,180,[50,85,120,155],op=.3)+'<rect x="270" y="165" width="100" height="78" rx="12" fill="#161616" stroke="#ff5a5a" stroke-width="3"/><path d="M293 165v-24a27 27 0 0154 0v24" fill="none" stroke="url(#m)" stroke-width="9" stroke-linecap="round"/><circle cx="320" cy="203" r="9" fill="#ff5a5a"/>'+dots(320,180,190,40,2,.35),
 "truck": "".join(f'<path d="M{x},360 L{320+(x-320)*.18:.0f},120" stroke="#ff6a6a" stroke-opacity=".2"/>' for x in range(-200,900,90))+'<path d="M0 120H640" stroke="#ff6a6a" stroke-opacity=".35"/><rect x="200" y="150" width="170" height="88" rx="6" fill="#161616" stroke="url(#m)" stroke-width="3"/><path d="M370 178h46l30 34v26H370z" fill="#1d1d1d" stroke="url(#m)" stroke-width="3"/><circle cx="250" cy="246" r="17" fill="#0b0b0b" stroke="#ff5a5a" stroke-width="4"/><circle cx="330" cy="246" r="17" fill="#0b0b0b" stroke="#ff5a5a" stroke-width="4"/><circle cx="420" cy="246" r="17" fill="#0b0b0b" stroke="#ff5a5a" stroke-width="4"/><path d="M60 300H580" stroke="url(#r)" stroke-width="3"/>',
 "cycle": rings(320,180,[110,150],op=.18)+'<path d="M320 85a95 95 0 0188 60" fill="none" stroke="#ff5a5a" stroke-width="9" stroke-linecap="round"/><path d="M408 215a95 95 0 01-150 52" fill="none" stroke="url(#m)" stroke-width="9" stroke-linecap="round"/><path d="M232 232a95 95 0 0188-147" fill="none" stroke="#8B0000" stroke-width="9" stroke-linecap="round"/><path d="M408 145l16-30 14 36z" fill="#ff5a5a"/><circle cx="320" cy="180" r="14" fill="#ff5a5a"/>'+dots(320,180,200,48,2,.3),
 "doc": "".join(f'<rect x="{200+i*14}" y="{80+i*10}" width="190" height="220" rx="8" fill="#{["1a1a1a","202020","262626"][i]}" stroke="url(#m)" stroke-opacity=".{4+i*2}" stroke-width="2"/>' for i in range(3))+"".join(f'<rect x="{248}" y="{128+j*30}" width="{[110,140,90,120][j]}" height="8" rx="4" fill="{"#ff5a5a" if j==0 else "#8a8a8a"}" opacity=".{9 if j==0 else 6}"/>' for j in range(4))+'<circle cx="400" cy="250" r="26" fill="#161616" stroke="#ff5a5a" stroke-width="3"/><path d="M388 250l9 9 16-18" fill="none" stroke="#ff5a5a" stroke-width="4" stroke-linecap="round"/>',
 "dollar": "".join(f'<rect x="{190+i*60}" y="{250-h}" width="38" height="{h}" rx="5" fill="{"#ff5a5a" if i==4 else "url(#m)"}" opacity="{.95 if i==4 else .55}"/>' for i,h in enumerate([50,80,110,150,200]))+'<path d="M180 262H500" stroke="#8a8a8a" stroke-opacity=".5"/><path d="M200 220 L260 190 L320 160 L380 120 L440 70" fill="none" stroke="url(#r)" stroke-width="3"/>'+dots(440,70,24,10,2,.6),
 "bars": '<path d="M110 190H530" stroke="url(#r)" stroke-width="3"/>'+"".join(f'<circle cx="{150+i*113}" cy="190" r="{14 if i<3 else 20}" fill="#161616" stroke="{"#ff5a5a" if i>=3 else "#8a8a8a"}" stroke-width="3"/><path d="M{150+i*113} {190-(70 if i%2==0 else -70)}V190" stroke="#8a8a8a" stroke-opacity=".5"/><rect x="{150+i*113-34}" y="{(120-30) if i%2==0 else 260}" width="68" height="30" rx="6" fill="#1d1d1d" stroke="#ff5a5a" stroke-opacity=".5"/>' for i in range(4))+rings(320,180,[160],op=.15),
}
for k,v in cards.items(): w(f"card-{k}.svg", c(v))
print("art:", ", ".join(sorted(f for f in os.listdir(A) if f.endswith(".svg"))))
