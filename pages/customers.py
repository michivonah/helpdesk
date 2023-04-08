import streamlit as st
import dbfunctions
import branding

branding.loadBranding()

st.write("""
# Customers
Here you can see all customers:
""")

customerList = st.tabs(["All customers"])

with customerList:
    st.dataframe(dbfunctions.loadTable(f"SELECT * FROM alltickets WHERE \"Status\" = 'Open' AND \"Assigned to\" = '{st.session_state.username}' ORDER BY \"Ticketnumber\""), use_container_width=True)