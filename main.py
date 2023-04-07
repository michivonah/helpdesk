import streamlit as st
import hashlib
import branding
import dbfunctions

branding.loadBranding()

def createUser(email, password, username):
    db = dbfunctions.connectDatabase()
    db.execute(f"INSERT INTO \"user\" (username, password, mail, fk_usergroupid) VALUES ('{username}', '{password}', '{email}', 2);")
    st.sidebar.success('Account created.', icon="✅")

def collectUserinfo(email, password):
    username = st.sidebar.text_input('Username')
    createBtn = st.sidebar.button('Register account')
    if createBtn:
        createUser(email, password, username)
    else:
        st.sidebar.warning('Account not created', icon="ℹ️")

def loginUser(email, password):
    userdata = dbfunctions.executeQuery(f"SELECT DISTINCT username, password from \"user\" WHERE mail = '{email}';")
    if userdata:
        for value in userdata:
            correctPW = value[1]
        if password == correctPW:
            st.info('Welcome back', icon="👋🏻")
        else:
            st.warning('Wrong password')
    else:
        createUser(email, password, email)

st.write("""
# Helpdesk by Michi
This is a simple helpdesk tool.

[View on Github](https://github.com/michivonah/helpdesk)
""")

st.sidebar.markdown("# Login")

email = st.sidebar.text_input('Mail')
password = st.sidebar.text_input('Password', type="password")        
loginBtn = st.sidebar.button('Sign in')

if loginBtn:
    st.sidebar.info('Logged in', icon="ℹ️")
    st.session_state['email'] = email
    passwordHashed = hashlib.sha256(password.encode())
    st.session_state['password'] = passwordHashed.hexdigest()
    loginUser(email, st.session_state.password)
else:
    st.sidebar.info('Logged out', icon="ℹ️")


st.warning('Currently in development. This is a early version.', icon="🐞")

