import streamlit as st
import psycopg2
import pandas as pd

# Create a connection to database
#@st.cache_resource
def connectDatabase():
    conn = psycopg2.connect(
        host=st.secrets["DBHOST"],
        database="helpdesk",
        user=st.secrets["DBUSER"],
        password=st.secrets["DBPASSWORD"],
        port="5454",)
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor

def executeQuery(query):
    conn = connectDatabase()
    conn.execute(query)
    result = conn.fetchall()
    return result

#@st.cache_data(ttl=30)
def loadTable(query):
    conn = connectDatabase()
    conn.execute(query)
    result = conn.fetchall()
    colnames = [desc[0] for desc in conn.description]
    df = pd.DataFrame(result, columns=colnames)
    return df