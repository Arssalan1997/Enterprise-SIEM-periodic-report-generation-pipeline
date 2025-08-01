import streamlit as st
import time


with st.form(key="receive_of_date_ranges"):

    st.write("#### Enter Date Ranges Of Current Report Weeks")
    st.write("\n")
    st.write("\n")

    st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS = list()

    if st.session_state.number_of_numerical_columns_of_current_month == 4:

        # ----------------------------
        cols = st.columns(2)

        with cols[0]:
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{1}'th date range"))
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{2}'th date range"))

        with cols[1]:
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{3}'th date range"))
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{4}'th date range"))
        # ----------------------------

    elif st.session_state.number_of_numerical_columns_of_current_month == 5:

        # ----------------------------
        cols = st.columns(2)

        with cols[0]:
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{1}'th time range"))
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{2}'th time range"))
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{3}'th time range"))

        with cols[1]:
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{4}'th time range"))
            st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS.append(st.text_input(f"Enter '{5}'th time range"))
        # ----------------------------

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
        st.switch_page("pages/4-upload last month report file.py")

if next_button:
    if not all(st.session_state.LIST_HEADER_NAMES_OF_NUMERICAL_COLUMNS):
        st.write("\n")
        st.warning("fill in all of the fields please!")
        time.sleep(2)
        st.rerun()
    else:
        st.switch_page("pages/6-upload weekly report files.py")
