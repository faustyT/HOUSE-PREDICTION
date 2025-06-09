import streamlit as st
import joblib
import numpy as np
import os

if not os.path.exists("kc_House_prediction.pkl"):
    import download_model
    
# Load the saved Random Forest model
model = joblib.load("KC_House_Prediction.pkl")

# Custom CSS for background image
st.markdown(
    """
    <style>
    body {
        background-image: url('house img.jpeg');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .stApp {
        background-color: rgba('blue');
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Streamlit app title
st.title("House Price Prediction App")
st.write("This app predicts house prices based on user inputs using a Random Forest model.")

# Sidebar for user input
st.sidebar.header("Input Features")

def user_input():
    bedrooms = st.sidebar.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.sidebar.number_input("Number of Bathrooms", min_value=1.0, max_value=10.0, value=2.0)
    sqft_living = st.sidebar.number_input("Living Area (sqft)", min_value=500, max_value=10000, value=1800)
    sqft_lot = st.sidebar.number_input("Lot Area (sqft)", min_value=1000, max_value=100000, value=5000)
    floors = st.sidebar.number_input("Number of Floors", min_value=1.0, max_value=4.0, value=1.0)
    waterfront = st.sidebar.selectbox("Waterfront (0 = No, 1 = Yes)", [0, 1])
    view = st.sidebar.slider("View", min_value=0, max_value=4, value=0)
    condition = st.sidebar.slider("Condition", min_value=1, max_value=5, value=3)
    grade = st.sidebar.slider("Grade", min_value=1, max_value=13, value=7)
    sqft_above = st.sidebar.number_input("Square Footage Above Ground", min_value=500, max_value=10000, value=1500)
    sqft_basement = st.sidebar.number_input("Square Footage of Basement", min_value=0, max_value=5000, value=300)
    yr_built = st.sidebar.number_input("Year Built", min_value=1900, max_value=2024, value=2000)
    yr_renovated = st.sidebar.number_input("Year Renovated (0 if not renovated)", min_value=0, max_value=2024, value=0)
    lat = st.sidebar.number_input("Latitude", value=47.5112)
    long = st.sidebar.number_input("Longitude", value=-122.257)

    # Collecting inputs into a numpy array
    features = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, 
                          floors, waterfront, view, condition, grade, 
                          sqft_above, sqft_basement, yr_built, yr_renovated, 
                          lat, long]])
    return features

# Get user input
input_features = user_input()

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_features)
    st.subheader("Predicted House Price:")
    st.write(f"${prediction[0]:,.2f}")
