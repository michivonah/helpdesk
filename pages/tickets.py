import streamlit as st
import dbfunctions
import branding
         
branding.loadBranding()

# create a new ticket
def createTicket(name, desc):
    dbfunctions.executeQuery(f"INSERT INTO ticket (name, description, fk_statusid, fk_userid, fk_customerid) VALUES ('{name}', '{desc}', 1, 1, 1);")

st.write("""
# Tickets
""")

ticketList, myTickets, newTicket = st.tabs(["All Tickets", "My Tickets", "Create new ticket"])

with ticketList:
    showClosedTickets = st.checkbox('Show completed tickets')
    if showClosedTickets:
        st.dataframe(dbfunctions.loadTable("SELECT * FROM alltickets ORDER BY \"Ticketnumber\""), use_container_width=True)
    else:
        st.dataframe(dbfunctions.loadTable("SELECT * FROM alltickets WHERE \"Status\" = 'Open' ORDER BY \"Ticketnumber\""), use_container_width=True)

with myTickets:
    st.dataframe(dbfunctions.loadTable(f"SELECT * FROM alltickets WHERE \"Status\" = 'Open' AND \"Assigned to\" = '{st.session_state.username}' ORDER BY \"Ticketnumber\""), use_container_width=True)

with newTicket:
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

