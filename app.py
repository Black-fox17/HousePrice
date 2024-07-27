import streamlit as st
import pickle 
import numpy as np
# Set up the title and subheader
st.title("House Price Predictor")
st.subheader("ABDUR-RAZAQ SAYFULLAH ADEBOLA House price predictor")
# Display a warning message
st.warning("Please fill out the form below:")

# Input fields for house attributes
house_age = st.text_input("Please enter House age: ")
num_bedrooms = st.text_input("Please enter Number of Bedrooms: ")
num_bathrooms = st.text_input("Please enter Number of Bathrooms: ")
area = st.text_input("Please enter Area (in sq ft): ")
location = st.selectbox(
    'Choose Location:',
    ('Urban', 'Suburban', 'Rural')
)
# Ensure all inputs are provided
if st.button("Predict Price"):
    if not all([house_age, num_bedrooms, num_bathrooms, area, location]):
        st.error("Please fill out all the fields.")
    else:
        try:
            # Convert inputs to appropriate data types
            house_age = int(house_age)
            num_bedrooms = int(num_bedrooms)
            num_bathrooms = int(num_bathrooms)
            area = float(area)
            location = location.strip().lower()
            value = False
            if location == "urban":
                loc_int = 0
                value = True
            elif location == "suburban":
                loc_int = 1
                value = True
            elif location == "rural":
                loc_int = 2
                value = True


            if value == True:
                input_values = np.array([house_age, num_bedrooms, num_bathrooms, area, loc_int]).reshape(1,-1)
                with open("prediction.pkl","rb") as file:
                    model = pickle.load(file)
                predicted_price = model.predict(input_values)
                predicted_price = predicted_price.tolist()[0]
                # Display the predicted price
                st.success(f"Predicted House Price: ${predicted_price:,.2f}")
            else:
                st.error("Please enter any values in [Suburban,Urban,Rural] for the Location Field")

        except ValueError:
            st.error("Please enter valid numbers for House Age, Number of Bedrooms, Number of Bathrooms, and Area.")
