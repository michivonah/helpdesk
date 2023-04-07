import streamlit as st
import dbfunctions
import branding
         
branding.loadBranding()

# create a new ticket
def createTicket(name, desc, customer, assign):
    customerid = dbfunctions.executeQuery(f"SELECT DISTINCT customerid, name from \"customer\" WHERE name = '{customer}';")[0][0]
    userid = dbfunctions.executeQuery(f"SELECT DISTINCT userid, username from \"user\" WHERE username = '{assign}';")[0][0]
    dbfunctions.executeWithoutFetch(f"INSERT INTO ticket (name, description, fk_statusid, fk_userid, fk_customerid) VALUES ('{name}', '{desc}', 1, {userid}, {customerid});")

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
        customers = ()
        for customer in customerList:
            customers = customers + (customer[0],)
        userList = dbfunctions.executeQuery(f"SELECT username FROM \"user\";")
        users = ()
        for user in userList:
            users = users + (user[0],)
        ticketDescription = st.text_area('Description')
        ticketCustomer = st.selectbox('Customer', customers)
        ticketAssignment = st.selectbox('Assign to', users)
        createTicketBtn = st.button('Create ticket')

    if createTicketBtn:
        createTicket(newTicketname, ticketDescription, ticketCustomer, ticketAssignment)

