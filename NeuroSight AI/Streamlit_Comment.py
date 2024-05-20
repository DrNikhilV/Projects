import streamlit as st  # Import Streamlit for web application interface
import tensorflow as tf  # Import TensorFlow for model loading and prediction
from tensorflow.keras.preprocessing import image  # Import Keras image processing utilities
import numpy as np  # Import NumPy for numerical operations
import requests  # Import requests to handle HTTP requests
import os  # Import os to handle file operations

# Function to download the model file from a URL
def download_model():
    model_url = 'https://github.com/DrNikhilV/Web-Applications/raw/main/Brain%20Tumor%20Prediction/adrelu.h5'
    response = requests.get(model_url)  # Send a GET request to the model URL
    response.raise_for_status()  # Check if the request was successful
    # Save the content of the response (the model file) to a local file
    with open('model.h5', 'wb') as f:
        f.write(response.content)
    return 'model.h5'  # Return the path to the saved model file

# Download and load the model
model_file_path = download_model()
loaded_model = tf.keras.models.load_model(model_file_path)

# Dictionary mapping class indices to class names
class_names = {
    0: 'Glioma',
    1: 'Meningioma',
    2: 'No Tumor',
    3: 'Pituitary Tumor'
}

# Function to predict the class of the uploaded image
def predict_class(image_file):
    # Load the image with target size of 150x150 pixels
    img = image.load_img(image_file, target_size=(150, 150))
    # Convert the image to a NumPy array
    img_array = image.img_to_array(img)
    # Expand dimensions to match the model's expected input shape
    img_array = np.expand_dims(img_array, axis=0)
    # Rescale pixel values to the range [0, 1]
    img_array /= 255.
    # Predict the class of the image using the loaded model
    predictions = loaded_model.predict(img_array)
    # Get the index of the class with the highest predicted probability
    predicted_class = np.argmax(predictions)
    # Return the corresponding class name
    return class_names[predicted_class]

# Streamlit code to create the web application
st.title("Brain Tumor Classification")  # Set the title of the app
# Create a file uploader widget to upload image files
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If a file is uploaded, display it and make a prediction
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")  # Add a separator line
    st.write("Classifying...")  # Display a message indicating classification

    # Predict the class of the uploaded image
    prediction = predict_class(uploaded_file)
    # Display the prediction result
    st.write("Prediction:", prediction)

# Clean up by removing the downloaded model file
os.remove(model_file_path)
