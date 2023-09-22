"""This is the main app for the dashboard."""
import streamlit as st

from backend.job_seeker import top_job_seeker


def main():
    st.set_page_config(
        page_title="Malagasy Job Market Dashboard",
        page_icon="",
        # layout="wide"
    )
    # Create a horizontal bar chart for the most sought-after job titles
    st.write("""#### Most Sought-After Job Titles in Madagascar""")
    top_job_seeker()
    
if __name__ == "__main__":
    main()