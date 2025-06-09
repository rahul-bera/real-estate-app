import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import os
import gdown

st.set_page_config(page_title="Recommended Apartment")
st.title('Recommend Analysis')

# Function to download a file from Google Drive if not present
def download_if_not_exists(filepath, gdrive_url):
    if not os.path.exists(filepath):
        file_id = gdrive_url.split("/d/")[1].split("/")[0]
        direct_url = f"https://drive.google.com/uc?export=download&id={file_id}"
        gdown.download(direct_url, filepath, quiet=False)

# Download files if missing
download_if_not_exists('datasets/location_distance.pkl', 'https://drive.google.com/file/d/1aC4AYjHqFeP6y9_pE93ydNF2HlOlgYTL/view?usp=drive_link')
download_if_not_exists('datasets/cosine_sim1.pkl', 'https://drive.google.com/file/d/1VBO_Pd2Ksx9znC_pshwoXvjkpENVbklA/view?usp=drive_link')
download_if_not_exists('datasets/cosine_sim2.pkl', 'https://drive.google.com/file/d/1w8nZg5wdL4Wy4rD-rkKoACcDUMOWhT_E/view?usp=drive_link')
download_if_not_exists('datasets/cosine_sim3.pkl', 'https://drive.google.com/file/d/19K-EBMPePasPHDbnQuMfChmF5TEWWH3C/view?usp=drive_link')

# Load the files
location_df = joblib.load('datasets/location_distance.pkl')
cosine_sim1 = joblib.load('datasets/cosine_sim1.pkl')
cosine_sim2 = joblib.load('datasets/cosine_sim2.pkl')
cosine_sim3 = joblib.load('datasets/cosine_sim3.pkl')

# Recommendation function
def recommend_properties_with_scores(property_name, top_n=247):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()

    return pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

# UI for nearby properties
st.title('Select Location and Radius')
selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in Kms')

if st.button('Search'):
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
    if result_ser.empty:
        st.warning("No nearby properties found within the selected radius.")
    else:
        st.success(f"✅ Found {len(result_ser)} properties nearby.")
        for key, value in result_ser.items():
            st.text(f"{key} - {round(value / 1000, 2)} kms")

# UI for recommendations
st.title('Recommend Appartments')
selected_appartment = st.selectbox('Select an appartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_appartment, top_n=5)
    st.dataframe(recommendation_df)
