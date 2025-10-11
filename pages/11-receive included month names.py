import streamlit as st
import time


with st.form(key="receive_of_month_names"):

    st.write("#### Enter Month Names Of Current Report In Persian")
    st.write("\n")
    st.write("\n")

    st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS = list()

    for i in range(3):
        st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{i + 1}'th month name"))

    st.write("\n")
    st.write("\n")

    # The following will make the button show up in almost middle of the container frame space
    cols = st.columns(7)
    with cols[3]:
        next_button = st.form_submit_button(label="Next")

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

cols = st.columns(9)
with cols[0]:
    if st.button("Back"):
        st.switch_page("pages/10-upload last season report file.py")

if next_button:
    if not all(st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS):
        st.write("\n")
        st.warning("fill in all of the fields please!")
        time.sleep(2)
        st.rerun()
    else:
        st.switch_page("pages/12-upload monthly report files.py")
