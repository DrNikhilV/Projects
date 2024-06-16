import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf

# Function to preprocess the uploaded image
def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((64, 64))
    img = np.array(img)
    img = img / 255.0  # Normalizing pixel values
    return img.reshape(-1, 64, 64, 3)

# Load the trained ResNet50 model
model = load_model("model_100_epoch.h5")

st.title("Land Class Prediction")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Make prediction
    if st.button('Predict'):
        st.write("Predicting...")

        # Preprocess the image
        img_array = preprocess_image(uploaded_file)

        # Make prediction
        predictions = model.predict(img_array)

        # Get the predicted class
        predicted_class = np.argmax(predictions)

        # Define class names
        class_names = ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial', 'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake']

        # Show the result
        st.write(f"Predicted Land Class: {class_names[predicted_class]}")
