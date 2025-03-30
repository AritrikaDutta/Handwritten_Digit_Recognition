import streamlit as st
from app.draw_predict import draw_digit_predict
from app.image_predict import image_digit_predict

st.title("Handwritten Digit Recognition")

# Navigation between the different options
option = st.sidebar.selectbox(
    "Choose an option",
    ["Draw a digit", "Upload an image"]
)

if option == "Draw a digit":
    draw_digit_predict()
elif option == "Upload an image":
    image_digit_predict()
