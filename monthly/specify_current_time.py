import streamlit as st
from datetime import datetime


def specify_current_time():
    if st.session_state.need_to_recalculate_current_time is True:

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        st.session_state.CURRENT_TIME = current_time
