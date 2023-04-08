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

def getSelectableList(field, table):
    listQuery = dbfunctions.executeQuery(f'SELECT "{field}" FROM {table};')
    list = ()
    for listItem in listQuery:
        list = list + (listItem[0],)
    return list

def getSelectableTicketList(query):
    listQuery = dbfunctions.executeQuery(query)
    list = ()
    for listItem in listQuery:
        list = list + (f"{listItem[0]} - {listItem[1]}",)
    return list

def openTicket(ticketid):
    st.write(f"### Ticket Nr. {ticketid}")
    # get data
    ticketInfo = dbfunctions.executeQuery(f'SELECT * FROM ticket WHERE ticketid = {ticketid}')
    # build page
    st.markdown(ticketInfo[0][2])
    ticketIdField, ticketNameField = st.columns(2)
    ticketIdField.text_input('Ticket Nr', ticketid, disabled=True)
    ticketNameField.text_input('Ticketname', ticketInfo[0][1], disabled=True)
    st.text_area('Description', ticketInfo[0][2], disabled=True)
    if int(ticketInfo[0][3]) == 1:
        ticketClosed = st.checkbox('Ticket closed', False)
    else:
        ticketClosed = st.checkbox('Ticket closed', True)
    saveBtn = st.button('Save changes')
    if saveBtn:
        updateTicket()

def updateTicket():
    st.warning('Ticket not modified', icon="⚠️")
    

st.write("""
# Tickets
""")
         
if 'username' not in st.session_state:
    st.session_state['username'] = "SYSTEM"

ticketList, myTickets, newTicket, ticketDetails = st.tabs(["All Tickets", "My Tickets", "Create new ticket", "View ticket"])

with ticketList:
    toggleClose, toggleCustomer = st.columns(2)
    showClosedTickets = toggleClose.checkbox('Show completed tickets')
    orderByName = toggleClose.checkbox('Order by name')
    selectedCustomers = toggleCustomer.multiselect(
    'Choose customers to show',
    getSelectableList('name', 'customer'))
    if orderByName:
        loadTicketlist(showClosedTickets, 'Ticketname')
    else:
        loadTicketlist(showClosedTickets, 'Ticketnumber')

with myTickets:
    st.dataframe(dbfunctions.loadTable(f"SELECT * FROM alltickets WHERE \"Status\" = 'Open' AND \"Assigned to\" = '{st.session_state.username}' ORDER BY \"Ticketnumber\""), use_container_width=True)

with newTicket:
    with st.container():
        newTicketname = st.text_input('Ticketname')
        customers = getSelectableList('name', 'customer')
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

with ticketDetails:
    # selectTicket = st.selectbox('Select ticket', getSelectableTicketList('SELECT ticketid, "name" FROM ticket;'))
    selectTicket = st.selectbox('Select ticket', getSelectableList('ticketid', 'ticket'))
    openTicket(selectTicket)

