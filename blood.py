import streamlit as st


# PAWcHIKE - FOR . . .

# Function to calculate blood pressure based on heartbeat formula
def calculate_blood_pressure(heartbeat):
    # Use a simple formula for demonstration purposes
    # You can replace this with a more accurate formula
    systolic_pressure = 90 + 0.6 * heartbeat
    diastolic_pressure = 60 + 0.4 * heartbeat
    return systolic_pressure, diastolic_pressure

# Streamlit app
def main():
    st.title("Blood Pressure Check App")

    # Sidebar with navigation
    option = st.sidebar.selectbox("Select Page", ["Home", "Blood Pressure Check", "CREATE U TABLE"])

    if option == "Home":
        st.write("Welcome to the Blood Pressure Check App!")
        st.write("count the number of beats in 15 seconds. Multiply this number by four to calculate your beats per minute.")
        

    elif option == "Blood Pressure Check":
        st.header("Calculate Blood Pressure")

        # Input for heartbeat
        heartbeat = st.number_input("Enter Heartbeat (beats per minute):", min_value=30, max_value=200, value=75, step=1)

        if st.button("Calculate Blood Pressure"):
            systolic, diastolic = calculate_blood_pressure(heartbeat)
            st.success(f"Estimated Systolic Pressure: {systolic} mmHg")
            st.success(f"Estimated Diastolic Pressure: {diastolic} mmHg")


# PAWcHIKE TABLE . . .
        # Display table using Streamlit's data frame
        # st.table(table_data)

# Run the app
if __name__ == "__main__":
    main()
