import streamlit as st


st.markdown(
    "<h1 style='color:green; text-align:center; font-family:sans-serif;'>Number of Weeks Specification</h1>",
    unsafe_allow_html=True
)

with st.container(border=True):
    st.write("###### How many weeks does your file include(number of last month weeks)?")

    st.session_state.number_of_numerical_columns_of_last_month = st.radio("no need", [4, 5], key="last_month_number_of_numerical_columns", label_visibility="hidden")

    st.divider()
    st.write("\n")

    st.write("###### How many weeks does your file need to include(number of this month weeks)?")
    st.session_state.number_of_numerical_columns_of_current_month = st.radio("no need", [4, 5], key="current_month_number_of_numerical_columns", label_visibility="hidden")

    cols = st.columns(9)

    with cols[3]:
        if st.button("Next"):
            st.switch_page("pages/3-upload aggregation file.py")

    with cols[5]:
        if st.button("Back"):
            st.switch_page("pages/1-determine kind of report.py")
