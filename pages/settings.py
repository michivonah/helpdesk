import streamlit as st
import dbfunctions
import branding
         
branding.loadBranding()

st.write("""
# Settings
""")
         
if st.session_state.loginSucceed:
    st.write('You are logged in')
    newUsername = st.text_input('Username', st.session_state.username)
    saveBtn = st.button('Save changes')
    st.info(f"Your UserID: {int(st.session_state.userid)}")
else:
    st.write('You are not logged in. Please log in before accessing the settings.')

if saveBtn:
    dbfunctions.executeQuery(f"UPDATE \"user\" SET username = '{newUsername}' WHERE userid = {int(st.session_state.userid)};")
    st.success('Username changed', icon="✅")