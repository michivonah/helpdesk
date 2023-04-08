import streamlit as st
import dbfunctions
import branding
         
branding.loadBranding()

# create a new ticket
def createTicket(name, desc, customer, assign):
    customerid = dbfunctions.executeQuery(f"SELECT DISTINCT customerid, name from \"customer\" WHERE name = '{customer}';")[0][0]
    userid = dbfunctions.executeQuery(f"SELECT DISTINCT userid, username from \"user\" WHERE username = '{assign}';")[0][0]
    dbfunctions.executeWithoutFetch(f"INSERT INTO ticket (name, description, fk_statusid, fk_userid, fk_customerid) VALUES ('{name}', '{desc}', 1, {userid}, {customerid});")
    st.success("Ticket created", icon="✅")

def loadTicketlist(closed, orderBy):
    if closed:
        st.dataframe(dbfunctions.loadTable(f"SELECT * FROM alltickets ORDER BY \"{orderBy}\""), use_container_width=True)
    else:
        st.dataframe(dbfunctions.loadTable(f"SELECT * FROM alltickets WHERE \"Status\" = 'Open' ORDER BY \"{orderBy}\""), use_container_width=True)

def getCustomerList():
    customerList = dbfunctions.executeQuery(f"SELECT \"name\" FROM customer;")
    customers = ()
    for customer in customerList:
        customers = customers + (customer[0],)
    return customers

st.write("""
# Tickets
""")
         
if 'username' not in st.session_state:
    st.session_state['username'] = "SYSTEM"

ticketList, myTickets, newTicket = st.tabs(["All Tickets", "My Tickets", "Create new ticket"])

with ticketList:
    toggleClose, toggleCustomer = st.columns(2)
    showClosedTickets = toggleClose.checkbox('Show completed tickets')
    orderByName = toggleClose.checkbox('Order by name')
    selectedCustomers = toggleCustomer.multiselect(
    'Choose customers to show',
    getCustomerList())
    if orderByName:
        loadTicketlist(showClosedTickets, 'Ticketname')
    else:
        loadTicketlist(showClosedTickets, 'Ticketnumber')

with myTickets:
    st.dataframe(dbfunctions.loadTable(f"SELECT * FROM alltickets WHERE \"Status\" = 'Open' AND \"Assigned to\" = '{st.session_state.username}' ORDER BY \"Ticketnumber\""), use_container_width=True)

with newTicket:
    with st.container():
        newTicketname = st.text_input('Ticketname')
        customers = getCustomerList()
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

