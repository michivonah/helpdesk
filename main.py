import streamlit as st
import hashlib

st.set_page_config(
    page_title="Helpdesk by Michi",
    page_icon="🎟️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Helpdesk by Michi von Ah"
    }
)

st.write("""
# Helpdesk by Michi
This is a simple helpdesk tool.

[View on Github](https://github.com/michivonah/helpdesk)
""")
         
loginTab, registerTab = st.sidebar.tabs(["Login", "Register"])

with loginTab:
    st.markdown("# Login")

with registerTab:
    st.markdown("# Register")

email = st.sidebar.text_input('Mail')
password = st.sidebar.text_input('Password', type="password")        
loginBtn = st.sidebar.button('Sign in')

if loginBtn:
    st.sidebar.info('Logged in', icon="ℹ️")
    st.session_state['email'] = email
    passwordHashed = hashlib.sha256(password.encode())
    st.session_state['password'] = passwordHashed.hexdigest()
    st.sidebar.info(st.session_state.password)
else:
    st.sidebar.info('Logged out', icon="ℹ️")


st.warning('Currently in development. This is a early version.', icon="🐞")

