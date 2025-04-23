import streamlit as st

def main():
    # No st.set_page_config() here to prevent conflicts with main.py
    
    st.title("Your Third App")
    st.write("""
    This is where your third app's description will go.
    Add your app's functionality here.
    """)

    # Add your app's functionality here
    # For example:
    # uploaded_file = st.file_uploader("Choose a file", type="xyz")
    # if uploaded_file is not None:
    #     # Process the file
    #     # Show preview
    #     # Add download button
    
if __name__ == "__main__":
    main() 