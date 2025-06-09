import os
import gdown
import streamlit as st

# ---------------------- UI CONFIGURATION ----------------------
st.set_page_config(
    page_title="Real Estate App",
    page_icon="🏡",
)

# ---------------------- BEAUTIFIED HOME PAGE ----------------------
# Title and subtitle
st.markdown("<h1 style='text-align: center; color: white;'>🏡 Real Estate Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Explore | Analyze | Predict | Recommend</h3>", unsafe_allow_html=True)

# Banner image (replace with your own if needed)
st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa", use_column_width=True)

# Welcome message
st.markdown("""
<div style='padding: 20px; background-color: #1e1e1e; border-radius: 10px;'>
    <p style='font-size: 18px; color: white;'>
        Welcome to the Real Estate App! This project lets you:
        <ul style='color: white;'>
            <li>🔍 Explore historical trends in property prices</li>
            <li>📈 Predict future property values using ML</li>
            <li>🧠 Analyze key influencing factors</li>
            <li>🤝 Get property recommendations based on your preferences</li>
        </ul>
        Use the menu on the left to navigate between features.
    </p>
</div>
""", unsafe_allow_html=True)

st.success("👈 Select a demo from the sidebar to begin!")
st.sidebar.success("Select a demo above.")

# ---------------------- DOWNLOAD FILES FROM GOOGLE DRIVE ----------------------

# Create datasets directory if not exists
os.makedirs('real-estate-app/datasets', exist_ok=True)

# Files to download
files_to_download = {
    'feature_text.pkl': '1OM2sRJ1z9ScjC7GLWYXMycvpiSqyUISb',
    'cosine_sim1.pkl': '1VBO_Pd2Ksx9znC_pshwoXvjkpENVbklA',
    'cosine_sim2.pkl': '1w8nZg5wdL4Wy4rD-rkKoACcDUMOWhT_E',
    'cosine_sim3.pkl': '19K-EBMPePasPHDbnQuMfChmF5TEWWH3C',
    'location_distance.pkl': '1aC4AYjHqFeP6y9_pE93ydNF2HlOlgYTL',
    'df.pkl': '1ocVXvHImvBTbOJhq6LWtiraZUZcBkSgw',
}

# Download missing files
for filename, file_id in files_to_download.items():
    file_path = f'real-estate-app/datasets/{filename}'
    if not os.path.exists(file_path):
        with st.spinner(f"Downloading {filename}..."):
            gdown.download(id=file_id, output=file_path, quiet=False)
            st.success(f"{filename} downloaded successfully!")

# Download pipeline.pkl separately
pipeline_id = '1-6NF33Q_GQ_zjPEwqVdAe3oJaHkIslDF'
pipeline_url = f"https://drive.google.com/uc?export=download&id={pipeline_id}"
if not os.path.exists("pipeline.pkl"):
    with st.spinner("Downloading pipeline.pkl..."):
        gdown.download(pipeline_url, "pipeline.pkl", quiet=False)
        st.success("pipeline.pkl downloaded successfully!")
