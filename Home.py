import os
import gdown
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="w",

)

st.write("# Welcome to Streamlit! ")

st.sidebar.success("Select a demo above.")

# Create datasets directory if not exists
os.makedirs('real-estate-app/datasets', exist_ok=True)

# Download only if file does not exist
files_to_download = {
    'feature_text.pkl': '1OM2sRJ1z9ScjC7GLWYXMycvpiSqyUISb',
    'cosine_sim1.pkl': '1VBO_Pd2Ksx9znC_pshwoXvjkpENVbklA',
    'cosine_sim2.pkl': '1w8nZg5wdL4Wy4rD-rkKoACcDUMOWhT_E',
    'cosine_sim3.pkl': '19K-EBMPePasPHDbnQuMfChmF5TEWWH3C',
    'location_distance.pkl': '1aC4AYjHqFeP6y9_pE93ydNF2HlOlgYTL',
    'df.pkl': '1ocVXvHImvBTbOJhq6LWtiraZUZcBkSgw',
}

for filename, file_id in files_to_download.items():
    file_path = f'real-estate-app/datasets/{filename}'
    if not os.path.exists(file_path):
        print(f"Downloading {filename}...")
        gdown.download(id=file_id, output=file_path, quiet=False)




import os
import gdown
import streamlit as st  # Make sure you have this too

# Download pipeline.pkl from Google Drive if not already present
file_id = '1-6NF33Q_GQ_zjPEwqVdAe3oJaHkIslDF'
url = f"https://drive.google.com/uc?export=download&id={file_id}"

if not os.path.exists("pipeline.pkl"):
    with st.spinner("Downloading pipeline.pkl..."):
        gdown.download(url, "pipeline.pkl", quiet=False)
        st.success("pipeline.pkl downloaded successfully!")


