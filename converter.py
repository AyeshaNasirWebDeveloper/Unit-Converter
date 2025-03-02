import streamlit as st

# Unit conversion function
def convert_length(value, from_unit, to_unit):
    conversions = {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'inch': 39.3701,
        'foot': 3.28084,
        'yard': 1.09361,
        'mile': 0.000621371
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'kilogram': 1,
        'gram': 1000,
        'milligram': 1e6,
        'pound': 2.20462,
        'ounce': 35.274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Streamlit app
def main():
    st.set_page_config(page_title="Unit Converter", layout="wide")

    # Initialize session state for theme
    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    # Mode change
    def apply_theme(theme):
        if theme == "dark":
            st.markdown(
                """
                <style>
                .stApp {
                    background-color: #1e1e1e;
                    color: #ffffff;
                }
                .stSuccess {
                    background-color: #4CAF50;
                    color: white;
                }
                .stButton button {
                    background-color: #000000;
                    color: white;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <style>
                .stApp {
                    background-color: #ffffff;
                    color: #000000;
                }
                .stSuccess {
                    background-color: #4CAF50;
                    color: white;
                }
                # .stButton button {
                #     background-color: ;
                #     color: white;
                # }
                </style>
                """,
                unsafe_allow_html=True,
            )

    # Toggle button
    col1, col2 = st.columns([9, 1])
    with col1:
        st.title("Unit Converter")
        st.write("#### Convert with Confidence – Seamlessly Switch Between Units, Anytime, Anywhere!")
    with col2:
        if st.button("🌙" if st.session_state.theme == "light" else "☀️"):
            st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

    # Apply the selected theme
    apply_theme(st.session_state.theme)

    # Unit type selection
    unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

    # Unit conversion
    if unit_type == "Length":
        units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'inch', 'foot', 'yard', 'mile']
    elif unit_type == "Weight":
        units = ['kilogram', 'gram', 'milligram', 'pound', 'ounce']
    elif unit_type == "Temperature":
        units = ['celsius', 'fahrenheit', 'kelvin']

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", units)
    with col2:
        to_unit = st.selectbox("To", units)

    value = st.number_input("Enter value", value=1.0)

    if unit_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif unit_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif unit_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    st.success(f"Converted value: {result:.2f} {to_unit}")

    # Simple explanation
    if st.button("Explain Unit"):
        st.info(f"The unit '{from_unit}' is a standard unit of measurement for {unit_type.lower()}.")

if __name__ == "__main__":
    main()