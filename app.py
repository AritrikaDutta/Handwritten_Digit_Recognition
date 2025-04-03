import streamlit as st
from app.draw_predict import draw_digit_predict
from app.image_predict import image_digit_predict


# Title
st.markdown(
    "<h1 style='text-align: center; font-size: 35px;'>Single Handwritten Digit Recognition</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Welcome to the Single Handwritten Digit Recognition App!</p>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'> Select an option to get started.</p>", 
    unsafe_allow_html=True
)

# Centering the radio button using columns
col1, col2, col3 = st.columns([2, 3, 2])  # Adjust column width as needed

with col2:  # Placing the radio button in the center column
    option = st.radio(
        "Choose an option",
        ["Home", "Draw a digit", "Upload an image"],
        index=0
    )

# Show content based on selected option
if option == "Home":
    pass

elif option == "Draw a digit":
    draw_digit_predict()

elif option == "Upload an image":
    image_digit_predict()
