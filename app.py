import numpy as np
import pickle
import streamlit as st

# Load the model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Function for prediction
def Housing_price_prediction(input_data):
    # Convert input_data to a NumPy array and reshape
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Make prediction
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]  # Return the predicted value

def main():
    # Setting the title
    st.title("California Housing Price Prediction")

    # Getting data from the user
    MedInc = st.text_input('Median Income')
    HouseAge = st.text_input('Median House Age')
    AveRooms = st.text_input('Average Number of Rooms')
    AveBedrms = st.text_input('Average Number of Bedrooms')
    Population = st.text_input('Block Group Population')
    AveOccup = st.text_input('Average Number of Household Members')
    Latitude = st.text_input('Latitude')
    Longitude = st.text_input('Longitude (in -)')

    # Convert inputs to a list
    input_data = [MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]

    # Button for prediction
    if st.button('Housing Price Prediction'):
        try:
            # Convert input_data to floats and predict
            prediction = Housing_price_prediction(input_data)
            st.success(f'The predicted housing price is: ${prediction*100000:.2f}')
        except Exception as e:
            st.error(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
