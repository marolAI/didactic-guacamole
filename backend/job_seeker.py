"""This is a streamlit app for job seekers."""
import os
import urllib.request
import pandas as pd
import streamlit as st

from io import StringIO
from matplotlib import pyplot as plt
from cryptography.fernet import Fernet


cipher_suite = Fernet(st.secrets.encryption_key)
dataset_url = "https://raw.githubusercontent.com/marolAI/job-market-trends-MG/main/data/job_title_counts"


@st.cache_data
def get_data(url) -> pd.DataFrame:
    """Get the data from the GitHub repository."""
    with urllib.request.urlopen(url) as f:
        encrypted_data = f.read().decode("utf-8")
        # Decrypt the data
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        decrypted_string = decrypted_data.decode('utf-8')
        decrypted_file = StringIO(decrypted_string)
    
    return pd.read_csv(decrypted_file)


def top_job_seeker():
    job_title_counts_df = get_data(dataset_url)

    with st.sidebar:
        st.write(" Select a value on the slider to view the top job seekers ")
        # Create a slider for the top_n variable
        top_n = st.slider(
            label="Choose a value",
            min_value=1, 
            max_value=30, 
            value=10
        )

    top_job_titles = job_title_counts_df.sort_values(ascending=False, by='Count')
    top_job_titles = top_job_titles.head(top_n)

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_job_titles.job_title, top_job_titles.Count, color='skyblue')
    ax.set_xlabel('Count')
    ax.set_title('Top {} Job Seekers in Madagascar'.format(top_n))

    # Invert the y-axis to display 
    # the most sought-after job titles at the top
    ax.invert_yaxis()
    st.pyplot(fig)