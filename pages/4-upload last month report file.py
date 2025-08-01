import streamlit as st
import time


with st.form(key="monthly_report_file_upload"):

    st.markdown(
        "<h1 style='color:green; text-align:center; font-family:sans-serif;'>Upload Last Month Report File</h1>",
        unsafe_allow_html=True
                )

    st.session_state.monthly_report_file = st.file_uploader("no need", label_visibility="hidden", type=["xlsx"])

    st.write("\n")
    st.write("\n")

    # The following will make the button show up in almost middle of the container frame space
    cols = st.columns(7)
    with cols[3]:
        next_button = st.form_submit_button(label="Next")

# ----------------------------------------------------------------------
cols = st.columns(9)
with cols[0]:
    if st.button("Back"):
        st.switch_page("pages/3-upload aggregation file.py")

if next_button:
    if st.session_state.monthly_report_file is None:
        st.write("\n")
        st.warning("Upload the file please!")
        time.sleep(2)
        st.rerun()
    else:
        st.switch_page("pages/5-receive date ranges.py")
