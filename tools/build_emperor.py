"""Generates assets/emperor.svg. Edit PROVINCES and rerun: python3 tools/build_emperor.py"""
import math
from pathlib import Path

PROVINCES = [
    ("DATA", ["numpy", "pandas", "polars", "scipy", "statsmodels", "matplotlib", "seaborn", "plotly", "networkx"]),
    ("MACHINE LEARNING", ["scikit-learn", "xgboost", "lightgbm", "optuna", "shap", "joblib", "mlflow"]),
    ("DEEP LEARNING", ["pytorch", "torchvision", "tensorflow", "keras", "transformers", "peft", "open_clip", "onnxruntime"]),
    ("LLMs", ["anthropic", "openai", "tiktoken", "sentence-transformers", "whisper", "speechrecognition"]),
    ("AI AGENTS & RAG", ["langchain", "langgraph", "llama-index", "crewai", "autogen", "mcp", "claude-agent-sdk", "chromadb", "faiss", "pinecone"]),
    ("VISION", ["opencv", "pillow", "ultralytics", "mediapipe", "dlib", "pyzbar", "qrcode"]),
    ("SECURITY", ["scapy", "cryptography", "paramiko", "pwntools", "impacket", "python-nmap", "yara-python"]),
    ("GIS", ["geopandas", "shapely", "folium", "geopy", "osmnx", "rasterio"]),
    ("BACKEND", ["fastapi", "flask", "django", "pydantic", "sqlalchemy", "httpx", "requests", "psycopg", "pymongo", "bcrypt", "apscheduler", "python-telegram-bot"]),
    ("WEB & FRONTEND", ["streamlit", "gradio", "reflex", "nicegui", "flet", "jinja2", "beautifulsoup4", "selenium", "scrapy", "playwright"]),
    ("DATA ENGINEERING", ["pyspark", "airflow", "duckdb", "kafka-python"]),
    ("AUTOMATION & DOCS", ["pymupdf", "pypdf2", "reportlab", "fpdf", "pyserial", "pytest"]),
]
CORE = ["numpy", "pandas", "pytorch", "transformers", "langchain", "scikit-learn", "fastapi",
        "anthropic", "opencv", "geopandas", "scapy", "pyspark", "streamlit", "pydantic"]

W = 1200
GOLD, CY, GR = "#f5c451", "#22d3ee", "#34d399"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SERIF = "Georgia,'Times New Roman',serif"
X, LABEL_W, RIGHT = 540, 180, 1160
CHAR_W, LINE_H, GAP = 7.8, 20, 13


def esc(s):
    return s.replace("&", "&amp;")


def wrap(libs):
    max_w = RIGHT - (X + LABEL_W)
    lines, line = [], ""
    for lib in libs:
        t = f"{line} · {lib}" if line else lib
        if len(t) * CHAR_W > max_w:
            lines.append(line)
            line = lib
        else:
            line = t
    return lines + [line]


rows, y = [], 160
for name, libs in PROVINCES:
    lines = wrap(libs)
    rows.append((name, lines, y))
    y += LINE_H * len(lines) + GAP
H = y + 50
N = sum(len(l) for _, l in PROVINCES)
cx, cy = 270, H // 2
R1, R2, R3 = 222, 178, 140


def ring(id_, r):
    return f'<path id="{id_}" d="M {cx-r},{cy} a {r},{r} 0 1,1 {2*r},0 a {r},{r} 0 1,1 {-2*r},0" fill="none"/>'


def ring_text(cls, href, r, size, fill, text, extra=""):
    L = 2 * math.pi * r - 6
    return (f'<g class="{cls}"><text font-size="{size}" fill="{fill}" {extra}>'
            f'<textPath href="#{href}" textLength="{L:.0f}" lengthAdjust="spacingAndGlyphs">{esc(text)}</textPath></text></g>')


o = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#03060c"/><stop offset="1" stop-color="#0a1219"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe7a3"/><stop offset=".55" stop-color="{GOLD}"/><stop offset="1" stop-color="#b8862b"/></linearGradient>
<radialGradient id="halo"><stop offset="0" stop-color="{GOLD}" stop-opacity=".22"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="14"/></clipPath>
{ring("r1", R1)}{ring("r2", R2)}{ring("r3", R3)}
</defs>
<style>
.cw{{animation:spin 60s linear infinite;transform-origin:{cx}px {cy}px}}
.ccw{{animation:spin 40s linear infinite reverse;transform-origin:{cx}px {cy}px}}
.slow{{animation:spin 90s linear infinite;transform-origin:{cx}px {cy}px}}
.crown{{animation:float 4s ease-in-out infinite}}
.row{{animation:fade 1s ease-out both}}
.gem{{animation:pulse 2.4s ease-in-out infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
@keyframes fade{{from{{opacity:0;transform:translateX(12px)}}to{{opacity:1;transform:none}}}}
@keyframes pulse{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
</style>
<g clip-path="url(#frame)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<circle cx="{cx}" cy="{cy}" r="250" fill="url(#halo)"/>
<circle cx="{cx}" cy="{cy}" r="246" fill="none" stroke="{GOLD}" stroke-opacity=".35"/>
<circle cx="{cx}" cy="{cy}" r="200" fill="none" stroke="{CY}" stroke-opacity=".15"/>
<circle cx="{cx}" cy="{cy}" r="158" fill="none" stroke="{GR}" stroke-opacity=".15" stroke-dasharray="2 6"/>
<circle cx="{cx}" cy="{cy}" r="118" fill="none" stroke="{GOLD}" stroke-opacity=".3"/>''']
a = o.append
a(ring_text("slow", "r1", R1, 17, "url(#gold)", "THE EMPEROR OF PYTHON · " * 4,
            f'font-family="{SERIF}" font-weight="700" letter-spacing="3"'))
a(ring_text("ccw", "r2", R2, 13, CY, " · ".join(CORE) + " · ", f'font-family="{MONO}"'))
a(ring_text("cw", "r3", R3, 10, GR, " · ".join(p for p, _ in PROVINCES) + " · ",
            f'font-family="{MONO}" letter-spacing="1" fill-opacity=".85"'))
a(f'''<g class="crown" filter="url(#glow)">
<path d="M{cx-52},{cy-6} L{cx-60},{cy-58} L{cx-28},{cy-30} L{cx},{cy-72} L{cx+28},{cy-30} L{cx+60},{cy-58} L{cx+52},{cy-6} Z" fill="url(#gold)" stroke="#7a5714" stroke-width="1.5" stroke-linejoin="round"/>
<rect x="{cx-54}" y="{cy-8}" width="108" height="14" rx="3" fill="url(#gold)" stroke="#7a5714" stroke-width="1.5"/>
<circle class="gem" cx="{cx}" cy="{cy-1}" r="4" fill="{CY}"/><circle class="gem" cx="{cx-30}" cy="{cy-1}" r="3" fill="{GR}" style="animation-delay:-.8s"/><circle class="gem" cx="{cx+30}" cy="{cy-1}" r="3" fill="{GR}" style="animation-delay:-1.6s"/>
<circle cx="{cx-60}" cy="{cy-60}" r="4" fill="url(#gold)"/><circle cx="{cx}" cy="{cy-75}" r="5" fill="url(#gold)"/><circle cx="{cx+60}" cy="{cy-60}" r="4" fill="url(#gold)"/>
</g>
<text x="{cx}" y="{cy+56}" text-anchor="middle" font-family="{MONO}" font-size="44" font-weight="700" fill="{CY}" filter="url(#glow)">{N}</text>
<text x="{cx}" y="{cy+80}" text-anchor="middle" font-family="{MONO}" font-size="12" letter-spacing="3" fill="#8aa0ae">LIBRARIES</text>''')
a(f'<text x="{X}" y="74" font-family="{SERIF}" font-size="38" font-weight="700" letter-spacing="2" fill="url(#gold)" filter="url(#glow)">The Emperor of Python</text>')
a(f'<text x="{X}" y="106" font-family="{MONO}" font-size="15"><tspan fill="{GR}">&gt;&gt;&gt;</tspan>'
  f'<tspan fill="#e2f4f8"> import empire</tspan><tspan fill="#4b5d6b">   # {len(PROVINCES)} provinces, one language</tspan></text>')
a(f'<line x1="{X}" y1="126" x2="{RIGHT}" y2="126" stroke="{GOLD}" stroke-opacity=".3"/>')
for i, (name, lines, y) in enumerate(rows):
    a(f'<g class="row" style="animation-delay:{0.12*i+0.2:.2f}s">')
    a(f'<text x="{X}" y="{y}" font-family="{MONO}" font-size="11" font-weight="700" letter-spacing="1.5" fill="{GOLD}">{esc(name)}</text>')
    for k, ln in enumerate(lines):
        a(f'<text x="{X+LABEL_W}" y="{y+k*LINE_H}" font-family="{MONO}" font-size="13" fill="#c9d1d9">{esc(ln)}</text>')
    a('</g>')
a(f'''<text x="{X}" y="{H-22}" font-family="{MONO}" font-size="12" fill="#4b5d6b">&gt;&gt;&gt; empire.status()  # "still expanding"</text>
</g>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="none" stroke="{GOLD}" stroke-opacity=".3"/>
</svg>''')

out = Path(__file__).resolve().parent.parent / "assets" / "emperor.svg"
out.write_text("\n".join(o))
print(f"{N} libraries, {W}x{H} -> {out}")
