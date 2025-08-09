from main import main_function__to_be_called
import streamlit as st
from CONSTANTS import FILES_DIRECTORY_OF_MONTHLY
import os
from returns.pipeline import is_successful
from monthly.handle_errors import else_block_code, except_block_code
from monthly.specify_current_time import specify_current_time


st.session_state.need_to_recalculate_current_time = True
specify_current_time()
st.session_state.need_to_recalculate_current_time = False

# ###########################################################################################################


def save_the_uploaded_files():

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Making The Directory %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    os.makedirs(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.CURRENT_TIME}")

    # the following is inserted since in "pages/8-display report info.py" 'st.session_state.CURRENT_TIME' recreates the
    # current time for unknown reason
    st.session_state.sub_folder_name_of_upload_directory = os.path.basename(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.CURRENT_TIME}")

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Saving Aggregation File %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # Construct the full path for the file
    save_path = os.path.join(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.CURRENT_TIME}", st.session_state.aggregation_file.name)

    # Save the file locally
    with open(save_path, 'wb') as f:
        f.write(st.session_state.aggregation_file.getbuffer())

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Saving Monthly Report File %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # Construct the full path for the file
    save_path = os.path.join(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.CURRENT_TIME}", st.session_state.monthly_report_file.name)

    # Save the file locally
    with open(save_path, 'wb') as f:
        f.write(st.session_state.monthly_report_file.getbuffer())

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Saving Weekly Report Files %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    for weekly_report in st.session_state.weekly_report_files:

        # Construct the full path for the file
        save_path = os.path.join(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.CURRENT_TIME}", weekly_report.name)

        # Save the file locally
        with open(save_path, 'wb') as f:
            f.write(weekly_report.getbuffer())


def do_the_report():
    st.session_state.progress_text = "Operation in progress. Please wait, saving the uploaded files... 3%"
    st.session_state.progress_bar = st.progress(3, text=st.session_state.progress_text)

    save_the_uploaded_files()

    # ******************************************
    # ******************************************

    result = main_function__to_be_called()

    if is_successful(result):
        # print("Success:", result.unwrap())
        else_block_code()
    else:
        # print("Failed:", result.failure())
        except_block_code(result.failure())

    # ******************************************
    # ******************************************


def download_the_report_file(download_after_report_info_is_displayed=False):
    if download_after_report_info_is_displayed is False:
        report_file_fullname = fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.CURRENT_TIME}\Report Made by Automation System.xlsx"
    else:
        report_file_fullname = fr"{st.session_state.target_directory_path_inside_archive}\Report Made by Automation System.xlsx"

    with open(report_file_fullname, "rb") as file:

        cols = st.columns(3)
        with cols[1]:

            st.session_state.download_button = st.download_button(
                label="Download The Report File",
                data=file,
                file_name="Report Made by Automation System.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_btn"
            )

# ###########################################################################################

with st.container(border=True):
    if "report_is_done" not in st.session_state:
        st.session_state.report_is_done = False

        do_the_report()

        if st.session_state.report_is_done is True:
            download_the_report_file()

# ###########################################

if "backspace_is_clicked_after_report_info_displayed" in st.session_state:
    if st.session_state.backspace_is_clicked_after_report_info_displayed is True:
        download_the_report_file(download_after_report_info_is_displayed=True)

# ###########################################

if st.session_state.report_is_done is True:
    st.session_state.progress_text = "Operation is finished."
    st.session_state.progress_bar.progress(100, text=st.session_state.progress_text)

    st.write("\n")
    if st.button("Display The Report Necessary Info To Check"):
        st.switch_page("pages/8-display report info.py")
