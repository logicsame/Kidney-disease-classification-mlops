
import streamlit as st
import io
from PIL import Image
import os
from cnnClassifier.pipeline.predict import Prediction

st.set_page_config(page_title="Chicken Health Predictor", page_icon="🐔", layout="wide")

st.title("🐔 Chicken Health Predictor")
st.markdown("### Upload an image to predict if the chicken is healthy or has coccidiosis")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Save the uploaded file temporarily
    temp_file = "temp_image.jpg"
    image.save(temp_file)
    
    with st.spinner("Analyzing the image..."):
        predictor = Prediction(temp_file)
        prediction = predictor.predict()
    
    # Remove the temporary file
    os.remove(temp_file)
    
    col2.markdown("## Prediction Result")
    if prediction == "Normal":
        col2.success(f"The chicken appears to be **{prediction}**! 🎉")
        col2.markdown("Keep up the good care for your feathered friend!")
    else:
        col2.error(f"The kidney may have **{prediction}**. 😢")
        col2.markdown("Please consult with a veterinarian for proper treatment.")
    
    

st.sidebar.title("About")
st.sidebar.info(
    "This app uses a deep learning model to predict whether a chicken is healthy "
    "or has coccidiosis based on an uploaded image. Always consult with a "
    "veterinarian for accurate diagnosis and treatment."
)

st.sidebar.title("Instructions")
st.sidebar.markdown(
    """
    1. Upload a clear image of a chicken.
    2. Wait for the model to analyze the image.
    3. View the prediction result and additional information.
    """
)

st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #FDFCFB, #E2D1C3);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(to bottom, #FDFCFB, #E2D1C3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)