import streamlit as st


def reset_streamlit_session_variables():
    for key in st.session_state.keys():
        # del st.session_state[key]
        st.session_state[key] = None
        st.session_state.issue_with_aggregation_list = True
