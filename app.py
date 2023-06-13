import streamlit as st
import pandas as pd

# Load the Profiles and Tally dataframes
profiles = pd.read_csv("profiles.csv")
tally = pd.read_csv("tally.csv")

# Create a filter widget for the resource_id column
resource_id = st.selectbox("Filter by resource_id", profiles["resource_id"].unique())

# Filter the Profiles and Tally dataframes by the resource_id
profiles_filtered = profiles[profiles["resource_id"] == resource_id]
tally_filtered = tally[tally["resource_id"] == resource_id]

# Display the Profiles and Tally dataframes
st.table(profiles_filtered)
st.table(tally_filtered)
