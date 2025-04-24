import streamlit as st
from apps.csv_converter import main as csv_converter_app
from apps.question_converter import main as question_converter_app
from apps.exam_quiz_converter import main as exam_quiz_converter_app
from shared.common import set_page_style

# App information
APP_INFO = {
    "Exam Quiz Converter": {
        "icon": "📝",
        "description": "This is the first step to import the exams. Drop the author's file on and here an answer key is applicable.",
        "function": exam_quiz_converter_app
    },
    "Question Converter": {
        "icon": "❓",
        "description": "This is the second step to import the exams. Drop the file created by the previous tool on here and add the category.",
        "function": question_converter_app
    },
    "CSV to XLSX Converter": {
        "icon": "📊",
        "description": "This is a tool used to convert the downloaded CFP credit report into a file that can be uploaded to the CFP Board site.",
        "function": csv_converter_app
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
    
    # Add JavaScript for sidebar toggle on mobile
    sidebar_toggle_js = """
    <script>
    // Add sidebar toggle functionality for mobile
    document.addEventListener('DOMContentLoaded', function() {
        // Function to handle sidebar toggle
        function setupSidebar() {
            const body = document.querySelector('body');
            
            // Create toggle button if it doesn't exist yet
            if (!document.querySelector('.sidebar-toggle')) {
                const toggleButton = document.createElement('button');
                toggleButton.innerHTML = '☰';
                toggleButton.setAttribute('aria-label', 'Toggle Sidebar');
                toggleButton.setAttribute('title', 'Toggle Sidebar');
                toggleButton.classList.add('sidebar-toggle');
                toggleButton.style.cssText = `
                    position: fixed;
                    top: 10px;
                    left: 10px;
                    z-index: 1000;
                    background: #1e88e5;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    width: 40px;
                    height: 40px;
                    font-size: 20px;
                    cursor: pointer;
                    display: none;
                    transition: transform 0.3s ease, background-color 0.3s ease;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
                `;
                
                // Toggle sidebar state on button click
                toggleButton.addEventListener('click', function() {
                    body.classList.toggle('sidebar-collapsed');
                    localStorage.setItem('sidebarCollapsed', body.classList.contains('sidebar-collapsed'));
                });
                
                document.body.appendChild(toggleButton);
            }
            
            // Handle screen size changes
            const mediaQuery = window.matchMedia('(max-width: 992px)');
            function handleScreenChange(e) {
                const toggleButton = document.querySelector('.sidebar-toggle');
                if (e.matches) {
                    // Mobile view
                    toggleButton.style.display = 'block';
                    
                    // Restore saved state or default to not collapsed
                    const wasCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
                    if (wasCollapsed) {
                        body.classList.add('sidebar-collapsed');
                    } else {
                        body.classList.remove('sidebar-collapsed');
                    }
                } else {
                    // Desktop view
                    toggleButton.style.display = 'none';
                    body.classList.remove('sidebar-collapsed');
                }
            }
            
            mediaQuery.addEventListener('change', handleScreenChange);
            handleScreenChange(mediaQuery);
            
            // Close sidebar when clicking on main content in mobile view
            const mainContent = document.querySelector('.main');
            if (mainContent) {
                mainContent.addEventListener('click', function() {
                    if (mediaQuery.matches && !body.classList.contains('sidebar-collapsed')) {
                        body.classList.add('sidebar-collapsed');
                        localStorage.setItem('sidebarCollapsed', 'true');
                    }
                });
            }
        }
        
        // Initial setup
        setupSidebar();
        
        // Re-run setup when Streamlit reruns
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.addedNodes.length) {
                    setupSidebar();
                }
            });
        });
        
        observer.observe(document.body, { childList: true, subtree: true });
    });
    </script>
    """
    st.markdown(sidebar_toggle_js, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-header">File Converter Tools</div>', unsafe_allow_html=True)
        st.markdown("A suite of tools for file conversion and processing.")
        
        st.markdown("---")
        st.markdown("### Navigation")
        
        # Create app selection with icons
        app_options = [f"{info['icon']} {name}" for name, info in APP_INFO.items()]
        selected_app_with_icon = st.radio("", app_options)
        
        # Extract app name without icon
        selected_app = selected_app_with_icon.split(" ", 1)[1]
        
        # Display app info
        st.markdown("---")
        st.markdown(f"### About {selected_app}")
        st.markdown(APP_INFO[selected_app]["description"])
        
        # Add additional sidebar elements
        st.markdown("---")
        st.markdown("### Help")
        st.markdown("For issues or feature requests, please contact support.")
    
    # Run the selected app
    APP_INFO[selected_app]["function"]()

if __name__ == "__main__":
    main() 