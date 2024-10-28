# Import necessary library
import streamlit as st

# Title of the app
st.title("Temperature Converter")

# User input for temperature in Fahrenheit
fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Button to trigger conversion
if st.button("Convert to Celsius"):
    celsius = fahrenheit_to_celsius(fahrenheit)
    st.write(f"The temperature in Celsius is: {celsius:.2f} °C")
