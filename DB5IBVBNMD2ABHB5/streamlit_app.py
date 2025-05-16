# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Get the current credentials
session = get_active_session()

# Write directly to the app
st.title(f"Using RAP with SIS")

user = session.sql("SELECT current_user() AS user").collect()[0]['USER']
st.markdown(f"Hello. Your current user is: :blue[{user}]")

user_role = session.sql("SELECT current_role() AS role").collect()[0]['ROLE']
st.markdown(f"Hello. Your current role is: :blue[{user_role}]")

st.markdown("Let's access the `APP_DATA` table")
df = session.table("sandbox.idea.app_data").to_pandas()
st.dataframe(df)