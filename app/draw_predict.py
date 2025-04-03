import streamlit as st
from streamlit_drawable_canvas import st_canvas
from app.utils import predict_digit_from_image

def draw_digit_predict():
    st.header("Draw a digit")
    st.write("Kindly draw a single digit.")
    st.write("Multiple digits will display inaccurate results.")

    canvas_result = st_canvas(
        fill_color="#000000",
        stroke_width=10,
        stroke_color="#FFFFFF",
        background_color="#000000",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas"
    )

    if st.button("Predict"):
        if canvas_result.image_data is not None:
            prediction = predict_digit_from_image(canvas_result.image_data)
            st.write(f"Prediction: {prediction}")
