import streamlit as st
import pandas as pd
import dbfunctions
import branding
         
branding.loadBranding()

# create a new ticket
def createTicket(name, desc):
    dbfunctions.executeQuery(f"INSERT INTO ticket (name, description, fk_statusid, fk_userid, fk_customerid) VALUES ('{name}', '{desc}', 1, 1, 1);")

# load tickets from database
#@st.cache_data(ttl=30)
def loadTickets():
    db = dbfunctions.connectDatabase()
    db.execute("SELECT * FROM alltickets")
    result = db.fetchall()
    colnames = [desc[0] for desc in db.description]
    df = pd.DataFrame(result, columns=colnames)
    return df

st.write("""
# Tickets
""")

ticketList, newTicket = st.tabs(["Tickets", "Create new ticket"])

with ticketList:
    st.write("""
    Here you can see all your tickets:
    """)
    st.dataframe(loadTickets())

with newTicket:
    st.write("""
    Here you can create a new ticket:
    """)
    with st.container():
        newTicketname = st.text_input('Ticketname')
        customerList = dbfunctions.executeQuery(f"SELECT \"name\" FROM customer;")
        userList = dbfunctions.executeQuery(f"SELECT username FROM \"user\";")
        ticketDescription = st.text_area('Description')
        st.selectbox('Customer', customerList)
        st.selectbox('Assign to', userList)
        createTicketBtn = st.button('Create ticket')

    if createTicketBtn:
        createTicket(newTicketname, ticketDescription)



