import streamlit as st
import datetime
import dbfunctions
import branding

branding.loadBranding()

def createCustomer(custname, mail, phone, address, website, birthdate, notes):
    dbfunctions.executeWithoutFetch(f"INSERT INTO \"customer\" (\"name\", mail, phone, address, website, birthdate, notes) VALUES ('{custname}', '{mail}', '{phone}', '{address}', '{website}', '{birthdate}', '{notes}');")
    st.success("New customer created successfully", icon="✅")

st.write("""
# Customers
Here you can see all customers:
""")

customerList, newCustomer = st.tabs(["All customers", "Create new customer"])

with customerList:
    st.dataframe(dbfunctions.loadTable(f"SELECT * FROM allcustomers"), use_container_width=True)

with newCustomer:
    with st.container():
        newCustomerName = st.text_input('Customer Name')
        newCustomerMail = st.text_input('E-Mail Address', placeholder="example@example.com")
        newCustomerPhone = st.text_input('Phone', placeholder="+41791234567")
        newCustomerURL = st.text_input('Website', placeholder="https://example.com")
        newCustomerAddress = st.text_area('Address', placeholder="Example Street 11\n6003 Lucerne")
        newCustomerBirthdate = st.date_input('Birthdate', min_value=datetime.date(1900, 1, 1))
        newCustomerNotes = st.text_area('Notes')
        createCustomerBtn = st.button('Create customer')

        if createCustomerBtn:
            createCustomer(newCustomerName, newCustomerMail, newCustomerPhone, newCustomerAddress, newCustomerURL, newCustomerBirthdate, newCustomerNotes)

