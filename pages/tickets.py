import streamlit as st
import psycopg2
import pandas as pd
import numpy as np

st.write("""
# My tickets
""")
         
st.sidebar.markdown("# My tickets")

conn = psycopg2.connect(
    host="helpdesk-db",
    database="helpdesk",
    user="helpdesk",
    password="password",
    port="5454",)

cursor = conn.cursor()

cursor.execute("SELECT * FROM alltickets")

print(cursor.fetchall())