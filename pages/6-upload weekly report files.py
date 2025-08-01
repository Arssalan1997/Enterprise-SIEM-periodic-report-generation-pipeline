import streamlit as st
import time


st.markdown(
    "<h1 style='color:green; text-align:center; font-family:sans-serif;'>Upload of Weekly Report Files</h1>",
    unsafe_allow_html=True
)

st.session_state.weekly_report_files = list()
st.session_state.number_of_needed_weekly_reports = 2
# ###############################################################################################################
with st.form(key="upload_of_weekly_report_files"):

    # note: why not using loops inside the following 'if' & 'elif': error in next page...
    # if st.session_state.number_of_numerical_columns_of_current_month == 4:

    # ---------------------------------------------------------------------
    st.write("###### Upload '1'th weekly report file please.")
    # NOTE: limiting the file upload to Excel Files only will be implemented later
    st.session_state.first_weekly_report_file = st.file_uploader("no need", label_visibility="hidden",
                                                                 key="'1'th weekly report file upload", type=["xlsx"])
    st.session_state.weekly_report_files.append(st.session_state.first_weekly_report_file)

    st.divider()

    st.write("###### Upload '2'th weekly report file please.")
    # NOTE: limiting the file upload to Excel Files only will be implemented later
    st.session_state.second_weekly_report_file = st.file_uploader("no need", label_visibility="hidden",
                                                                  key="'2'th weekly report file upload", type=["xlsx"])
    st.session_state.weekly_report_files.append(st.session_state.second_weekly_report_file)

    st.divider()

    # ---------------------------------------------------------------------

    st.session_state.third_weekly_report_file = None
    if st.session_state.number_of_numerical_columns_of_current_month == 5:
        st.session_state.number_of_needed_weekly_reports = 3

        # ---------------------------------------------------------------------
        st.write("###### Upload '3'th weekly report file please.")
        # NOTE: limiting the file upload to Excel Files only will be implemented later
        st.session_state.third_weekly_report_file = st.file_uploader("no need", label_visibility="hidden",
                                                                     key="'3'th weekly report file upload", type=["xlsx"])
        st.session_state.weekly_report_files.append(st.session_state.third_weekly_report_file)
        # ---------------------------------------------------------------------

        st.divider()

    # ------------------------------------------------------------------------------
    cols = st.columns(3)
    with cols[1]:
        start_to_do_the_report__button = st.form_submit_button("Start Doing The Report")
# ###############################################################################################################

cols = st.columns(9)
with cols[0]:
    if st.button("Back"):
        st.switch_page("pages/5-receive date ranges.py")

# -----------------------------------------------------------
if start_to_do_the_report__button:

    if st.session_state.number_of_needed_weekly_reports == 2:
        if (st.session_state.first_weekly_report_file is None) or (st.session_state.second_weekly_report_file is None):
            st.warning("fill in all of the fields please!")
            time.sleep(2)
            st.rerun()
        # --------------------------------
        else:
            st.switch_page("pages/7-do the report.py")

    elif st.session_state.number_of_needed_weekly_reports == 3:
        if (st.session_state.first_weekly_report_file is None) or (st.session_state.second_weekly_report_file is None)\
                or (st.session_state.third_weekly_report_file is None):
            st.warning("fill in all of the fields please!")
            time.sleep(2)
            st.rerun()
        # --------------------------------
        else:
            st.switch_page("pages/7-do the report.py")
