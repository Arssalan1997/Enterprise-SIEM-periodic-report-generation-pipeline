import streamlit as st


with st.container(border=True):
    st.write("#### Quarterly Report Version Of The Automation Will Be Developed in Next Seasons of The Year.")
    st.write("\n")
    st.write("\n")

    cols = st.columns(7)
    with cols[3]:
        if st.button("Back"):
            st.switch_page("pages/1-determine kind of report.py")
