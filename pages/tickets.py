import streamlit as st
from PIL import Image
import psycopg2
import pandas as pd
         
# st.sidebar.markdown("# Your tickets")
# image = Image.open("assets/ticket.png")
# st.sidebar.image(image, caption='Sunrise by the mountains')

# Create a connection to database
def connectDatabase():
    conn = psycopg2.connect(
        host=st.secrets["DBHOST"],
        database="helpdesk",
        user=st.secrets["DBUSER"],
        password=st.secrets["DBPASSWORD"],
        port="5454",)
    cursor = conn.cursor()
    return cursor

# create a new ticket
def createTicket(name):
    db = connectDatabase()
    db.execute("INSERT INTO ticket (name, fk_statusid, fk_userid, fk_customerid) VALUES ('{name}', 1, 1, 1);")

# load tickets from database
def loadTickets():
    db = connectDatabase()
    db.execute("SELECT * FROM alltickets")
    result = db.fetchall()
    colnames = [desc[0] for desc in db.description]
    df = pd.DataFrame(result, columns=colnames)
    st.dataframe(df)

st.write("""
# Tickets
""")


ticketList, newTicket = st.tabs(["Tickets", "Create new ticket"])

with ticketList:
    st.write("""
    Here you can see all your tickets:
    """)
    loadTickets()

with newTicket:
    st.write("""
    Here you can create a new ticket:
    """)
    with st.container():
        newTicketname = st.text_input('Ticketname')
        st.text_input('Description')
        st.selectbox('Customer',('Email', 'Home phone', 'Mobile phone'))
        st.selectbox('Assign to',('Email', 'Home phone', 'Mobile phone'))
        createTicketBtn = st.button('Create ticket')

    if createTicketBtn:
        createTicket(newTicketname)



