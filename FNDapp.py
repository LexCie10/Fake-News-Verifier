
import pickle
import streamlit as st
import pandas as pd


# load the file that contains the model (model.pkl)
with open("fake_news_pipeline.pkl", 'rb') as f:
    pipeline = pickle.load(f)


    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color:white;
        border-radius:10px;
        font-size:20px;
        height:3em;
        width:10em;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff6666;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        border: 2px solid #4A7DF5;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Give the Streamlit app page a title
st.markdown("<h1 style='text-align: center; color: #4A7DF5;'>FAKE NEWS VERIFIER</h1>", unsafe_allow_html=True)
st.write("<h3 style='text-align: center;'>Type a news article title and content here to verify if it's <b>Fake</b> or <b>Real</b>.</h3>", unsafe_allow_html=True)

# input fields for getting user values for X (title and text fields)
title = st.text_input("Title", placeholder="Enter the news headline here...")
text = st.text_area("Content", placeholder="Paste the full news article here...")

# After the user pastes the title and text of his or her News article and the 'submit' button is clicked, make the prediction and store it
if st.button("Verify"):
    if title and text:
        # Combine title and text
        combined_text = title + " " + text

        # Predict using the pipeline
        prediction = pipeline.predict([combined_text])[0]

        # Show result
        result = "✅ **Real News**" if prediction == 1 else "❌ **Fake News**"
        st.subheader(result)
    else:
        st.warning("⚠️ Please enter both the title and content to verify.")
