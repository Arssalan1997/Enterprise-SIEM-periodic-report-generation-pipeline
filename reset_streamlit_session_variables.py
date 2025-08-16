import streamlit as st


def reset_streamlit_session_variables():
    st.session_state.clear()
    st.rerun()
