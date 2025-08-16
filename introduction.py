import streamlit as st
from reset_streamlit_session_variables import reset_streamlit_session_variables


if st.session_state.keys():
    reset_streamlit_session_variables()

# ##############################################################################################################

st.set_page_config(initial_sidebar_state="collapsed")    # hides the sidebar

st.write("\n")
st.write("\n")

# Customizing the title using HTML and Markdown
st.markdown(
    "<h1 style='color:blue; text-align:center; font-family:sans-serif;'>Report Generator Application Of Sadad SOC SIEM</h1>",
    unsafe_allow_html=True
)

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

with st.container(border=True):
    st.write("##### You Will Be Asked To Fill In Some Fields That Are Needed To Perform The Task")
    st.write("\n")

    # The following will make the button show up in almost middle of the container frame space
    cols = st.columns(7)
    with cols[3]:
        if st.button("Start"):
            st.switch_page("pages/1-determine kind of report.py")
