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
# Helpdesk by Michi
This is a simple helpdesk tool.

[View on Github](https://github.com/michivonah/helpdesk)
""")
                  
st.sidebar.markdown("# Login")

username = st.sidebar.text_input('Username')

password = st.sidebar.text_input('Password')

st.sidebar.button('Sign in')

st.error('Please connect to a database!', icon="💽")

