import streamlit as st
import pandas as pd
from io import StringIO

# Set the title of the app
st.title("CSV Data Viewer and Downloader")

# Option to upload CSV or input data
st.header("Upload or Enter CSV Data")

# Create an upload file button
uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])

# Text area for manual data input
data_text = st.text_area("Or, paste your CSV data here", height=200)

# DataFrame display area
st.subheader("Data Preview")

# Function to load data from uploaded file or text input
def load_data(file=None, text=None):
    if file:
        return pd.read_csv(file)
    elif text:
        return pd.read_csv(StringIO(text))
    else:
        return None

# Load data from the file or text input
if uploaded_file:
    df = load_data(file=uploaded_file)
elif data_text:
    df = load_data(text=data_text)
else:
    df = None

# Display the DataFrame if available
if df is not None:
    st.write(df)

    # Button to download DataFrame as a CSV file
    st.subheader("Download CSV File")
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="downloaded_data.csv",
        mime="text/csv",
    )
else:
    st.write("Upload a file or enter CSV data to see a preview.")
