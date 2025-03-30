import streamlit as st
from PIL import Image
from app.utils import predict_digit_from_image

def image_digit_predict():
    st.header("Upload an image of a digit")
    uploaded_file = st.file_uploader("Choose an image...", type="png")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        
        if st.button("Predict"):
            prediction = predict_digit_from_image(image)
            st.write(f"Prediction: {prediction}")
