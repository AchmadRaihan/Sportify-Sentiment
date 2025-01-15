import streamlit as st
import eda
import prediction

#---------------------------------#

PAGES = {
    "Exploratory Data Analysis": eda,
    "Prediction": prediction
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()