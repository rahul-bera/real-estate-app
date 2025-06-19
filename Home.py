import os
import streamlit as st
import gdown

# ---------------------- UI CONFIG ----------------------
st.set_page_config(
    page_title="Real Estate App",
    page_icon="🏡",
)

# ---------------------- HEADER ----------------------
st.title("🏡 Real Estate Price Prediction App")
st.markdown("### Explore | Analyze | Predict | Recommend")
st.markdown("---")

# ---------------------- Welcome Text ----------------------
st.markdown("""
Welcome to the **Real Estate App**!

This project allows you to:

- 📈 Predict property values using ML
- 🔍 Analyze key influencing factors
- 🤝 Get personalized property recommendations

Use the **sidebar** to navigate between features.
""")

# ---------------------- File Downloader ----------------------
st.info("Downloading required model files from Google Drive (only once)...")

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
        with st.spinner(f"Downloading {filename}..."):
            gdown.download(id=file_id, output=file_path, quiet=False)
            st.success(f"{filename} downloaded!")

# Download pipeline.pkl separately
pipeline_id = '1-6NF33Q_GQ_zjPEwqVdAe3oJaHkIslDF'
pipeline_path = "pipeline.pkl"
if not os.path.exists(pipeline_path):
    with st.spinner("Downloading pipeline.pkl..."):
        pipeline_url = f"https://drive.google.com/uc?export=download&id={pipeline_id}"
        gdown.download(pipeline_url, pipeline_path, quiet=False)
        st.success("pipeline.pkl downloaded!")

# ---------------------- Footer Message ----------------------
st.success("✅ Setup complete. Choose a demo from the sidebar to begin.")
