import streamlit as st

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
# Helpdesk
This is a simple helpdesk tool.

[View on Github](https://github.com/michivonah/helpdesk)
""")
                  
st.sidebar.markdown("# Helpdesk")

st.button('Load tickets')

username = st.text_input('Username')

password = st.text_input('Password')

st.button('Sign in')

st.error('Please connect to a database!', icon="💽")

