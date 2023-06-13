import streamlit as st
import pandas as pd

# Load the Profiles and Tally dataframes
#profiles = pd.read_csv("profiles.csv")
tally = pd.read_csv("tally.csv")

# convert to datetime
tally['start_cycle_date'] = pd.to_datetime(tally['start_cycle_date'])
tally['current_cycle_date'] = pd.to_datetime(tally['current_cycle_date'])

# convert date to year-month-day
tally['start_cycle_date'] = tally['start_cycle_date'].dt.strftime('%Y-%m-%d')
tally['current_cycle_date'] = tally['current_cycle_date'].dt.strftime('%Y-%m-%d')


# Create a list of ids
ids = tally["resource_id"].unique()

# Create a drop down menu for the id
id = st.selectbox("Select an id", ids)

# If an id is selected, read the corresponding Profiles dataframe
if id:
  profiles = pd.read_csv(f"profiles_{id}.csv")
 
  # Create a new dataframe for the aggregation
  org = tally[tally.resource_id == id]
  
  high_level = pd.DataFrame()
  high_level['org_name'] = org['name']
  high_level['org_id'] = org['resource_id']
  #high_level['num_team_members'] = num_team_members
  high_level['became_customer_at'] = org['customer_join_date']
  high_level['allowed_views'] = org['allowance']
  high_level['credits_used'] = org['usage']
  high_level['prcnt_used'] = round(org['usage'] / org['allowance'], 2)
  high_level['current_cycle_start_date'] = org['start_cycle_date']
  high_level['cycle_length'] = org['current_cycle_date'] - org['start_cycle_date']
  high_level['days_left_in_cycle'] = 365 - high_level['cycle_length'].dt.days 
  high_level['prcnt_in_cycle'] = round(high_level['cycle_length'].dt.days  / 365, 2)
  # set first row to be index 
  high_level = high_level.set_index('org_name')
  
  
  
# Display the aggregated Tally dataframe
st.table(high_level)

