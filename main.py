import streamlit as st
import hashlib
import branding
import dbfunctions
import time

branding.loadBranding()

def createUser(email, password, username):
    db = dbfunctions.connectDatabase()
    db.execute(f"INSERT INTO \"user\" (username, password, mail, fk_usergroupid) VALUES ('{username}', '{password}', '{email}', 2);")
    st.sidebar.info(f"INSERT INTO \"user\" (username, password, mail, fk_usergroupid) VALUES ('{username}', '{password}', '{email}', 2);")
    st.sidebar.success('Account created.', icon="✅")

def collectUserinfo(email, password):
    username = st.sidebar.text_input('Username')
    createBtn = st.sidebar.button('Register account')
    if createBtn:
        createUser(email, password, username)
    else:
        st.sidebar.warning('Account not created', icon="ℹ️")

def loginUser(email, password):
    db = dbfunctions.connectDatabase()
    db.execute(f"SELECT username from \"user\" WHERE mail = '{email}';")
    result = db.fetchall()
    if result:
        st.info('Welcome back', icon="👋🏻")
    else:
        createUser(email, password, email)

st.write("""
# Helpdesk by Michi
This is a simple helpdesk tool.

[View on Github](https://github.com/michivonah/helpdesk)
""")

st.markdown("# Login")

email = st.sidebar.text_input('Mail')
password = st.sidebar.text_input('Password', type="password")        
loginBtn = st.sidebar.button('Sign in')

if loginBtn:
    st.sidebar.info('Logged in', icon="ℹ️")
    st.session_state['email'] = email
    passwordHashed = hashlib.sha256(password.encode())
    st.session_state['password'] = passwordHashed.hexdigest()
    st.sidebar.info(st.session_state.password)
    loginUser(email, st.session_state.password)
else:
    st.sidebar.info('Logged out', icon="ℹ️")


st.warning('Currently in development. This is a early version.', icon="🐞")

