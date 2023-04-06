import streamlit as st
from PIL import Image
import psycopg2
import pandas as pd

st.write("""
# Your tickets
Here you can see all your tickets:
""")
         
# st.sidebar.markdown("# Your tickets")
# image = Image.open("assets/ticket.png")
# st.sidebar.image(image, caption='Sunrise by the mountains')

conn = psycopg2.connect(
    host=st.secrets["DBHOST"],
    database="helpdesk",
    user=st.secrets["DBUSER"],
    password=st.secrets["DBPASSWORD"],
    port="5454",)

cursor = conn.cursor()

cursor.execute("SELECT * FROM alltickets")

result = cursor.fetchall()
colnames = [desc[0] for desc in cursor.description]
df = pd.DataFrame(result, columns=colnames)
st.dataframe(df)

with st.container():
    st.write('### Create new ticket')
    st.text_input('Ticketname')
    st.text_input('Description')
    st.selectbox('Customer',('Email', 'Home phone', 'Mobile phone'))
    st.selectbox('Assign to',('Email', 'Home phone', 'Mobile phone'))
    st.button('Create ticket')
