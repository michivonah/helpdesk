import streamlit as st
import dbfunctions as db
import branding
         
branding.loadBranding()

# create a new ticket
def createTicket(name, desc, customer, assign):
    customerid = db.executeQuery(f"SELECT DISTINCT customerid, name from \"customer\" WHERE name = '{customer}';")[0][0]
    userid = db.executeQuery(f"SELECT DISTINCT userid, username from \"user\" WHERE username = '{assign}';")[0][0]
    db.executeWithoutFetch(f"INSERT INTO ticket (name, description, fk_statusid, fk_userid, fk_customerid) VALUES ('{name}', '{desc}', 1, {userid}, {customerid});")
    st.success("Ticket created", icon="✅")

def loadTicketlist(closed, orderBy):
    if closed:
        st.dataframe(db.loadTable(f"SELECT * FROM alltickets ORDER BY \"{orderBy}\""), use_container_width=True)
    else:
        st.dataframe(db.loadTable(f"SELECT * FROM alltickets WHERE \"Status\" = 'Open' ORDER BY \"{orderBy}\""), use_container_width=True)

def getSelectableList(field, table):
    listQuery = db.executeQuery(f'SELECT "{field}" FROM "{table}" ORDER BY {field};')
    list = ()
    for listItem in listQuery:
        list = list + (listItem[0],)
    return list

def getSelectableTicketList(query):
    listQuery = db.executeQuery(query)
    list = ()
    for listItem in listQuery:
        list = list + (f"{listItem[0]} - {listItem[1]}",)
    return list

def openTicket(ticketid):
    st.write(f"### Ticket Nr. {ticketid}")
    # get data
    ticketInfo = db.executeQuery(f'SELECT * FROM ticket WHERE ticketid = {ticketid}')
    # build page
    st.markdown(ticketInfo[0][2])
    ticketIdField, ticketNameField = st.columns(2)
    ticketIdField.text_input('Ticket Nr', ticketid, disabled=True)
    ticketName = ticketNameField.text_input('Ticketname', ticketInfo[0][1])
    ticketDescription = st.text_area('Description', ticketInfo[0][2], key="editTicketDesc")
    if int(ticketInfo[0][3]) == 1:
        ticketClosed = st.checkbox('Ticket closed', False)
    else:
        ticketClosed = st.checkbox('Ticket closed', True)
    usersList = list(getSelectableList('username', 'user'))
    assignedName = db.executeQuery(f"SELECT username FROM \"user\" WHERE userid = {ticketInfo[0][5]}")[0][0]
    usersList.remove(assignedName)
    usersList = [assignedName] + usersList
    assignmentBox = st.selectbox('Assign to', usersList)
    saveBtn = st.button('Save changes')
    if saveBtn:
        updateTicket(ticketid, ticketName, ticketDescription, ticketClosed, assignmentBox)

def updateTicket(ticketid, name, desc, closed, assignment):
    if closed:
        closedName = "Closed"
    else:
        closedName = "Open"
    db.executeWithoutFetch(f"UPDATE ticket SET name = '{name}', description = '{desc}', \"fk_statusid\" = (SELECT DISTINCT statusid FROM status WHERE \"name\" = '{closedName}'), \"fk_userid\" = (SELECT DISTINCT userid FROM \"user\" WHERE \"username\" = '{assignment}')  WHERE ticketid = {ticketid};")
    st.success("Ticket modified", icon="✅")
    

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
    st.write("Press **R** for refreshing the ticket list")

with myTickets:
    st.dataframe(db.loadTable(f"SELECT * FROM alltickets WHERE \"Status\" = 'Open' AND \"Assigned to\" = '{st.session_state.username}' ORDER BY \"Ticketnumber\""), use_container_width=True)

with newTicket:
    with st.container():
        newTicketname = st.text_input('Ticketname')
        customers = getSelectableList('name', 'customer')
        users = getSelectableList('username', 'userlist')
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

