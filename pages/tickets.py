import streamlit as st
import pandas as pd
import dbfunctions
import branding
         
branding.loadBranding()

# create a new ticket
def createTicket(name):
    db = dbfunctions.connectDatabase()
    db.execute("INSERT INTO ticket (name, fk_statusid, fk_userid, fk_customerid) VALUES ('{name}', 1, 1, 1);")

# load tickets from database
@st.cache_data(ttl=120)
def loadTickets():
    db = dbfunctions.connectDatabase()
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



