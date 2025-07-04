import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os
# import os
import gdown
# import streamlit as st

st.set_page_config(page_title="Viz Demo")

# Google Drive File ID
file_id = '1-6NF33Q_GQ_zjPEwqVdAe3oJaHkIslDF'
url = f'https://drive.google.com/uc?export=download&id={file_id}'

# Download if not present
if not os.path.exists('pipeline.pkl'):
    with st.spinner('Downloading pipeline.pkl...'):
        gdown.download(url, 'pipeline.pkl', quiet=False)
        st.success('pipeline.pkl downloaded!')


def download_if_not_exists(file_name, file_id):
    if not os.path.exists(file_name):
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        gdown.download(url, file_name, quiet=False)

# Example for df.pkl
download_if_not_exists('df.pkl', '1ocVXvHImvBTbOJhq6LWtiraZUZcBkSgw')
df = joblib.load('df.pkl')



# df = joblib.load('df.pkl')
# df = joblib.load('df.pkl')

pipeline = joblib.load('pipeline.pkl')

# with open('df.pkl', 'rb') as file:
#     df = pickle.load(file)
#
# with open('pipeline.pkl', 'rb') as file:
#     pipeline = pickle.load(file)


# st.dataframe(df)

st.header('Enter your inputs')

# property_type
property_type = st.selectbox('Property Type', ['flat','house'])

# sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
store_room = float(st.selectbox('Store Room',[0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    # Form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area,
             servant_room, store_room, furnishing_type, luxury_category, floor_category]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # Display the DataFrame


    #Predict
    base_price= np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high =base_price +0.22

    #display
    st.text("The Price of the flat is between {} Cr and {} Cr".format (round(low,2),round(high,2)))


