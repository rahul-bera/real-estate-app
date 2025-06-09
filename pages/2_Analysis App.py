import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt


st.set_page_config(page_title= "Plotting Demo")

st.title('Analytics')

# new_df = pd.read_csv('datasets/data_viz1.csv')

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle. load(open('datasets/feature_text.pkl','rb'))

# group_df = new_df.groupby('sector') .mean() [['price',
#                                               'price_per_sqft',
#                                               'built_up_area',
#                                               'latitude',
#                                               'longitude']]
# Select only numeric columns
numeric_cols = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']

# Group by sector and take mean only for numeric columns
group_df = new_df[numeric_cols + ['sector']].groupby('sector').mean()


st.header('Sector price per Sqft Geomap')
fig = px.scatter_mapbox(group_df,
                        lat="latitude",
                        lon="longitude",
                        color="price_per_sqft",
                        size='built_up_area',
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        zoom=10,
                        mapbox_style="open-street-map",
                        width=1200,
                        height=700,
                        hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)


st.header('Features Wordcloud')
wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.tight_layout(pad = 0)
# st.pyplot()

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")

# Pass the figure to st.pyplot()
st.pyplot(fig)


st.header('Area vs Price')
property_type = st.selectbox('Select Property Type', ['flat', 'house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price",
                      color="bedRoom", title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price",
                      color="bedRoom", title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)



st.header ('BHK Pie Chart')

sector_options = new_df['sector'].unique() . tolist()
sector_options. insert(0,'overall')

selected_sector= st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)

else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)

st.header('Side by side BHK price comparison')
fig3 =px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)
