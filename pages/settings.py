import streamlit as st
import dbfunctions
import branding
import usermanagement as usr # For detection if user is logged in
         
branding.loadBranding()

st.write("""
# Settings
""")
         
if usr.checkLogin():
    st.write('You are logged in')
    newUsername = st.text_input('Username', st.session_state.username)
    saveBtn = st.button('Save changes')
    st.info(f"Your UserID: {int(st.session_state.userid)}")
    if saveBtn:
        dbfunctions.executeWithoutFetch(f"UPDATE \"user\" SET username = '{newUsername}' WHERE userid = {int(st.session_state.userid)};")
        st.success('Username changed', icon="✅")
else:
    usr.showError()
