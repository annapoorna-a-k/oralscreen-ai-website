"""OralScreen AI - project website (documentation portal).

Run locally:  streamlit run app.py
Edit the CONFIG block below to update team details, links and demo videos.
"""
import base64
from pathlib import Path

import streamlit as st

# ============================================================================ CONFIG (edit me)
PROJECT_TITLE = "OralScreen AI"
PROJECT_SUBTITLE = "Explainable oral cancer screening from intra-oral photographs and patient metadata"
GITHUB_URL = "https://github.com/annapoorna-a-k/Oral-Cancer-Detection-and-Multiclass-Classification"
RELEASE_URL = GITHUB_URL + "/releases/tag/v1.0"
LIVE_APP_URL = "https://oralscreen-ai-3nloatzwnkaypoqubwkfpy.streamlit.app/"
DATASET_URL = "https://zenodo.org/records/10664056"
LAB = ("Vision, Language and Intelligent Learning (VLIL)",
       "https://www.amrita.edu/research/thematic-areas/aiml/artificialintelligence/")
INSTITUTION = "Amrita Vishwa Vidyapeetham, Coimbatore"
PROGRAMME = "M.Tech in Artificial Intelligence"

TEAM = [
    {"name": "Annapoorna A K", "role": "M.Tech student, Artificial Intelligence",
     "detail": "School of Computing, Amrita Vishwa Vidyapeetham, Coimbatore", "photo": "student_annapoorna.jpg"},
    {"name": "Dr. Swapna T. R.", "role": "Project guide",
     "detail": "Associate Professor, School of Computing, Amrita Vishwa Vidyapeetham, Coimbatore", "photo": "guide_swapna.jpg"},
]

# Demonstration videos: YouTube / Google Drive / direct .mp4 links, or put .mp4 files in assets/videos/
DEMO_VIDEOS = [
    # {"title": "Walkthrough of the screening app", "url": "https://www.youtube.com/watch?v=..."},
]
# ============================================================================

HERE = Path(__file__).parent
ASSETS = HERE / "assets"

st.set_page_config(page_title=f"{PROJECT_TITLE} - Project", page_icon=str(ASSETS / "logo.png"),
                   layout="wide", initial_sidebar_state="collapsed")


def img_b64(name):
    return base64.b64encode((ASSETS / name).read_bytes()).decode()


def figure(name, caption=None):
    st.image(str(ASSETS / name), use_container_width=True)
    if caption:
        st.markdown(f"<p class='cap'>{caption}</p>", unsafe_allow_html=True)


def figure_c(name, caption=None, width=0.7):
    pad = (1 - width) / 2
    _, mid, _ = st.columns([pad, width, pad])
    with mid:
        figure(name, caption)


def section(anchor, eyebrow, title, lead=None):
    st.markdown(f"<div id='{anchor}' class='anchor'></div><h2 class='h2'>{title}</h2>"
                + (f"<p class='lead'>{lead}</p>" if lead else ""), unsafe_allow_html=True)


def cards(items, cols=3, cls="card"):
    html = f"<div class='grid g{cols}'>"
    for it in items:
        icon = f"<div class='ic'>{it['icon']}</div>" if it.get("icon") else ""
        html += f"<div class='{cls}'>{icon}<h4>{it['title']}</h4><p>{it['text']}</p></div>"
    st.markdown(html + "</div>", unsafe_allow_html=True)


def divider():
    st.markdown("<div class='sep'></div>", unsafe_allow_html=True)


# ============================================================================ STYLE
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap');
:root{--navy:#0F2A44;--ink:#14253A;--muted:#5A6B80;--line:#DCE4EE;--card:#FFFFFF;--bg:#F6F8FB;
      --accent:#C8553D;--blue:#1E5BB8;--soft:#EAF0F7;--good:#2E7D5B;
      --kp:#EEF4FB;--hl:#FFF4EF;--note:#FFF8E6;--notetx:#5E4B12;}
html, body, [class*="css"], .stMarkdown, p, li {font-family:'Inter',sans-serif;}
.stApp{background:var(--bg);}
header[data-testid="stHeader"]{background:transparent;height:0;}
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"]{visibility:hidden;}
.block-container{max-width:1180px;padding-top:1.2rem;padding-bottom:3rem;}
.anchor{position:relative;top:-80px;}

/* nav */
.nav{display:flex;align-items:center;justify-content:space-between;gap:1rem;
     background:var(--card);border:1px solid var(--line);
     border-radius:16px;padding:.6rem 1rem;margin-bottom:0;box-shadow:0 4px 18px rgba(15,42,68,.06);}
.brand{white-space:nowrap;display:flex;align-items:center;gap:.6rem;font-weight:800;color:var(--navy);font-size:1.05rem;}
.brand img{width:34px;height:34px;border-radius:9px;}
.links{display:flex;flex-wrap:wrap;gap:.15rem;}
.links a{color:var(--ink)!important;text-decoration:none!important;font-size:.86rem;font-weight:500;padding:.38rem .5rem;border-radius:8px;}
.links a:hover{background:var(--soft);}
.links a.gh{background:#1E5BB8;color:#fff!important;}

/* hero */
.hero{display:grid;grid-template-columns:1.15fr 1fr;gap:2rem;align-items:center;
      background:linear-gradient(135deg,#0F2A44 0%,#1B3F66 60%,#24507E 100%);border-radius:24px;
      padding:2.6rem 2.6rem;color:#fff;box-shadow:0 18px 40px rgba(15,42,68,.18);}
.pill{display:inline-block;border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:.28rem .8rem;font-size:.78rem;
      letter-spacing:.02em;color:#DCE8F6;margin-bottom:1rem;}
.hero h1{font-family:'Fraunces',serif!important;font-size:3.1rem!important;line-height:1.05!important;margin:0 0 .8rem 0;padding:0!important;color:#fff!important;}
.hero h1 span{color:#F2A58F!important;}
.hero p.sub{font-size:1.08rem;line-height:1.6;color:#D6E2F0;margin-bottom:1.5rem;}
.btns{display:flex;flex-wrap:wrap;gap:.6rem;}
.btn{display:inline-block;padding:.7rem 1.15rem;border-radius:12px;font-weight:600;font-size:.92rem;text-decoration:none!important;}
.btn.p{background:#fff;color:#0F2A44!important;}
.btn.s{border:1px solid rgba(255,255,255,.45);color:#fff!important;}
.hero img{width:100%;border-radius:18px;box-shadow:0 12px 30px rgba(0,0,0,.25);}

/* stats */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin:1.3rem 0 .4rem 0;}
.stat{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:1.1rem 1.2rem;}
.stat b{display:block;font-size:1.9rem;font-weight:800;color:var(--navy);line-height:1.1;}
.stat span{font-size:.86rem;color:var(--muted);}

/* sections */
.eyebrow{color:var(--accent);font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:.76rem;margin:0 0 .3rem 0;}
.h2{font-family:'Fraunces',serif;color:var(--navy)!important;font-size:2.05rem;margin:0 0 .5rem 0;line-height:1.15;}
.lead{color:var(--muted);font-size:1.03rem;line-height:1.7;max-width:860px;margin-bottom:1.3rem;}
.sep{height:1px;background:var(--line);margin:3rem 0 2.4rem 0;}
.cap{text-align:center;color:var(--muted);font-size:.86rem;margin-top:.3rem;}
h3.h3{color:var(--navy)!important;font-size:1.2rem;margin:1.6rem 0 .6rem 0;font-weight:700;}

.grid{display:grid;gap:1rem;margin:.4rem 0 1rem 0;}
.g2{grid-template-columns:repeat(2,1fr);} .g3{grid-template-columns:repeat(3,1fr);} .g4{grid-template-columns:repeat(4,1fr);}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:1.2rem 1.25rem;}
.card h4{margin:.2rem 0 .4rem 0;color:var(--navy);font-size:1.02rem;}
.card p{margin:0;color:var(--muted);font-size:.92rem;line-height:1.6;}
.ic{width:38px;height:38px;border-radius:10px;background:var(--soft);display:flex;align-items:center;justify-content:center;font-size:1.15rem;margin-bottom:.5rem;}
.card.obj{border-left:4px solid var(--accent);}
.card.future{border-top:4px solid var(--blue);}

.problem{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--accent);border-radius:16px;
         padding:1.4rem 1.5rem;font-size:1.02rem;line-height:1.75;color:var(--ink);}

/* method steps */
.steps{display:grid;grid-template-columns:repeat(5,1fr);gap:.7rem;margin:.6rem 0 1.4rem 0;}
.step{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1rem;position:relative;}
.step .n{display:inline-flex;width:28px;height:28px;border-radius:50%;background:#1E5BB8;color:#fff;font-weight:700;
         font-size:.85rem;align-items:center;justify-content:center;margin-bottom:.45rem;}
.step h4{margin:0 0 .3rem 0;font-size:.95rem;color:var(--navy);}
.step p{margin:0;font-size:.84rem;color:var(--muted);line-height:1.5;}

/* step-by-step explanation */
.sx{display:flex;gap:1rem;align-items:flex-start;margin:1.6rem 0 .8rem 0;}
.sxn{flex:0 0 36px;height:36px;border-radius:50%;background:var(--accent);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;}
.sx h4{margin:.25rem 0 .35rem 0;color:var(--navy);font-size:1.12rem;}
.sx p{margin:0;color:var(--ink);font-size:.98rem;line-height:1.7;max-width:980px;}
.kp{background:var(--kp);border-left:4px solid var(--blue);border-radius:10px;padding:.85rem 1rem;color:var(--ink);font-size:.93rem;line-height:1.6;margin:.6rem 0 1rem 0;}
/* table */
table.t{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;font-size:.92rem;}
table.t th{background:var(--soft);color:var(--navy);text-align:left;padding:.65rem .8rem;font-weight:700;}
table.t td{padding:.6rem .8rem;border-top:1px solid var(--line);color:var(--ink);}
table.t tr.best td{background:var(--hl);font-weight:700;}

/* timeline */
.tl{position:relative;margin:.6rem 0 0 .4rem;padding-left:1.6rem;border-left:3px solid var(--line);}
.tli{position:relative;margin-bottom:1.1rem;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:.9rem 1.1rem;}
.tli:before{content:"";position:absolute;left:-2.15rem;top:1.05rem;width:16px;height:16px;border-radius:50%;
            background:var(--good);border:3px solid var(--bg);}
.tli .when{font-size:.78rem;font-weight:700;color:var(--accent);letter-spacing:.06em;text-transform:uppercase;}
.tli h4{margin:.15rem 0 .25rem 0;color:var(--navy);font-size:1rem;}
.tli p{margin:0;color:var(--muted);font-size:.9rem;line-height:1.55;}
.chip{display:inline-block;background:var(--soft);color:var(--good);font-weight:700;font-size:.72rem;border-radius:999px;padding:.15rem .55rem;margin-left:.4rem;vertical-align:middle;}

/* team */
.person{min-height:350px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:1.4rem;text-align:center;}
.avatar{width:66px;height:66px;border-radius:50%;margin:0 auto .7rem auto;background:linear-gradient(135deg,#1B3F66,#C8553D);
        color:#fff;font-weight:800;font-size:1.4rem;display:flex;align-items:center;justify-content:center;}
.person h4{margin:0;color:var(--navy);} .person .r{color:var(--accent);font-weight:600;font-size:.85rem;margin:.2rem 0 .4rem 0;}
.person p{color:var(--muted);font-size:.88rem;margin:0;}

/* doc links */
a.doc{display:block;text-decoration:none!important;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:1.1rem 1.2rem;transition:.15s;}
a.doc:hover{border-color:var(--blue);box-shadow:0 6px 18px rgba(30,91,184,.12);transform:translateY(-2px);}
a.doc h4{margin:0 0 .3rem 0;color:var(--navy);font-size:1rem;} a.doc p{margin:0;color:var(--muted);font-size:.88rem;}
a.doc span{color:var(--blue);font-size:.82rem;font-weight:600;}

.note{background:var(--note);border:1px solid var(--line);border-radius:14px;padding:1rem 1.2rem;color:var(--notetx);font-size:.92rem;line-height:1.6;}
.foot{margin-top:3rem;padding:1.6rem;border-radius:18px;background:#0F2A44;color:#C9D7E8;font-size:.88rem;text-align:center;}
.foot a{color:#fff!important;}

[data-testid="stImage"] img{border-radius:14px;border:1px solid var(--line);background:#fff;}
[data-testid="stTabs"] button p{font-weight:600;}

@media (max-width: 900px){
 .hero{grid-template-columns:1fr;padding:1.6rem;} .hero h1{font-size:2.2rem;}
 .stats,.g3,.g4,.steps{grid-template-columns:repeat(2,1fr);} .g2{grid-template-columns:1fr;}
 .links{display:none;}
}
.person img{width:120px;height:120px;border-radius:50%;object-fit:cover;margin:0 auto .8rem auto;display:block;border:3px solid var(--line);}
.tag{display:inline-block;margin-top:.7rem;padding:.3rem .7rem;border-radius:999px;background:var(--soft);font-size:.78rem;font-weight:600;}
.tag a{color:var(--blue)!important;text-decoration:none!important;}
.anchor{display:block;}
</style>
""", unsafe_allow_html=True)

# ============================================================================ NAV
nav_l, nav_r = st.columns([0.87, 0.13], vertical_alignment="center")
with nav_l:
    st.markdown(f"""
<div class="nav">
  <div class="brand"><img src="data:image/png;base64,{img_b64('logo.png')}">{PROJECT_TITLE}</div>
  <div class="links">
    <a href="#problem">Problem</a><a href="#objectives">Objectives</a><a href="#methodology">Methodology</a>
    <a href="#results">Results</a><a href="#explainability">Explainability</a><a href="#demo">Demo</a>
    <a href="#progress">Progress</a><a href="#documentation">Docs</a><a href="#team">Team</a>
  </div>
</div>
""", unsafe_allow_html=True)
with nav_r:
    dark = st.toggle("Dark mode", key="dark")

if dark:
    st.markdown("""<style>
:root{--navy:#E4ECF7;--ink:#D5DFEB;--muted:#9AABC0;--line:#22344B;--card:#122133;--bg:#0A1420;
      --accent:#EE8E76;--blue:#78A9F2;--soft:#1A2B42;--good:#5CC08F;--kp:#13263D;--hl:#2A2018;--note:#2A2414;--notetx:#E8D9A8;}
.stApp, [data-testid="stAppViewContainer"]{background:var(--bg)!important;}
.stMarkdown p, .stMarkdown li, .stMarkdown strong, .stMarkdown b{color:var(--ink);}
[data-testid="stTabs"] button p{color:var(--ink)!important;}
[data-testid="stTabs"] [aria-selected="true"] p{color:var(--accent)!important;}
[data-testid="stExpander"] details{background:var(--card);border-color:var(--line)!important;}
[data-testid="stExpander"] summary p, [data-testid="stExpander"] summary svg{color:var(--ink)!important;fill:var(--ink);}
[data-testid="stWidgetLabel"] p, label p{color:var(--ink)!important;}
[data-testid="stCode"] pre, pre{background:#0F1C2C!important;}
pre code, pre code span{color:#D5DFEB!important;}
.stMarkdown a{color:#8DB8F5!important;}
</style>""", unsafe_allow_html=True)

# ============================================================================ HERO
st.markdown(f"""
<div class="hero">
  <div>
    <span class="pill">{PROGRAMME} &middot; {INSTITUTION}</span>
    <h1>{PROJECT_TITLE}</h1>
    <p class="sub">{PROJECT_SUBTITLE}. The system segments the oral cavity in a clinical photograph, classifies it as
    suspicious (OPMD or oral cancer) or not suspicious, explains the decision with Grad-CAM and SHAP, and generates a
    plain-language report with next steps.</p>
    <div class="btns">
      <a class="btn p" href="{LIVE_APP_URL}" target="_blank">Open the screening app</a>
      <a class="btn s" href="{GITHUB_URL}" target="_blank">GitHub repository</a>
      <a class="btn s" href="{DATASET_URL}" target="_blank">Dataset</a>
    </div>
  </div>
  <div><img src="data:image/jpeg;base64,{img_b64('banner.jpg')}"></div>
</div>
<div class="stats">
  <div class="stat"><b>3,000</b><span>intra-oral photos from 714 patients</span></div>
  <div class="stat"><b>0.943</b><span>Dice score of the oral-cavity segmentation</span></div>
  <div class="stat"><b>94.6%</b><span>of oral cancer images flagged as suspicious (test)</span></div>
  <div class="stat"><b>0.854</b><span>AUC of the final image + metadata model (test)</span></div>
</div>
""", unsafe_allow_html=True)

divider()

# ============================================================================ PROBLEM
section("problem", "", "Problem Statement")
c1, c2 = st.columns([1.25, 1], gap="large")
with c1:
    st.markdown("""
<div class="problem">
Oral cancer is among the most common cancers in India, driven largely by tobacco and <b>betel quid</b> use.
Most cases are found late, when treatment is harder and survival is lower, because <b>specialist examination is
scarce</b> outside cities. Many cancers are preceded by visible <b>oral potentially malignant disorders (OPMD)</b>
such as leukoplakia, which can be spotted early.<br><br>
The challenge is to build a <b>low-cost, explainable screening aid</b> that works from an ordinary intra-oral
photograph and a few patient details, runs on a normal computer, tells the user <i>why</i> it flagged a case,
and guides them to the right next step, without claiming to make a diagnosis.
</div>""", unsafe_allow_html=True)
with c2:
    cards([
        {"title": "Noisy photos", "text": "Lips, teeth, skin and background distract a classifier from the lesion."},
        {"title": "Severe imbalance", "text": "Only 76 training images of oral cancer (3.9%) against 884 OPMD."},
        {"title": "Black-box models", "text": "Clinicians and patients need to see what the model looked at."},
    ], cols=1)

divider()

# ============================================================================ OBJECTIVES
section("objectives", "", "Objectives")
cards([
    {"title": "O1 &middot; Oral-cavity segmentation", "text": "Locate and crop the oral cavity with a lightweight model so the classifier sees only the relevant region."},
    {"title": "O2 &middot; Handle class imbalance", "text": "Use patient-level splitting, augmentation and a clinically meaningful label grouping to cope with very few oral cancer images."},
    {"title": "O3 &middot; Image + metadata classification", "text": "Combine a CNN image classifier with patient risk factors (age, sex, smoking, alcohol, betel quid) for better screening."},
    {"title": "O4 &middot; Explainability", "text": "Explain every prediction with Grad-CAM heatmaps and SHAP risk-factor contributions."},
    {"title": "O5 &middot; Patient-friendly report", "text": "Turn the result into a safe, plain-language report with next steps and tobacco-cessation advice using a fine-tuned LLM."},
    {"title": "O6 &middot; Usable application", "text": "Deliver the full pipeline as a simple web application that runs on a standard CPU."},
], cols=3, cls="card obj")

divider()

# ============================================================================ METHODOLOGY
section("methodology", "", "Methodology",
        "The pipeline has five stages. Segmentation removes background clutter, a compact CNN reads the image, "
        "XGBoost fuses it with patient risk factors, and two explanation methods plus a guarded language model "
        "make the output understandable.")
st.markdown("""
<div class="steps">
 <div class="step"><span class="n">1</span><h4>Segment</h4><p>Mobile U-Net with adapters finds the oral cavity (0.29 M params).</p></div>
 <div class="step"><span class="n">2</span><h4>Classify image</h4><p>EfficientNet-B0 at 384 px gives p(OPMD + OCA).</p></div>
 <div class="step"><span class="n">3</span><h4>Fuse metadata</h4><p>XGBoost stacks the image probability with 9 encoded risk factors.</p></div>
 <div class="step"><span class="n">4</span><h4>Explain</h4><p>Grad-CAM shows where it looked; SHAP shows which habits mattered.</p></div>
 <div class="step"><span class="n">5</span><h4>Report</h4><p>Template + Qwen2.5-1.5B (LoRA) rewrite, checked by a safety validator.</p></div>
</div>""", unsafe_allow_html=True)
figure("system_architecture.png", "Overall system architecture")

def step(n, title, text):
    st.markdown(f"<div class='sx'><span class='sxn'>{n}</span><div><h4>{title}</h4><p>{text}</p></div></div>",
                unsafe_allow_html=True)


def keypoint(text):
    st.markdown(f"<div class='kp'>{text}</div>", unsafe_allow_html=True)


t1, t2, t3, t4 = st.tabs(["1 · Dataset & split", "2 · Segmentation", "3 · Classification & fusion", "4 · Report generation"])

# ---------------------------------------------------------------- TAB 1
with t1:
    step(1, "The dataset",
         f"We used the public <a href='{DATASET_URL}' target='_blank'>Zenodo oral-cavity dataset</a> (Piyarathne <i>et al.</i>): <b>3,000 intra-oral photographs from "
         "714 patients</b>, each labelled as <b>Healthy, Benign, OPMD</b> (potentially malignant disorder) or <b>OCA</b> "
         "(oral cancer). Every photo also has hand-drawn outlines of the oral cavity and of any lesion, and each patient has "
         "metadata: age, sex, smoking, alcohol and betel quid chewing.")
    a, b = st.columns([1.1, 1], gap="large")
    with a: figure("dataset_four_classes.jpg", "One example from each of the four categories")
    with b:
        st.markdown("""<table class="t"><tr><th>Category</th><th>What it means</th></tr>
        <tr><td>Healthy</td><td>Normal oral mucosa</td></tr>
        <tr><td>Benign</td><td>Non-cancerous lesion (e.g. ulcer, fibroma)</td></tr>
        <tr><td>OPMD</td><td>Lesion that may turn cancerous (e.g. leukoplakia)</td></tr>
        <tr><td>OCA</td><td>Oral cancer (squamous cell carcinoma)</td></tr></table>""", unsafe_allow_html=True)
        keypoint("The classes are very unequal: OPMD is about 46% of the images, while oral cancer is only about 4%.")

    step(2, "Understanding the patient data",
         "Before modelling, the metadata was explored at <b>patient level</b> (one row per person, not per photo) to see how "
         "each habit relates to cancer. Betel quid chewing shows the clearest link: cancer is about twice as common among "
         "chewers. These five attributes later become the metadata input of the model.")
    a, b = st.columns([1.1, 1], gap="large")
    with a: figure("metadata_vs_cancer.png", "Cancer vs non-cancer patients by gender, smoking, betel quid and alcohol")
    with b:
        keypoint("Age is scaled to 0–1 and sex and the three habits are one-hot encoded, giving a "
                 "<b>9-number metadata vector</b> for every patient.")

    step(3, "Patient-level split",
         "Most patients have several photos. If photos of the same person ended up in both training and test sets, the model "
         "could 'recognise the patient' instead of the disease and the results would look better than they really are. So the "
         "data was split <b>by patient</b> using stratified group k-fold (70 / 15 / 15): every patient's photos stay together in "
         "one split, and each split keeps similar class proportions.")
    a, b = st.columns([1.2, 1], gap="large")
    with a: figure("patient_split.png", "Share of patients and images in each split")
    with b:
        st.markdown("""<table class="t"><tr><th>Split</th><th>Patients</th><th>Images</th></tr>
        <tr><td>Train</td><td>476</td><td>1,933</td></tr>
        <tr><td>Validation</td><td>119</td><td>517</td></tr>
        <tr><td>Test</td><td>119</td><td>550</td></tr></table>""", unsafe_allow_html=True)
        keypoint("No patient appears in more than one split, so the test results reflect performance on <b>unseen patients</b>.")

# ---------------------------------------------------------------- TAB 2
with t2:
    step(1, "Why segment first?",
         "A raw mouth photo also contains lips, teeth, skin, beard and background. These can distract a classifier or even "
         "become shortcuts. The first stage therefore finds the <b>oral cavity</b> and crops the photo to it, so the classifier "
         "only looks at the region where lesions occur.")
    step(2, "Creating the training masks",
         "The dataset gives the oral cavity as a polygon outline. Each outline was filled in to make a <b>black-and-white mask</b> "
         "(white = oral cavity). This gave 2,999 image–mask pairs (one photo had no oral-cavity outline), split 80 / 20 for "
         "training and validation.")
    figure_c("annotation_mask.jpg", "Original photo → outlines (green: oral cavity, yellow: lesion) → binary mask used for training")

    step(3, "Comparing three segmentation models",
         "Three models were trained the same way (256 × 256 images, 25 epochs, BCE + Dice loss): <b>U-Net with a ResNet34 "
         "encoder</b>, <b>DeepLabV3+</b> and a lightweight <b>Mobile U-Net</b> built from depthwise-separable convolutions. "
         "Quality was measured with the <b>Dice score</b> (overlap between predicted and true mask; 1.0 = perfect).")
    a, b = st.columns([1, 1.1], gap="large")
    with a:
        st.markdown("""<table class="t"><tr><th>Model</th><th>Params</th><th>Size</th><th>Val Dice</th></tr>
        <tr><td>U-Net + ResNet34</td><td>24.37 M</td><td>292.9 MB</td><td>0.9530</td></tr>
        <tr><td>DeepLabV3+</td><td>26.73 M</td><td>321.3 MB</td><td>0.9450</td></tr>
        <tr class="best"><td>Mobile U-Net</td><td>0.24 M</td><td>3.1 MB</td><td>0.9296</td></tr></table>""",
                    unsafe_allow_html=True)
    with b:
        keypoint("Mobile U-Net was chosen: it is about <b>100× smaller</b> yet only ~2 Dice points lower. Since the mask is "
                 "only used to crop the oral cavity, this small gap barely changes the crop, and the tiny model runs fast on a CPU.")

    step(4, "Tuning and fine-tuning Mobile U-Net",
         "<b>Phase 1: hyperparameters:</b> learning rate, batch size, dropout and weight decay were varied; a low learning "
         "rate (1e-5) with batch size 16 worked best (Dice 0.9422).<br><b>Phase 2: fine-tuning strategy:</b> four ways of "
         "re-training were compared: head only, top layers, the full network, and <b>adapters</b> (small extra layers added "
         "while the original network stays frozen). Adapters gave the best Dice (<b>0.9428</b>, IoU 0.8921) while training only "
         "<b>18.8%</b> of the parameters.")
    a, b = st.columns([1.15, 1], gap="large")
    with a: figure("segmentation_selection.png", "(a) model size, (b) hyperparameter tuning, (c) fine-tuning strategies, (d) parameters trained")
    with b: figure("mobile_unet_architecture.png", "Final Mobile U-Net: encoder, bottleneck and decoder with adapters after every block")

    step(5, "Producing the crops",
         "The final model was run on all 3,000 photos. Each predicted mask was thresholded, the background set to black, and "
         "the image cropped to the mask's bounding box. These <b>segmented oral-cavity crops</b> are the input to every "
         "classification experiment.")
    figure_c("segmentation_examples.jpg", "Input photo → predicted mask → segmented oral cavity", 0.6)

# ---------------------------------------------------------------- TAB 3
with t3:
    step(1, "Choosing an image backbone (four classes)",
         "Four lightweight ImageNet-pretrained CNNs were fine-tuned on the crops to predict all four classes: EfficientNet-B0, "
         "EfficientNetV2-B0, MobileNetV2 and MobileNetV3-Small. <b>EfficientNet-B0</b> was best (test accuracy 0.580, "
         "macro-F1 0.510) and was tuned further in five stages (data and loss weighting, dropout and weight decay, optimiser "
         "and batch size, classifier head, final run).")
    step(2, "Why switch to two classes",
         "Even after tuning, the four-class model reached only 0.56 accuracy and caught just <b>27% of oral cancer</b> images, "
         "because there were only 76 OCA training photos and Healthy/Benign and OPMD/OCA look alike. For screening, the real "
         "question is simply <b>\"does this person need a specialist?\"</b>, so the labels were grouped into "
         "<b>not suspicious</b> (Healthy + Benign) and <b>suspicious</b> (OPMD + OCA). This also balanced the classes "
         "(973 vs 960 training images).")
    figure_c("classification_results.png", "(a) four-class per-class results, (b) four-class vs final binary model, (c) binary results with metadata at 224 px")

    step(3, "Exploring alternatives",
         "Two other directions were tested: <b>attention models</b> (Squeeze-and-Excitation, a CNN–ViT hybrid and axial "
         "attention) and a <b>YOLO26</b> pipeline that first detects the lesion, crops it and then classifies it. Neither beat "
         "the plain EfficientNet-B0 approach consistently, and YOLO missed the lesion in about 23% of images.")

    step(4, "Adding patient metadata",
         "The image model gives a probability that the photo is suspicious. The 9-number metadata vector was combined with it "
         "in several ways: <b>early fusion</b> inside the network (concatenation, FiLM) and <b>late fusion</b> of predictions "
         "(averaging, weighted averaging, logistic-regression and XGBoost stacking). The best was <b>L4: XGBoost stacking</b>: "
         "the image probability and the nine metadata features are fed together into an XGBoost classifier, trained on the "
         "validation set to avoid leakage.")
    a, b = st.columns([1, 1.4], gap="large")
    with a: figure("efficientnet_xgboost_fusion.png", "EfficientNet-B0 probability + metadata → XGBoost → prediction")
    with b:
        keypoint("Why XGBoost on raw features works better than averaging two probabilities: it can learn interactions, e.g. "
                 "a medium image score matters more for a betel quid chewer.")
        step(5, "Higher resolution",
             "Finally the input size was raised from 224 to <b>384 pixels</b> (with AdamW weight decay 0.05 to limit "
             "overfitting) so finer lesion detail is kept. This helped EfficientNet-B0 most: test MCC rose from 0.548 to "
             "<b>0.585</b> for the fused model.")
        figure("resolution_effect.png", "Test MCC at 224 px vs 384 px")
    keypoint("<b>Final model:</b> segmented crop → EfficientNet-B0 (384 px) → probability + 9 metadata features → XGBoost "
             "stacking → suspicious / not suspicious. Test accuracy 0.785, AUC 0.854, 94.6% of oral cancer images flagged.")

# ---------------------------------------------------------------- TAB 4
with t4:
    step(1, "Collect the facts",
         "After a prediction, code gathers a fixed set of facts: the result (suspicious / not suspicious), the model score, "
         "which habits <b>raised</b> or <b>lowered</b> the score according to SHAP, fixed next steps, lifestyle advice for "
         "each habit the person has, and the <b>National Tobacco Quitline (1800-11-2356)</b> for smokers and betel quid chewers.")
    step(2, "Write a template report",
         "These facts are placed into a report with four fixed headings: <b>Result</b>, <b>What influenced the result</b>, "
         "<b>What to do next</b> and <b>Reducing your risk</b>. This template is already correct and safe on its own.")
    step(3, "Rewrite it in plain language",
         "A small language model, <b>Qwen2.5-1.5B-Instruct</b>, rewrites the template in calm, simple English. It is told "
         "to use only the facts given, never to diagnose, and never to add numbers, diseases or treatments. The model never "
         "decides the result; it only rephrases it.")
    step(4, "Fine-tune the language model",
         "To make the small model reliable, a larger <b>Qwen2.5-7B</b> model first wrote example reports. Only those that "
         "passed the safety check were kept (99.7%), giving 598 training pairs. The 1.5B model was then fine-tuned on them "
         "with <b>LoRA</b> (rank 16, alpha 32), which trains only small adapter matrices so it still runs on a laptop.")
    step(5, "Check before showing",
         "Every rewritten report passes a <b>rule-based safety validator</b>: it is rejected if it contains diagnostic or "
         "alarming phrases (e.g. \"you have cancer\", \"good news\"), new numbers, or misses a heading, habit, next step or "
         "the quitline. A rejected report gets one retry; if it fails again, the template report is shown. The medical "
         "disclaimer is always added by code.")
    keypoint("Result: a report that a non-medical person can read, that always contains the right next steps, and that "
             "cannot claim a diagnosis.")

divider()

# ============================================================================ RESULTS
section("results", "", "Results",
        "Held-out, patient-level test set (550 images from 119 unseen patients).")
a, b = st.columns([1, 1.25], gap="large")
with a:
    st.markdown("""<table class="t">
    <tr><th>Model</th><th>Acc</th><th>AUC</th><th>Sens.</th><th>Spec.</th></tr>
    <tr><td>Metadata only (XGBoost)</td><td>0.711</td><td>0.800</td><td>0.650</td><td>0.783</td></tr>
    <tr><td>Image only (EfficientNet-B0)</td><td>0.733</td><td>0.813</td><td>0.633</td><td>0.850</td></tr>
    <tr><td>Early fusion (FiLM)</td><td>0.775</td><td>0.851</td><td>0.714</td><td>0.846</td></tr>
    <tr class="best"><td>Final: EfficientNet-B0 + XGBoost (L4)</td><td>0.785</td><td>0.854</td><td>0.714</td><td>0.870</td></tr>
    </table>""", unsafe_allow_html=True)
    st.markdown("<h3 class='h3'>Per-class behaviour of the final model</h3>", unsafe_allow_html=True)
    st.markdown("""<div class="stats" style="grid-template-columns:repeat(2,1fr);margin-top:.4rem">
      <div class="stat"><b>94.6%</b><span>of oral cancer (OCA) images flagged as suspicious</span></div>
      <div class="stat"><b>68.1%</b><span>of OPMD images flagged as suspicious</span></div>
      <div class="stat"><b>91.2%</b><span>of healthy images correctly cleared</span></div>
      <div class="stat"><b>82.8%</b><span>of benign images correctly cleared</span></div></div>""", unsafe_allow_html=True)
with b:
    figure("final_results.png", "Test metrics of the final 384 px models")

divider()

# ============================================================================ EXPLAINABILITY
section("explainability", "", "Explainability",
        "Grad-CAM shows the image regions that drove the decision; SHAP splits each decision into the contribution "
        "of every patient factor.")
figure("gradcam.jpg", "Grad-CAM and Grad-CAM++ on a healthy and an oral cancer case (dashed line: annotated lesion)")
a, b = st.columns(2, gap="large")
with a:
    figure("localisation.png", "Grad-CAM hits the annotated lesion 2.2&times; more often than chance")
with b:
    figure("shap.png", "SHAP: betel quid chewing is the strongest patient factor")
cards([
    {"title": "Lesion focus", "text": "Hottest point inside the lesion in 47.8% of cases vs 21.5% by chance; Grad-CAM and Grad-CAM++ agree (r = 0.83)."},
    {"title": "Image + metadata", "text": "On average 59% of each decision comes from the photo and 41% from patient details."},
    {"title": "Risk factors", "text": "Betel quid and age push towards suspicious; smoking and alcohol have small effects in this dataset."},
], cols=3)

divider()

# ============================================================================ DEMO
section("demo", "", "Demonstration",
        "A Streamlit app runs the full pipeline on a laptop CPU: upload a photo, add optional details, and get the "
        "segmentation, result, heatmap, SHAP chart and report.")
a, b = st.columns([1.3, 1], gap="large")
with a:
    figure("app_home.png", "Home screen of the OralScreen AI app")
with b:
    videos = list(DEMO_VIDEOS) + [{"title": p.stem.replace("_", " ").title(), "file": p}
                                  for p in sorted((ASSETS / "videos").glob("*.mp4"))]
    if videos:
        for v in videos:
            st.markdown(f"<h3 class='h3'>{v['title']}</h3>", unsafe_allow_html=True)
            st.video(str(v["file"]) if "file" in v else v["url"])
    else:
        st.markdown("""<div class="note"><b>Demonstration video</b><br>
        A walkthrough video of the application: uploading a photo, entering patient details, and reading the
        segmentation, Grad-CAM heatmap, SHAP chart and generated report.</div>""", unsafe_allow_html=True)
    st.link_button("Open the screening app", LIVE_APP_URL, use_container_width=True)
    st.markdown("<h3 class='h3'>Run it yourself</h3>", unsafe_allow_html=True)
    st.code(f"git clone {GITHUB_URL}.git\ncd Oral-Cancer-Detection-and-Multiclass-Classification/app\n"
            "pip install -r requirements.txt\nstreamlit run app.py", language="bash")

with st.expander("What else was explored (not in the final model)"):
    a, b = st.columns([1.2, 1], gap="large")
    with a: figure("synthetic_data.jpg", "Synthetic OCA images from diffusion (top) and StarGAN (bottom)")
    with b:
        st.markdown("""
- **Synthetic data:** class-conditioned Stable Diffusion with LoRA and a four-domain StarGAN were trained to create
  extra oral cancer images. With only 76 real examples, neither produced clinically realistic lesions, so synthetic
  data was not used.
- **Attention models:** SE, an SE-ViT hybrid and axial attention did not beat the plain EfficientNet-B0 head on the
  test set.
- **YOLO26 detect-crop-classify:** reached test macro-F1 0.548 on four classes, but found lesions in only about 77%
  of images.
- **Lesion segmentation:** several Mobile U-Net variants were explored for direct lesion masks.
""")

divider()

# ============================================================================ PROGRESS
section("progress", "", "Project Progress")
steps = [
    ("July 2026", "Literature review & data understanding", "Review of oral cancer screening literature; metadata EDA of the Zenodo dataset."),
    ("August 2026", "Oral-cavity segmentation", "U-Net + ResNet34, DeepLabV3+ and Mobile U-Net trained and compared; patient-level train / val / test split."),
    ("September 2026", "Segmentation tuning, crops & backbones", "Mobile U-Net hyperparameter sweeps and adapter fine-tuning; lesion-segmentation experiments; crop generation; augmentation; four-class backbone comparison."),
    ("October 2026", "Classifier tuning & alternatives", "EfficientNet-B0 stage-wise tuning; attention models (SE, ViT, axial); YOLO26 detect-crop-classify; diffusion and StarGAN synthetic data."),
    ("November 2026", "Fusion, explainability, report & app", "Binary screening with metadata fusion (224 and 384 px); Grad-CAM and SHAP; Qwen LoRA report generator; Streamlit application; GitHub repository and documentation."),
]
st.markdown("<div class='tl'>" + "".join(
    f"<div class='tli'><span class='when'>{w}</span><span class='chip'>Completed</span><h4>{t}</h4><p>{d}</p></div>"
    for w, t, d in steps) + "</div>", unsafe_allow_html=True)

divider()

# ============================================================================ DOCUMENTATION
section("documentation", "", "Documentation")
docs = [
    ("GitHub repository", "Source code, models, notebooks and documentation.", GITHUB_URL),
    ("README", "Overview, architecture, results and references.", GITHUB_URL + "#readme"),
    ("Installation guide", "Set up and run the screening app locally.", GITHUB_URL + "/blob/main/INSTALL.md"),
    ("Notebooks (33)", "All experiments in pipeline order, from EDA to the LLM.", GITHUB_URL + "/tree/main/notebooks"),
    ("Application source", "Streamlit app, pipeline and report generator.", GITHUB_URL + "/tree/main/app"),
    ("Release v1.0", "Final project release with notes.", RELEASE_URL),
    ("Dataset (Zenodo)", "Oral cavity image dataset with annotations and patient metadata.", DATASET_URL),
    ("Live application", "The deployed screening app on Streamlit Community Cloud.", LIVE_APP_URL),
]
html = "<div class='grid g3'>"
for t, d, u in docs:
    html += f"<a class='doc' href='{u}' target='_blank'><h4>{t}</h4><p>{d}</p><span>Open</span></a>"
st.markdown(html + "</div>", unsafe_allow_html=True)
st.markdown("<h3 class='h3'>Technology stack</h3>", unsafe_allow_html=True)
cards([
    {"title": "Deep learning", "text": "PyTorch, timm, TensorFlow / Keras, ONNX Runtime"},
    {"title": "Machine learning", "text": "XGBoost, scikit-learn, SHAP"},
    {"title": "Language model", "text": "Qwen2.5-1.5B-Instruct, Hugging Face Transformers, PEFT (LoRA)"},
    {"title": "Application", "text": "Streamlit, OpenCV, Pillow; trained on Kaggle GPUs"},
], cols=4)

divider()

# ============================================================================ FUTURE WORK
section("future", "", "Future Improvements",
        "The main limitation is data: one public dataset with only 76 training images of oral cancer.")
cards([
    {"title": "Larger multi-centre dataset", "text": "Collect biopsy-confirmed photos of all four categories, with far more OCA and OPMD cases and richer habit details, from several hospitals and phones."},
    {"title": "External & clinical validation", "text": "Test on images from unseen hospitals and devices, then run prospective studies in real screening camps."},
    {"title": "Lesion-focused learning", "text": "Use the lesion annotations during training so the model attends to lesions more consistently."},
    {"title": "Sensitivity-first threshold", "text": "Tune the decision threshold so fewer suspicious cases are missed, accepting a few more referrals."},
    {"title": "Offline mobile app", "text": "Run the lightweight models fully on a smartphone for community health workers in rural areas."},
    {"title": "Report evaluation", "text": "Have dentists, oncologists and patients rate the generated reports for clarity, accuracy and usefulness."},
], cols=3, cls="card future")

divider()

# ============================================================================ TEAM
section("team", "", "Team")
cols = st.columns(len(TEAM), gap="large")
for col, p in zip(cols, TEAM):
    with col:
        st.markdown(f"<div class='person'><img src='data:image/jpeg;base64,{img_b64(p['photo'])}'>"
                    f"<h4>{p['name']}</h4><div class='r'>{p['role']}</div><p>{p['detail']}</p>"
                    f"<span class='tag'><a href='{LAB[1]}' target='_blank'>{LAB[0]}</a></span></div>",
                    unsafe_allow_html=True)

# ============================================================================ FOOTER
st.markdown(f"""
<div class="foot">
<b style="color:#fff">{PROJECT_TITLE}</b> &middot; research prototype for screening support, not a diagnostic tool.<br>
{PROGRAMME} &middot; {INSTITUTION}<br>
Dataset: <a href="{DATASET_URL}" target="_blank">Zenodo oral cavity dataset</a> (Piyarathne <i>et al.</i>) &middot;
Code: <a href="{GITHUB_URL}" target="_blank">GitHub</a> (MIT License) &middot; <a href="{LIVE_APP_URL}" target="_blank">Screening app</a>
</div>""", unsafe_allow_html=True)
