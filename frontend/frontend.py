import streamlit as st
import requests
import math
import os

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Insurance AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

API_URL = os.getenv("BACKEND_URL", "https://insurance-premium-fastapi-q86v.onrender.com/predict")


# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

body {
    background: linear-gradient(-45deg,#0f2027,#203a43,#2c5364,#1c1c1c);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

.glass {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(20px);
    border-radius: 22px;
    padding: 30px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.5);
}

.title {
    font-size: 52px;
    font-weight: 900;
    color: white;
}

.subtitle {
    color: #d1d5db;
    font-size: 18px;
}

.metric {
    font-size: 26px;
    font-weight: 800;
    color: #00ffd5;
}

.result {
    font-size: 44px;
    font-weight: 900;
    text-align: center;
    color: #00ffd5;
    margin-top: 20px;
}

.footer {
    text-align:center;
    color:#9ca3af;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>🛡️ Insurance Premium AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Next-generation risk intelligence powered by Machine Learning</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------
with st.container():
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("🎂 Age", 18, 80, 30)
        income = st.slider("💰 Income (LPA)", 1, 100, 12)

    with col2:
        weight = st.slider("⚖️ Weight (kg)", 40, 150, 65)
        height = st.slider("📏 Height (m)", 1.3, 2.2, 1.7)

    with col3:
        smoker = st.selectbox("🚬 Smoker", [False, True])
        city = st.text_input("🏙️ City", "Delhi")
        occupation = st.selectbox(
            "💼 Occupation",
            [
                'private_job','government_job','business_owner',
                'freelancer','student','unemployed','retired'
            ]
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LIVE METRICS ----------------
bmi = round(weight / (height ** 2), 2)

st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("<div class='glass'><div class='metric'>BMI</div>" + str(bmi) + "</div>", unsafe_allow_html=True)

with m2:
    risk = "High" if smoker and bmi > 30 else "Medium" if smoker else "Low"
    st.markdown("<div class='glass'><div class='metric'>Lifestyle Risk</div>" + risk + "</div>", unsafe_allow_html=True)

with m3:
    tier = "Tier 1" if city.lower() in ['delhi','mumbai','bengaluru'] else "Tier 2 / 3"
    st.markdown("<div class='glass'><div class='metric'>City Tier</div>" + tier + "</div>", unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Predict Insurance Category", use_container_width=True):
    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    with st.spinner("🧠 Analyzing risk profile..."):
        response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        category = response.json()["predicted_category"]
        st.markdown(f"<div class='result'>🏷️ {category}</div>", unsafe_allow_html=True)
    else:
        st.error("Prediction failed. Check FastAPI server.")

# ---------------- FOOTER ----------------
st.markdown("<br><div class='footer'>Built with ❤️ using FastAPI • Scikit-Learn • Streamlit</div>", unsafe_allow_html=True)
