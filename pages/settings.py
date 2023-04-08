import streamlit as st
import dbfunctions
import branding
         
branding.loadBranding()

st.write("""
# Settings
""")
         
if 'loginSucceed' not in st.session_state:
    st.session_state['loginSucceed'] = False
         
if st.session_state.loginSucceed:
    st.write('You are logged in')
    newUsername = st.text_input('Username', st.session_state.username)
    saveBtn = st.button('Save changes')
    st.info(f"Your UserID: {int(st.session_state.userid)}")
    if saveBtn:
        dbfunctions.executeWithoutFetch(f"UPDATE \"user\" SET username = '{newUsername}' WHERE userid = {int(st.session_state.userid)};")
        st.success('Username changed', icon="✅")
else:
    st.write('You are not logged in. Please log in before accessing the settings.')
