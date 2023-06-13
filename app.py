import streamlit as st
import pandas as pd

# Load the Profiles and Tally dataframes
#profiles = pd.read_csv("profiles.csv")
tally = pd.read_csv("tally.csv")

# Create a list of ids
ids = tally["resource_id"].unique()

# Create a drop down menu for the id
id = st.selectbox("Select an id", ids)

# If an id is selected, read the corresponding Profiles dataframe
if id:
  profiles = pd.read_csv(f"profiles_{id}.csv")

# Display the Profiles dataframe
st.table(profiles)
