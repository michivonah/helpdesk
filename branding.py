import streamlit as st
from PIL import Image

def loadBranding():
    st.set_page_config(
        page_title="mangoTicket",
        page_icon="logo/logo.png",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "### mangoTicket by Michi \n [View on Github](https://github.com/michivonah/helpdesk)"
        }
    )
    # st.sidebar.markdown('### Helpdesk')
    #logo = Image.open('logo/logo.png')
    #st.sidebar.image(logo)