# =========================================================
# CUTANEXA AI
# FULL PROFESSIONAL APPLICATION
# =========================================================

import streamlit as st
from PIL import Image
import torch
import torch.nn as nn
from torchvision import transforms, models
import os

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CUTANEXA AI",
    page_icon="🩹",
    layout="wide"
)

# =========================================================
# MODEL
# =========================================================

classes = [
    "First Degree Burn",
    "Superficial Second Degree Burn",
    "Deep Second Degree Burn",
    "Third Degree Burn"
]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = models.mobilenet_v2(weights=None)

model.classifier[1] = nn.Linear(
    model.classifier[1].in_features,
    len(classes)
)

model.load_state_dict(
    torch.load(
        "burn_model.pth",
        map_location=device
    )
)

model = model.to(device)
model.eval()

# =========================================================
# TRANSFORM
# =========================================================

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"]{
    background:#07111f;
    color:white;
    font-family:'Segoe UI';
}

/* Hide streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#081120,#0f172a);
    border-right:1px solid #1e293b;
}

/* Titles */
.main-title{
    font-size:55px;
    font-weight:900;
    color:white;
}

.sub-title{
    color:#94a3b8;
    font-size:18px;
}

/* Cards */
.card{
    background:linear-gradient(135deg,#0f172a,#172554);
    padding:35px;
    border-radius:25px;
    margin-bottom:25px;
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0 0 25px rgba(0,255,255,0.08);
}

/* Prediction */
.prediction-box{
    background:linear-gradient(135deg,#1d4ed8,#2563eb);
    padding:35px;
    border-radius:25px;
    margin-top:20px;
    border:2px solid #38bdf8;
    box-shadow:0 0 30px rgba(56,189,248,0.25);
}

/* Information */
.info-card{
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:40px;
    border-radius:25px;
    margin-top:25px;
    line-height:2;
    border:1px solid rgba(255,255,255,0.08);
}

/* Warning */
.warning-box{
    background:linear-gradient(135deg,#7f1d1d,#dc2626);
    padding:30px;
    border-radius:25px;
    margin-bottom:25px;
    color:white;
}

/* Inputs */
.stTextInput input{
    background:#1e293b;
    color:white;
    border-radius:12px;
    border:1px solid #334155;
}

/* Buttons */
.stButton>button{
    background:linear-gradient(135deg,#06b6d4,#2563eb);
    color:white;
    border:none;
    border-radius:14px;
    padding:12px 25px;
    font-weight:bold;
    font-size:16px;
}

/* Select */
.stSelectbox div[data-baseweb="select"]{
    background:#1e293b;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOGIN STATE
# =========================================================

if "logged" not in st.session_state:
    st.session_state.logged = False

# =========================================================
# LOGIN PAGE
# =========================================================

if not st.session_state.logged:

    st.markdown("<br><br>", unsafe_allow_html=True)

    c1,c2,c3 = st.columns([1,2,1])

    with c2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if os.path.exists("assets/logo.png"):
            st.image("assets/logo.png", width=180)

        st.markdown("""
        <div class='main-title'>CUTANEXA AI</div>
        <div class='sub-title'>
        Visual analysis, dressing guidance and monitoring
        </div>
        <br>
        """, unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("LOGIN"):

            if username == "admin" and password == "admin":

                st.session_state.logged = True
                st.rerun()

            else:
                st.error("Wrong username or password")

        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=150)

    st.markdown("## Navigation")

    page = st.radio(
        "",
        [
            "Dashboard",
            "Prediction",
            "Assistant",
            "Information"
        ]
    )

    if st.button("Logout"):
        st.session_state.logged = False
        st.rerun()

# =========================================================
# WARNING
# =========================================================

warning_text = """
<div class='warning-box'>

<h1>⚠ Important Warning</h1>

This application provides general first-aid advice and indicative visual monitoring.

It does not replace professional evaluation and should never delay consultation in cases of:

<ul>
<li>severe pain</li>
<li>extensive burns</li>
<li>deep burns</li>
<li>fever</li>
<li>pus</li>
<li>rapid worsening</li>
</ul>

</div>
"""

# =========================================================
# COMPLETE INFORMATION
# =========================================================

burn_details = {

"First Degree Burn": """

<h1>First Degree Burn</h1>

<h2>Signs</h2>

<ul>
<li>redness</li>
<li>pain</li>
<li>dry skin</li>
<li>superficial injury</li>
</ul>

<h2>Rule of 20</h2>

<ul>
<li>20 cm from tap</li>
<li>20°C water</li>
<li>20 minutes cooling</li>
</ul>

<h2>What to do</h2>

<ol>
<li>Cool immediately with temperate water.</li>
<li>Protect skin gently.</li>
<li>Keep clean and dry.</li>
<li>Hydrate carefully.</li>
</ol>

<h2>Do NOT</h2>

<ul>
<li>apply ice</li>
<li>apply butter</li>
<li>apply oil</li>
<li>apply toothpaste</li>
</ul>

<h2>Monitor</h2>

<ul>
<li>pain increase</li>
<li>spreading redness</li>
<li>swelling</li>
</ul>

""",

"Superficial Second Degree Burn": """

<h1>Superficial Second Degree Burn</h1>

<h2>Possible Signs</h2>

<ul>
<li>blisters</li>
<li>pink moist skin</li>
<li>painful area</li>
<li>sensitive skin</li>
</ul>

<h2>Rule of 20</h2>

<ul>
<li>20 cm from tap</li>
<li>20°C water</li>
<li>20 minutes cooling</li>
</ul>

<h2>What to do</h2>

<ol>
<li>Cool with water immediately.</li>
<li>Remove rings and tight objects.</li>
<li>Protect the area.</li>
<li>Do not burst blisters.</li>
</ol>

<h2>Home Dressing Conditions</h2>

<ul>
<li>limited burn area</li>
<li>clean environment</li>
<li>sterile material available</li>
<li>pain remains tolerable</li>
</ul>

<h2>Required Materials</h2>

<ul>
<li>saline solution</li>
<li>sterile gauze</li>
<li>fatty gauze dressing</li>
<li>elastic bandage</li>
<li>sterile compresses</li>
</ul>

<h2>ZERALDA Dressing Protocol</h2>

<ol>
<li>Wash hands carefully.</li>
<li>Clean using saline solution.</li>
<li>Dry with sterile compresses.</li>
<li>Apply fatty gauze dressing.</li>
<li>Cover with sterile compresses.</li>
<li>Fix with elastic bandage.</li>
</ol>

<h2>Dressing Change</h2>

<ul>
<li>every half-day</li>
<li>earlier if wet</li>
<li>earlier if detached</li>
<li>earlier if painful</li>
</ul>

<h2>Monitor</h2>

<ul>
<li>fever</li>
<li>pus</li>
<li>bad smell</li>
<li>redness spread</li>
<li>pain worsening</li>
</ul>

""",

"Deep Second Degree Burn": """

<h1>Deep Second Degree Burn</h1>

<h2>Possible Signs</h2>

<ul>
<li>deep skin injury</li>
<li>pale skin</li>
<li>reduced sensitivity</li>
<li>high complication risk</li>
</ul>

<h2>What to do</h2>

<ol>
<li>Cool carefully with water.</li>
<li>Protect without rubbing.</li>
<li>Do not remove skin.</li>
<li>Seek rapid consultation.</li>
</ol>

<h2>Do NOT</h2>

<ul>
<li>burst blisters</li>
<li>remove skin</li>
<li>apply ointments without advice</li>
<li>apply toothpaste or oil</li>
</ul>

<h2>ZERALDA Protocol</h2>

<ul>
<li>saline cleaning</li>
<li>sterile compress drying</li>
<li>fatty gauze dressing</li>
<li>dry sterile compresses</li>
<li>elastic bandage</li>
<li>dressing change every half-day</li>
</ul>

""",

"Third Degree Burn": """

<h1>Third Degree Burn</h1>

<h2>Possible Signs</h2>

<ul>
<li>white or dark skin</li>
<li>deep tissue injury</li>
<li>possible absence of pain</li>
<li>destroyed skin layers</li>
</ul>

<h2>Emergency</h2>

<p>
Immediate evaluation required.
</p>

<h2>Do NOT</h2>

<ul>
<li>remove stuck clothes</li>
<li>apply ointments</li>
<li>apply toothpaste</li>
<li>apply oil</li>
<li>rub the injury</li>
</ul>

<h2>NO HOME DRESSING</h2>

<p>
Care must be performed by professionals.
</p>

""",

"Thermal Burn": """

<h1>Thermal Burn</h1>

<ul>
<li>hot liquids</li>
<li>steam</li>
<li>hot oil</li>
<li>hot surfaces</li>
</ul>

""",

"Chemical Burn": """

<h1>Chemical Burn</h1>

<ul>
<li>acids</li>
<li>cleaning products</li>
<li>industrial chemicals</li>
</ul>

<h2>First Aid</h2>

<ol>
<li>Wash immediately with water.</li>
<li>Remove contaminated clothing.</li>
<li>Avoid creams and oils.</li>
</ol>

""",

"Electrical Burn": """

<h1>Electrical Burn</h1>

<ul>
<li>possible internal injury</li>
<li>entry and exit wounds</li>
<li>deep hidden damage</li>
</ul>

""",

"Radiation Burn": """

<h1>Radiation Burn</h1>

<ul>
<li>sun exposure</li>
<li>UV exposure</li>
<li>radiation exposure</li>
</ul>

"""
}

# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.markdown(warning_text, unsafe_allow_html=True)

    st.markdown("""
    <div class='main-title'>CUTANEXA Dashboard</div>
    <div class='sub-title'>
    Visual analysis, dressing guidance and monitoring
    </div>
    <br>
    """, unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class='card'>
        <h1>🩹 Prediction</h1>

        <ul>
        <li>visual analysis</li>
        <li>burn degree estimation</li>
        <li>thermal burns</li>
        <li>chemical burns</li>
        <li>electrical burns</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='card'>
        <h1>📋 Guidance</h1>

        <ul>
        <li>dressing protocol</li>
        <li>cleaning guidance</li>
        <li>monitoring advice</li>
        <li>warning signs</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='card'>
        <h1>⚠ Monitoring</h1>

        <ul>
        <li>fever</li>
        <li>pus</li>
        <li>rapid worsening</li>
        <li>deep injuries</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PREDICTION
# =========================================================

elif page == "Prediction":

    st.markdown("""
    <div class='main-title'>Prediction</div>
    <div class='sub-title'>
    Upload an image for visual analysis
    </div>
    """, unsafe_allow_html=True)

    burn_type = st.selectbox(
        "Select burn type",
        [
            "Thermal Burn",
            "Chemical Burn",
            "Electrical Burn",
            "Radiation Burn"
        ]
    )

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file).convert("RGB")

        st.image(image, width=350)

        img = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():

            outputs = model(img)

            _, predicted = torch.max(outputs,1)

            prediction = classes[predicted.item()]

        st.markdown(f"""
        <div class='prediction-box'>
        <h1>Prediction Result</h1>
        <h1>{prediction}</h1>
        <h2>Burn Type: {burn_type}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class='info-card'>
        {burn_details[prediction]}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class='info-card'>
        {burn_details[burn_type]}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ASSISTANT
# =========================================================

elif page == "Assistant":

    st.markdown("""
    <div class='main-title'>Assistant</div>
    <div class='sub-title'>
    Guidance and monitoring assistant
    </div>
    """, unsafe_allow_html=True)

    question = st.text_area("Ask your question")

    if st.button("Send"):

        st.info("""
Cooling with temperate water is recommended immediately after thermal injuries.

Seek rapid consultation in cases of:
- fever
- pus
- severe pain
- extensive injuries
- rapid worsening
        """)

# =========================================================
# INFORMATION
# =========================================================

elif page == "Information":

    st.markdown(warning_text, unsafe_allow_html=True)

    st.markdown("""
    <div class='main-title'>Burn Information</div>
    <div class='sub-title'>
    Types, degrees, dressing guidance and monitoring
    </div>
    """, unsafe_allow_html=True)

    info = st.selectbox(
        "Select information",
        [
            "First Degree Burn",
            "Superficial Second Degree Burn",
            "Deep Second Degree Burn",
            "Third Degree Burn",
            "Thermal Burn",
            "Chemical Burn",
            "Electrical Burn",
            "Radiation Burn"
        ]
    )

    st.markdown(f"""
    <div class='info-card'>
    {burn_details[info]}
    </div>
    """, unsafe_allow_html=True)