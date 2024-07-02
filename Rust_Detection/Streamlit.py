import streamlit as st
import os
import numpy as np
import cv2
import tensorflow as tf
import pathlib

# Load the saved model
model = tf.keras.models.load_model("Rust_v1.h5")

# Define class labels
class_labels = ['corrosion', 'nocorrosion']

# Function to preprocess the uploaded image
def preprocess_image(image):
    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), 1)
    img = cv2.resize(img, (180, 180))
    img = img / 255.0  # Scale pixel values
    return img

# Streamlit app
st.title("Corrosion Detection")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    # Preprocess the uploaded image
    processed_image = preprocess_image(uploaded_file)

    # Make prediction
    prediction = model.predict(np.expand_dims(processed_image, axis=0))
    predicted_label = np.argmax(prediction)

    # Display prediction
    st.write(f"Prediction: {class_labels[predicted_label]}")