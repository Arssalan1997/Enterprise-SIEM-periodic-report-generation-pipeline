import streamlit as st
from CONSTANTS import LOGS_DIRECTORY, CURRENT_TIME
import time


def else_block_code():
    st.session_state.report_is_done = True

    st.session_state.progress_text = "Operation is finished."
    st.session_state.progress_bar.progress(100, text=st.session_state.progress_text)

    time.sleep(0.2)
    st.write("\n")
    st.write("\n")
    st.success("The Report Is Ready.")
    st.write("\n")


def except_block_code(error):

    def log_if_error_happens(_error):
        error_logs_filepath = rf'{LOGS_DIRECTORY}\error logs.txt'

        with open(error_logs_filepath, 'a') as f:
            f.write('\n')
            f.write('\n')
            f.write(f"{CURRENT_TIME} - error -- '{_error}'")

    # --------------------------------------------------------------------
    st.session_state.report_is_done = False

    with st.container(border=True):
        st.write("\n")

        st.warning("Something went wrong due to issues with uploaded files, "
                   "Please Contact The Developer Team Of The Tool!")
        st.write("\n")
        st.write("\n")

        st.markdown(
            "<h1 style='color:blue; text-align:center; '>You can try again if you know what file(s) were uploaded incorrectly</h1>",
            unsafe_allow_html=True
        )
        # st.write("You can try again if you know what file(s) were uploaded incorrectly")

    log_if_error_happens(error)
