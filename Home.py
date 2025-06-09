import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="w",

)

st.write("# Welcome to Streamlit! ")

st.sidebar.success("Select a demo above.")


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


