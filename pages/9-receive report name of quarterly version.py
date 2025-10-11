import streamlit as st
import time


with st.form(key="receive_of_report_name"):

    st.markdown(
        "<h1 style='color:green; text-align:center; font-family:sans-serif;'>Receive Report Name</h1>",
        unsafe_allow_html=True
                )

    st.write("\n")
    st.write("\n")

    st.write("###### Enter The Report Name In Persian That Will Be Displayed On The First Sheet Of The Report File.")
    st.session_state.report_name = st.text_input("no need", label_visibility="hidden")

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
        st.switch_page("pages/1-determine kind of report.py")

if next_button:
    if st.session_state.report_name is None:
        st.write("\n")
        st.warning("fill in the field please!")
        time.sleep(2)
        st.rerun()
    else:
        st.switch_page("pages/10-upload last season report file.py")
