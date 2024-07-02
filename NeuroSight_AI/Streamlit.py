import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import requests
import tempfile
import os

# Function to download the model file to a temporary location on disk
def download_model():
    model_url = 'https://raw.githubusercontent.com/DrNikhilV/My-Projects/main/NeuroSight%20AI/adrelu.h5'  # Replace with the correct raw URL
    response = requests.get(model_url)
    response.raise_for_status()
    
    # Create a temporary file
    temp_model_file = tempfile.NamedTemporaryFile(delete=False, suffix='.h5')
    temp_model_file.write(response.content)
    temp_model_file.close()
    
    return temp_model_file.name

# Load the saved model
model_file_path = download_model()
loaded_model = tf.keras.models.load_model(model_file_path)

# Define a dictionary to map numerical labels to class names
class_names = {
    0: 'Glioma',
    1: 'Meningioma',
    2: 'No Tumor',
    3: 'Pituitary Tumor'
}

def predict_class(image_file):
    img = image.load_img(image_file, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.  # Rescale pixel values to [0, 1]
    predictions = loaded_model.predict(img_array)
    predicted_class = np.argmax(predictions)
    return class_names[predicted_class]

# Streamlit code
st.title("Brain Tumor Classification")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    prediction = predict_class(uploaded_file)
    st.write("Prediction:", prediction)

# Remove the temporary model file after using it
os.remove(model_file_path)
