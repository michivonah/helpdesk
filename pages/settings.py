import streamlit as st
import dbfunctions as db
import branding
import usermanagement as usr
         
branding.loadBranding()

st.write("""
# Settings
""")
         
if usr.checkLogin():
    st.write('You are logged in')
    newUsername = st.text_input('Username', st.session_state.username)
    newDisplayname = st.text_input('Displayname', db.executeQuery(f"SELECT displayname FROM \"user\" WHERE userid = {st.session_state.userid}")[0][0])
    saveBtn = st.button('Save changes')
    st.info(f"Your UserID: {int(st.session_state.userid)}")
    if saveBtn:
        db.executeWithoutFetch(f"UPDATE \"user\" SET username = '{newUsername}' WHERE userid = {int(st.session_state.userid)};")
        st.success('Username changed', icon="✅")
else:
    usr.showError()
