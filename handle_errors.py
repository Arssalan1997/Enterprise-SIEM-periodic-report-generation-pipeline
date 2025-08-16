import streamlit as st
from CONSTANTS import LOGS_DIRECTORY
import time
from reset_streamlit_session_variables import reset_streamlit_session_variables


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
            f.write(f"{st.session_state.CURRENT_TIME} - error -- '{_error}'")

    # --------------------------------------------------------------------
    st.session_state.report_is_done = False

    log_if_error_happens(error)

    # ############################################################################

    st.write("\n")
    st.write("\n")
    st.warning("The Report Was Failed Most Probably Because Of Incorrect Uploads!")
    time.sleep(1)
    st.write("\n")
    st.success("You Can Retry If You Know What Input(s) Were Made Incorrectly With Correct Ones!")
    time.sleep(1)
    st.write("\n")
    st.warning("Please Contact The Developer Team Of The Tool To Check The Logs If You Are Certain That You Filled All Correctly")
    st.write("\n")
    st.write("\n")

    time.sleep(1)
    st.session_state.progress_bar.empty()

    st.divider()

    # resetting 'st.session_state' variables
    reset_streamlit_session_variables()

    cols = st.columns(3)
    with cols[1]:
        if st.button("Retry With New Items"):
            st.switch_page("introduction.py")
