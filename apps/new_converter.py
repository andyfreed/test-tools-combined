import streamlit as st
from shared.common import app_header, app_footer

def main():
    app_header(
        "New Converter Tool",
        "This is a template for a new file conversion tool. Customize it for your specific needs."
    )
    
    st.markdown('<div class="sub-header">Upload File</div>', unsafe_allow_html=True)
    
    # Add your app's functionality here
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt"])
    
    if uploaded_file is not None:
        st.markdown('<div class="sub-header">File Details</div>', unsafe_allow_html=True)
        
        file_details = {
            "Filename": uploaded_file.name,
            "File size": f"{uploaded_file.size / 1024:.2f} KB",
            "File type": uploaded_file.type
        }
        
        for key, value in file_details.items():
            st.write(f"**{key}:** {value}")
        
        # Add your processing code here
        
    app_footer()
    
if __name__ == "__main__":
    main() 