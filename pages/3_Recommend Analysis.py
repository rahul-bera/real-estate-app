import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import joblib


st.set_page_config(page_title= "Recommended Apartment")

st.title('Recommend Analysis')

location_df = joblib.load('datasets/location_distance.pkl')
cosine_sim1 = joblib.load('datasets/cosine_sim1.pkl')
cosine_sim2 = joblib.load('datasets/cosine_sim2.pkl')
cosine_sim3 = joblib.load('datasets/cosine_sim3.pkl')


def recommend_properties_with_scores(property_name, top_n=247):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df



st.title('Select Location and Radius')

selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))

radius = st.number_input ('Radius in Kms')

if st.button('Search'):
    result_ser = location_df[location_df[selected_location] < radius*1000][selected_location].sort_values()

    # for key, value in result_ser.items():
    #     st.text(str(key)+" "+ str(round(value/1000))+ 'kms')
    if result_ser.empty:
        st.warning("No nearby properties found within the selected radius.")
    else:
        st.success(f"✅ Found {len(result_ser)} properties nearby.")
        for key, value in result_ser.items():
            st.text(f"{key} - {round(value/1000, 2)} kms")

st.title('Recommend Appartments')

selected_appartment = st.selectbox(
    'Select an appartment', sorted(location_df.index.to_list())
)

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(
        selected_appartment, top_n=5
    )

    st.dataframe(recommendation_df)
