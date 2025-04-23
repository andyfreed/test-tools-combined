import streamlit as st
from apps.csv_converter import main as csv_converter_app
from apps.question_converter import main as question_converter_app
from apps.exam_quiz_converter import main as exam_quiz_converter_app
from shared.common import set_page_style

# App information
APP_INFO = {
    "CSV to XLSX Converter": {
        "icon": "📊",
        "description": "Convert CSV files to XLSX with specific CFP Board formatting.",
        "function": csv_converter_app
    },
    "Question Converter": {
        "icon": "❓",
        "description": "Transform exam questions into importable format.",
        "function": question_converter_app
    },
    "Exam Quiz Converter": {
        "icon": "📝",
        "description": "Convert exam questions from text format to structured spreadsheet.",
        "function": exam_quiz_converter_app
    }
}

def main():
    st.set_page_config(
        page_title="File Converter Tools",
        page_icon="🔄",
        layout="wide"
    )
    
    # Apply consistent styles
    set_page_style()
    
    # Sidebar
    st.sidebar.markdown('<div class="sidebar-header">File Converter Tools</div>', unsafe_allow_html=True)
    st.sidebar.markdown("A suite of tools for file conversion and processing.")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Navigation")
    
    # Create app selection with icons
    app_options = [f"{info['icon']} {name}" for name, info in APP_INFO.items()]
    selected_app_with_icon = st.sidebar.radio("", app_options)
    
    # Extract app name without icon
    selected_app = selected_app_with_icon.split(" ", 1)[1]
    
    # Display app info
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### About {selected_app}")
    st.sidebar.markdown(APP_INFO[selected_app]["description"])
    
    # Add additional sidebar elements
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Help")
    st.sidebar.markdown("For issues or feature requests, please contact support.")
    
    # Run the selected app
    APP_INFO[selected_app]["function"]()

if __name__ == "__main__":
    main() 