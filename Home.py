import os
import streamlit as st
import gdown

# ---------------------- UI CONFIG ----------------------
st.set_page_config(
    page_title="Real Estate App",
    page_icon="🏡",
    layout="centered",
)

# ---------------------- HEADER ----------------------
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏡 Real Estate Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #117A65;'>Explore | Analyze | Predict | Recommend</h4>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #F7DC6F;'>", unsafe_allow_html=True)

# ---------------------- Welcome Text ----------------------
st.markdown("""
<div style='background-color:#E8F8F5; padding: 15px; border-radius: 10px;'>
<b>🎉 Welcome to the <span style="color:#148F77;">Real Estate App</span>!</b><br><br>
This project allows you to:
<ul>
    <li>📈 <b>Predict</b> property values using ML</li>
    <li>🔍 <b>Analyze</b> key influencing factors</li>
    <li>🤝 <b>Get Recommendations</b> for locations or properties</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------------- Instructions ----------------------
st.markdown("### 🧭 <span style='color:#5D6D7E'>How to Use This App:</span>", unsafe_allow_html=True)

st.markdown("""
<div style='background-color:#FCF3CF; padding: 10px; border-left: 6px solid #F1C40F; border-radius: 6px;'>
👉 All features are in the <b>sidebar</b> (left side).  
If it's hidden, click the <b>☰ menu icon</b> at the top-left to open it.
</div>
""", unsafe_allow_html=True)

st.markdown("### 🌟 <span style='color:#6C3483;'>Available Features</span>", unsafe_allow_html=True)

st.markdown("""
- 🏠 <span style='color:#1F618D'>**Home**</span> — You're here now!
- 📊 <span style='color:#2874A6'>**Predict Price**</span> — Estimate the price of a property
- 📍 <span style='color:#239B56'>**Recommend Area**</span> — Get suggestions based on your needs
- 📌 <span style='color:#BA4A00'>**Explore Data**</span> — Visual insights and analysis
""", unsafe_allow_html=True)

# ---------------------- File Downloader Info ----------------------
st.info("📦 Downloading required model files from Google Drive (only once)...")

# Ensure datasets directory exists
os.makedirs('real-estate-app/datasets', exist_ok=True)

# Files from Google Drive
files_to_download = {
    'feature_text.pkl': '1OM2sRJ1z9ScjC7GLWYXMycvpiSqyUISb',
    'cosine_sim1.pkl': '1VBO_Pd2Ksx9znC_pshwoXvjkpENVbklA',
    'cosine_sim2.pkl': '1w8nZg5wdL4Wy4rD-rkKoACcDUMOWhT_E',
    'cosine_sim3.pkl': '19K-EBMPePasPHDbnQuMfChmF5TEWWH3C',
    'location_distance.pkl': '1aC4AYjHqFeP6y9_pE93ydNF2HlOlgYTL',
    'df.pkl': '1ocVXvHImvBTbOJhq6LWtiraZUZcBkSgw',
}

# Download files if not already present
for filename, file_id in files_to_download.items():
    file_path = f'real-estate-app/datasets/{filename}'
    if not os.path.exists(file_path):
        with st.spinner(f"⬇️ Downloading {filename}..."):
            gdown.download(id=file_id, output=file_path, quiet=False)
            st.success(f"✅ {filename} downloaded!")

# Download pipeline.pkl separately
pipeline_id = '1-6NF33Q_GQ_zjPEwqVdAe3oJaHkIslDF'
pipeline_path = "pipeline.pkl"
if not os.path.exists(pipeline_path):
    with st.spinner("⬇️ Downloading pipeline.pkl..."):
        pipeline_url = f"https://drive.google.com/uc?export=download&id={pipeline_id}"
        gdown.download(pipeline_url, pipeline_path, quiet=False)
        st.success("✅ pipeline.pkl downloaded!")

# ---------------------- Footer Message ----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.success("🎯 Setup complete! Use the **sidebar** to explore the app.")
