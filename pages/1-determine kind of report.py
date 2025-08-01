import streamlit as st


with st.container(border=True):

    st.write("### What Kind Of Report You Want To Be Made?")

    st.session_state.report_type = st.radio("no need", ["Weekly", "Monthly", "Quarterly"], label_visibility="hidden")

    st.write("\n")
    st.write("\n")
    st.write("\n")

    cols = st.columns(7)

    with cols[3]:
        if st.button("Proceed"):

            if st.session_state.report_type == "Weekly":
                st.switch_page("pages/fill weekly report parameters.py")

            elif st.session_state.report_type == "Monthly":
                st.switch_page("pages/2-determine number of last and current weeks of monthly report.py")

            elif st.session_state.report_type == "Quarterly":
                st.switch_page("pages/fill quarterly report parameters.py")
