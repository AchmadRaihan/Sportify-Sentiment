import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


#---------------------------------#
# Page layout
# Page expands to full width
st.set_page_config(page_title='Spotify Sentiment', layout='wide')
#---------------------------------#
def app():
    data = pd.read_csv('dataset.csv')
    data = data.dropna()
    eda = data.copy()

    ###################### Melihat secara garis besar persebaran data melalui visualisasi
    st.title('Data Distribution')
    fig1, ax = plt.subplots(1,2,figsize=(15,6))

    sns.countplot(x='label', data=eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel('Label')
    ax[0].set_ylabel('Count of Review')
    fig1.suptitle('Review Type Distribution')
    ax[0].tick_params(axis='x', rotation=90)
    plt.xlabel('Label')
    plt.ylabel('Count of Review')

    for pch in ax[0].patches:
        ax[0].annotate('%.0f'%(pch.get_height()), (pch.get_x() + pch.get_width() / 2, pch.get_height()+205), ha='center', va='center')
    eda['label'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    ax[1].set_ylabel('Percentage of Review')
    st.write(fig1)

    ####################### Visualisasi sentiment secara general
    st.title('General Sentiment')
    text_all = eda.Review.values
    cloud_all = WordCloud(background_color='black', colormap='cool', collocations=False, width=2000, height=1000).generate(' '.join(text_all))
    fig2, ax2 = plt.subplots()
    ax2.imshow(cloud_all)
    plt.axis('off')
    plt.title('All Review')
    st.pyplot(fig2)

    ####################### Visualisasi sentiment positif
    st.title('Positive Sentiment')
    text_positive = eda[eda['label'] == 'POSITIVE'].Review.values
    cloud_positive = WordCloud(background_color='black', colormap='cool', collocations=False, width=2000, height=1000).generate(' '.join(text_positive))
    fig3, ax3 = plt.subplots()
    ax3.imshow(cloud_positive)
    plt.axis('off')
    plt.title('Positive Review')
    st.pyplot(fig3)

    ####################### Visualisasi sentiment positif
    st.title('Negative Sentiment')
    text_negative = eda[eda['label'] == 'NEGATIVE'].Review.values
    cloud_negative = WordCloud(background_color='black', colormap='cool', collocations=False, width=2000, height=1000).generate(' '.join(text_negative))
    fig4, ax4 = plt.subplots()
    ax4.imshow(cloud_negative)
    plt.axis('off')
    plt.title('Negative Review')
    st.pyplot(fig4)

