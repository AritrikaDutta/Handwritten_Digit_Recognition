import numpy as np
import tensorflow as tf
from PIL import Image
import cv2
import streamlit as st

@st.cache_resource
def load_model():
    # Load the trained model only once
    return tf.keras.models.load_model("app/model/mnist_cnn_model.h5")

def preprocess_image(image):
    # Convert the image (from the canvas or webcam) to a NumPy array if not already
    if not isinstance(image, np.ndarray):
        image = np.array(image)
    
    # Convert the image to a PIL Image object (ensures ownership of data)
    image = Image.fromarray(np.uint8(image)).convert('L')
    
    # Resize the image to 28x28 (as required by your model)
    image = image.resize((28, 28))
    
    # Normalize the image data (if your model requires it)
    image = np.array(image) / 255.0  # Assuming normalization is needed
    
    # Reshape the image as required by your model
    image = image.reshape(1, 28, 28, 1)  # This shape depends on your model input requirements
    
    return image

def predict_digit_from_image(image):
    model = load_model()  # Use cached model

    preprocessed_image = preprocess_image(image)
    
    prediction = model.predict(preprocessed_image).argmax()
    return prediction
