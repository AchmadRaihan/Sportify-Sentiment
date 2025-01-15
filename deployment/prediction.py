# Import libraries

import streamlit as st
import pickle
import pandas as pd
import numpy as np
from tensorflow.keras.layers import TextVectorization

#---------------------------------#

def app():
    # create new data inference
    df_inf = st.text_input()

    # Load models
    Vectorize = pickle.load(open('Vectorize.pkl', 'rb'))
    from_disk = pickle.load(open("tv_layer.pkl", "rb"))
    model_ann = pickle.load(open('model.pkl', 'rb'))

    # vektorisasi data pada CountVectorizer()
    df_inf_encode = Vectorize.transform(df_inf)

    # open pickle TextVectorization()
    new_v = TextVectorization.from_config(from_disk['config'])
    # You have to call `adapt` with some dummy data (BUG in Keras)
    new_v.adapt(['axa'])
    new_v.set_weights(from_disk['weights'])

    # vektorisasi df_inf menggunakan TextVectorization()
    df_inf_ecd = new_v(df_inf)

    # prediksi
    y_pred_inf = model_ann.predict(df_inf_ecd)

    # hasil prediksi dengan pengondisian
    y_pred_inf = np.where(y_pred_inf >= 0.5, 'Positive', 'Negative')
    st.write('Hasil Prediksi menunjukkan: ', y_pred_inf)
    st.write(df_inf)

