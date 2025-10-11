import streamlit as st
from CONSTANTS import FILES_DIRECTORY_OF_QUARTERLY, ARCHIVE_FILE_DIRECTORY__OF_QUARTERLY_REPORT
import os
import shutil

# ###########################################################################################


def copy_all_files_from_files_directory_to_archive_directory():

    # ------------------ Making the target directory ------------------

    # make the corresponding directory
    st.session_state.target_directory_path_inside_archive = fr"{ARCHIVE_FILE_DIRECTORY__OF_QUARTERLY_REPORT}\{st.session_state.sub_folder_name_of_upload_directory}"

    os.makedirs(st.session_state.target_directory_path_inside_archive)

    # ---------------------- Coping All The Files ---------------------
    # Copy each file
    for file_name in os.listdir(fr"{FILES_DIRECTORY_OF_QUARTERLY}\{st.session_state.sub_folder_name_of_upload_directory}"):
        src_path = os.path.join(fr"{FILES_DIRECTORY_OF_QUARTERLY}\{st.session_state.sub_folder_name_of_upload_directory}", file_name)
        dst_path = os.path.join(st.session_state.target_directory_path_inside_archive, file_name)

        shutil.copy2(src_path, dst_path)  # copy2 preserves metadata


def delete_directory_holding_the_uploaded_files_recursively():
    shutil.rmtree(fr"{FILES_DIRECTORY_OF_QUARTERLY}\{st.session_state.sub_folder_name_of_upload_directory}")

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

    # -----------------------------------------  Display Sheets With Issues -----------------------------------

    if len(st.session_state.list_of_sheet_names_with_issues) == 0:
        st.write(f"There Are No Sheets With Issues in '{st.session_state.quarterly_report_file.name}' file")

    else:
        st.write(f"'{len(st.session_state.list_of_sheet_names_with_issues)}' sheets remained unchanged since had"
                 f" issues. You can view its titles in the following table.\n")
        st.dataframe(st.session_state.df__sheet_names_with_issues_in_report_file)

    st.divider()
    st.write("\n")

    # --------------------------  Display SheetNames With Issues Of Monthly Report Files ------------------------

    no_need_to_show__df__sheet_names_with_issues_in_monthly_report_files = st.session_state.\
        df__sheet_names_with_issues_in_monthly_report_files['SheetNames With Issues'].apply(lambda x: x == []).all()

    if no_need_to_show__df__sheet_names_with_issues_in_monthly_report_files:
        st.write("There Are No Issues With Sheets Of Monthly Report Files.")

    elif not no_need_to_show__df__sheet_names_with_issues_in_monthly_report_files:
        st.write("The following Table Shows SheetNames Of Corresponding Monthly Report Files That Have Issues Making "
                 "It Impossible To Transfer Data To Quarterly Report File.")
        st.dataframe(st.session_state.df__sheet_names_with_issues_in_monthly_report_files)

    st.divider()
    st.write("\n")

    # --------- Display SheetNames Not Found In 'Quarterly Report to Monthly Report Mapping.csv' file ------------

    no_need_to_show__df__sheet_names_not_found_in_mapping_file = st.\
        session_state.df__sheet_names_not_found_in_mapping_file['SheetName'].apply(lambda x: x == []).all()

    if no_need_to_show__df__sheet_names_not_found_in_mapping_file:
        st.write("All The Monthly Report Files have been found in 'Quarterly Report to Monthly Report Mapping.csv' "
                 "file. No further check is required")

    elif not no_need_to_show__df__sheet_names_not_found_in_mapping_file:
        st.write("The following Table Shows SheetNames That Are Found In Their Corresponding Monthly Report Files, But "
                 "Not Found In 'Quarterly Report to Monthly Report Mapping.csv' file.\nPlease check whether you need "
                 "to add new sheet and record to the quarterly report Excel spreadsheet file and also the "
                 "'Quarterly Report to Monthly Report Mapping.csv' mapping file.(The mapping file must be edited by "
                 "The Automation System Developers)\n")
        st.dataframe(st.session_state.df__sheet_names_not_found_in_mapping_file)
    # --------------------------------------

st.write("\n")
st.session_state.backspace_is_clicked_after_report_info_displayed = False
cols = st.columns(9)
with cols[0]:
    if st.button("Back"):
        st.session_state.backspace_is_clicked_after_report_info_displayed = True
        st.switch_page("pages/13-do the report for quarterly version.py")

# ############################# Part 2: Transfer The Files To The Archive Directory ##############################
# #############################                                                     ##############################

if "move_files_to_archive_directory__is_done" not in st.session_state:

    copy_all_files_from_files_directory_to_archive_directory()
    delete_directory_holding_the_uploaded_files_recursively()

    st.session_state.move_files_to_archive_directory__is_done = True
