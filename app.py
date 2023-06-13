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

# Create a new dataframe for the aggregation
agg_tally = tally.groupby(["name", "resource_id", "start_cycle_date", "current_cycle_date", "usage", "allowance"]).agg({"usage": "sum", "allowance": "sum"})

# Create a new dataframe for the aggregation
agg_profiles = profiles.groupby(["uuid"]).agg({"uuid": "count", "contributor_app_name": "value_counts", "type": "value_counts", "role": "nunique"})

# Display the aggregated Tally dataframe
st.table(agg_tally)

# Display the aggregated Profiles dataframe
st.table(agg_profiles)
