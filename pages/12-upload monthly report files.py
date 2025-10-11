import streamlit as st
import time


st.markdown(
    "<h1 style='color:green; text-align:center; font-family:sans-serif;'>Upload of Monthly Report Files</h1>",
    unsafe_allow_html=True
)

st.session_state.monthly_report_files = list()

# ###############################################################################################################
with st.form(key="upload_of_monthly_report_files"):

    for i in range(3):
        st.write(f"###### Upload '{i + 1}'th monthly report file please.")
        monthly_report_file = st.file_uploader("no need", label_visibility="hidden",
                                               key=f"'{i + 1}'th monthly report file upload", type=["xlsx"])

        st.session_state.monthly_report_files.append(monthly_report_file)
        st.divider()

    cols = st.columns(3)
    with cols[1]:
        start_to_do_the_report__button = st.form_submit_button("Start Doing The Report")
# ###############################################################################################################

cols = st.columns(9)
with cols[0]:
    if st.button("Back"):
        st.switch_page("pages/11-receive included month names.py")

# -----------------------------------------------------------
if start_to_do_the_report__button:
    if not all(st.session_state.monthly_report_files):
        st.write("\n")
        st.warning("do all the uploads please!")
        time.sleep(2)
        st.rerun()

    else:
        st.switch_page("pages/13-do the report for quarterly version.py")
