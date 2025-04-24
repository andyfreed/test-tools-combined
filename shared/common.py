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
            color: #1e88e5;
        }
        
        /* Enhanced Sidebar Styling */
        .css-1d391kg, .css-12oz5g7, [data-testid="stSidebar"] {
            background-color: #f8f9fa;
            border-right: 1px solid #e9ecef;
            box-shadow: 2px 0 5px rgba(0,0,0,0.05);
        }
        
        /* Fix sidebar text color */
        [data-testid="stSidebar"] {
            color: #333333;
        }
        
        [data-testid="stSidebar"] .stMarkdown {
            color: #333333;
        }
        
        /* Override all text colors in sidebar */
        [data-testid="stSidebar"] * {
            color: #333333 !important;
        }
        
        /* Set the header color back to blue for contrast */
        [data-testid="stSidebar"] .sidebar-header {
            color: #1e88e5 !important;
        }
        
        /* Radio button text color fix */
        .stRadio label {
            color: #333333 !important;
        }
        
        /* Radio button icon color fix */
        .stRadio [data-baseweb="radio"] div[role="radiogroup"] div {
            color: #333333 !important;
        }
        
        /* Force icon colors in the radio buttons */
        .stRadio [data-baseweb="radio"] [data-testid="stMarkdownContainer"] span {
            color: #333333 !important;
        }
        
        /* Fix sidebar markdown text */
        .sidebar .markdown-text-container p,
        .sidebar p,
        .sidebar .element-container {
            color: #333333 !important;
        }
        
        /* Make sure H3 titles have good contrast */
        .sidebar h3 {
            color: #1e88e5 !important;
        }
        
        /* Sidebar animation */
        @media (max-width: 992px) {
            [data-testid="stSidebar"] {
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                z-index: 1000;
            }
            .sidebar-collapsed [data-testid="stSidebar"] {
                transform: translateX(-100%);
                box-shadow: none;
            }
            /* Main content shift when sidebar is open */
            .main .block-container {
                transition: padding-left 0.3s ease, margin-left 0.3s ease;
            }
            .sidebar-collapsed .main .block-container {
                padding-left: 1rem !important;
                margin-left: 0 !important;
            }
        }
        
        /* Sidebar toggle button animation */
        .sidebar-toggle {
            transition: transform 0.3s ease, background-color 0.3s ease;
        }
        .sidebar-collapsed .sidebar-toggle {
            transform: rotate(90deg);
        }
        .sidebar-toggle:hover {
            background-color: #0d47a1 !important;
        }
        
        /* Sidebar items styling */
        .stRadio > div {
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 5px;
            transition: background-color 0.2s;
        }
        .stRadio > div:hover {
            background-color: #e3f2fd;
        }
        
        /* Styling for sidebar dividers */
        .sidebar .markdown-text-container hr {
            margin: 20px 0;
            border: 0;
            height: 1px;
            background: #e0e0e0;
        }
        
        /* Improved navigation section */
        .sidebar h3 {
            font-size: 1.2rem;
            font-weight: 600;
            margin-top: 1rem;
        }
        
        /* Active navigation item */
        .stRadio [data-baseweb="radio"] input:checked + div {
            background-color: #bbdefb;
            border-color: #1e88e5;
        }
        
        /* Sidebar content padding */
        [data-testid="stSidebar"] .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
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