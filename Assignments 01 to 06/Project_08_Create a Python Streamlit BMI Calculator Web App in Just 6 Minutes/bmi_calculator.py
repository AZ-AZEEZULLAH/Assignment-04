# Importing the required library
import streamlit as st

# Set the title of the app
st.title("💪 BMI Calculator Web App")

# Add a short description
st.write("Enter your weight and height below to calculate your BMI (Body Mass Index).")

# Input fields for weight (in kilograms)
weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=300.0, step=0.5)

# Input fields for height (in centimeters)
height = st.number_input("Enter your height (cm)", min_value=50.0, max_value=250.0, step=0.5)

# Button to trigger BMI calculation
if st.button("Calculate BMI"):
    # Convert height from cm to meters
    height_m = height / 100

    # Calculate BMI using the formula: weight / (height in meters)^2
    bmi = weight / (height_m ** 2)

    # Show the BMI result
    st.success(f"Your BMI is: {bmi:.2f}")

    # Determine the BMI category
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.info("You are overweight.")
    else:
        st.error("You are obese.")


# Add a footer with a link to the source code
st.markdown(
    """
    ---
    Made with ❤️ by [Azeezullah]
    ---
    
    """)