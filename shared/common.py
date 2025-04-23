import streamlit as st

def set_page_style():
    """Apply consistent styling across all apps"""
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        .sub-header {
            font-size: 1.5rem;
            color: #34495e;
            margin-bottom: 0.5rem;
        }
        .description {
            font-size: 1rem;
            color: #7f8c8d;
            margin-bottom: 2rem;
        }
        .success-message {
            background-color: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 0.3rem;
            margin: 1rem 0;
        }
        .sidebar-header {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

def app_header(title, description):
    """Display a consistent header for each app"""
    st.markdown(f'<div class="main-header">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="description">{description}</div>', unsafe_allow_html=True)

def app_footer():
    """Display a consistent footer for each app"""
    st.markdown("---")
    st.markdown("© 2025 File Converter Tools | Made with Streamlit")
    
def display_success(message):
    """Display a consistent success message"""
    st.markdown(f'<div class="success-message">{message}</div>', unsafe_allow_html=True) 