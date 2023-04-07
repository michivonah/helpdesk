import streamlit as st
from PIL import Image

def loadBranding():
    st.set_page_config(
        page_title="Helpdesk by Michi",
        page_icon="🎟️",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "### Helpdesk by Michi von Ah \n [View on Github](https://github.com/michivonah/helpdesk)"
        }
    )
    # st.sidebar.markdown('### Helpdesk')
    #logo = Image.open('pages/assets/ticket.png')
    #st.sidebar.image(logo)