import streamlit as st
from apps.csv_converter import main as csv_converter_app
from apps.new_converter import main as new_converter_app
from apps.third_app import main as third_app_main

# Dictionary of available apps
APPS = {
    "CSV to XLSX Converter": csv_converter_app,
    "New Converter": new_converter_app,
    "Third App": third_app_main,
}

def main():
    st.set_page_config(
        page_title="File Converter Tools",
        page_icon="🔄",
        layout="wide"
    )

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(APPS.keys()))

    # Run the selected app
    APPS[selection]()

if __name__ == "__main__":
    main() 