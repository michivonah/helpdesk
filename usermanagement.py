# User rights management
import streamlit as st

def checkLogin():
    if 'loginSucceed' not in st.session_state:
        st.session_state['loginSucceed'] = False
    loginSucceed = st.session_state.loginSucceed
    return loginSucceed

def showError():
    st.write('You are not logged in. Please log in before accessing the settings.')

def logout():
    st.session_state['loginSucceed'] = False
    st.session_state['username'] = "SYSTEM"
    st.session_state['userid'] = False

""" Example for use in page
import usermanagement as usr 

if usr.checkLogin():
    # Code here
else:
    usr.showError()
"""