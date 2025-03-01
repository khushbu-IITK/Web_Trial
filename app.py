# -*- coding: utf-8 -*-
"""App.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IZNqKlKSbmLxfBT-M_7fYflc3rS78K4B
"""

#!pip install streamlit

# app.py
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

# Load the trained model
path = 'mnist_model.h5'
model = load_model(path)

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((28, 28))
    image = image.convert('L')  # Convert to grayscale
    image = np.array(image) / 255.0  # Normalize
    image = image.reshape(1, 28, 28, 1)  # Reshape for the model
    return image

# Streamlit app layout
st.title("MNIST Digit Recognition")
st.write("Upload a handwritten digit image (28x28 pixels) to predict.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type="png")

if uploaded_file is not None:
    # Load and preprocess the image
    image = Image.open(uploaded_file)
    processed_image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(processed_image)
    predicted_digit = np.argmax(prediction)
    confidence = np.max(prediction)  # Get the confidence score

    # Display the image and prediction
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write(f"Predicted Digit: {predicted_digit}")
    st.write(f"Confidence: {confidence:.2f}")  # Display confidence as a percentage

