import streamlit as st
from CONSTANTS import FILES_DIRECTORY_OF_MONTHLY, ARCHIVE_FILE_DIRECTORY__OF_MONTHLY_REPORT
import os
import shutil

# ###########################################################################################


def copy_all_files_from_files_directory_to_archive_directory():

    # ------------------ Making the target directory ------------------

    # make the corresponding directory
    st.session_state.target_directory_path_inside_archive = fr"{ARCHIVE_FILE_DIRECTORY__OF_MONTHLY_REPORT}\{st.session_state.sub_folder_name_of_upload_directory}"

    os.makedirs(st.session_state.target_directory_path_inside_archive)

    # ---------------------- Coping All The Files ---------------------
    # Copy each file
    for file_name in os.listdir(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.sub_folder_name_of_upload_directory}"):
        src_path = os.path.join(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.sub_folder_name_of_upload_directory}", file_name)
        dst_path = os.path.join(st.session_state.target_directory_path_inside_archive, file_name)

        shutil.copy2(src_path, dst_path)  # copy2 preserves metadata


def delete_directory_holding_the_uploaded_files_recursively():
    shutil.rmtree(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.sub_folder_name_of_upload_directory}")

# ###########################################################################################

# ####################################### Part 1: Display Results Of Operations ####################################
# #######################################                                       ####################################


with st.container(border=True):
    # ----------------------------------------
    st.markdown(
        "<h1 style='color:green; text-align:center; font-family:sans-serif;'>Considerations About The Generated Report</h1>",
        unsafe_allow_html=True
    )
    st.write("\n")
    st.write("\n")

    # ---------  Display Messages With '0' As Aggregation Value of Worksheets That Have Aggregation Column ------------

    if st.session_state.issue_with_aggregation_list is True:
        st.write("There Is Something Wrong With The Aggregation File Which Needs To Be Checked By The Admin Of"
                 "The Automation Application!\nTry To Fill ّFields Of The Aggregation Columns Of First Worksheets Manually.")

    else:
        no_need_to_show__df__messages_with_zero_as_aggregation_value_in_some_worksheets = st.session_state.\
            df__messages_with_zero_as_aggregation_value_in_some_worksheets["Messages With \'0\' as Aggregation Value"].\
            apply(lambda x: x == []).all()

        if no_need_to_show__df__messages_with_zero_as_aggregation_value_in_some_worksheets:
            st.write("There Were No Messages With '0' As Aggregation Value In First 3 Worksheets Of Monthly Report File.")

        elif not no_need_to_show__df__messages_with_zero_as_aggregation_value_in_some_worksheets:
            st_write_output = f"The following shows info of messages with '0' as their aggregation value. There is no " \
                              f"corresponding record within '{st.session_state.aggregation_file.name}'.\nYou need to check the SIEM for the newly made " \
                              f"aggregation values and add them to the aggregation list file\nand also manually fill the aggregation" \
                              f" values within your Monthly Report File."
            st.write(st_write_output)
            st.dataframe(st.session_state.df__messages_with_zero_as_aggregation_value_in_some_worksheets)

    st.divider()
    st.write("\n")

    # -----------------------------------------  Display Sheets With Issues -----------------------------------

    if len(st.session_state.list_of_sheet_names_with_issues) == 0:
        st.write(f"There Are No Sheets With Issues in '{st.session_state.monthly_report_file.name}' file")

    else:
        st.write(f"'{len(st.session_state.list_of_sheet_names_with_issues)}' sheets remained unchanged since had"
                 f" issues. You can view its titles in the following table.\n")
        st.dataframe(st.session_state.df__sheet_names_with_issues_in_report_file)

    st.divider()
    st.write("\n")

    # --------------------------  Display SheetNames With Issues Of Weekly Report Files ------------------------

    no_need_to_show__df__sheet_names_with_issues_in_weekly_report_files = st.session_state.\
        df__sheet_names_with_issues_in_weekly_report_files['SheetNames With Issues'].apply(lambda x: x == []).all()

    if no_need_to_show__df__sheet_names_with_issues_in_weekly_report_files:
        st.write("There Are No Issues With Sheets Of Weekly Report Files.")

    elif not no_need_to_show__df__sheet_names_with_issues_in_weekly_report_files:
        st.write("The following Table Shows SheetNames Of Corresponding Weekly Report Files That Have Issues Making It "
                 "Impossible To Transfer Data To Monthly Report File.")
        st.dataframe(st.session_state.df__sheet_names_with_issues_in_weekly_report_files)

    st.divider()
    st.write("\n")

    # --------- Display SheetNames Not Found In 'Monthly Report to Weekly Report Mapping.csv' file ------------

    no_need_to_show__df__sheet_names_not_found_in_mapping_file = st.\
        session_state.df__sheet_names_not_found_in_mapping_file['SheetName'].apply(lambda x: x == []).all()

    if no_need_to_show__df__sheet_names_not_found_in_mapping_file:
        st.write("All The Weekly Report Files have been found in 'Monthly Report to Weekly Report Mapping.csv' file. No"
                 "further check is required")

    elif not no_need_to_show__df__sheet_names_not_found_in_mapping_file:
        st.write("The following Table Shows SheetNames That Are Found In Their Corresponding Weekly Report Files, But "
                 "Not Found In 'Monthly Report to Weekly Report Mapping.csv' file.\nPlease check whether you need to "
                 "add new sheet and record to the monthly report Excel spreadsheet file and also the "
                 "'Monthly Report to Weekly Report Mapping.csv' mapping file.(The mapping file must be edited by "
                 "The Automation System Developer)\n")
        st.dataframe(st.session_state.df__sheet_names_not_found_in_mapping_file)
    # --------------------------------------

st.write("\n")
st.session_state.backspace_is_clicked_after_report_info_displayed = False
cols = st.columns(9)
with cols[0]:
    if st.button("Back"):
        st.session_state.backspace_is_clicked_after_report_info_displayed = True
        st.switch_page("pages/7-do the report for monthly version.py")

# ############################# Part 2: Transfer The Files To The Archive Directory ##############################
# #############################                                                     ##############################

if "move_files_to_archive_directory__is_done" not in st.session_state:

    copy_all_files_from_files_directory_to_archive_directory()
    delete_directory_holding_the_uploaded_files_recursively()

    st.session_state.move_files_to_archive_directory__is_done = True
