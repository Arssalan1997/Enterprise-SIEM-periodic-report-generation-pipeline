import streamlit as st
from datetime import datetime
from CONSTANTS import FILES_DIRECTORY, LOGS_DIRECTORY, ARCHIVE_FILE_DIRECTORY__OF_UNSUCCESSFUL_MONTHLY_REPORT
import win32com.client as win32
import os
import shutil
import time


error_logs_filepath = rf'{LOGS_DIRECTORY}\error logs.txt'
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # generates log time applying the provided format


def log_if_error_happens(error):
    # error_logs_filepath = rf'{LOGS_DIRECTORY}\error logs.txt'
    with open(error_logs_filepath, 'a') as f:
        f.write('\n')  # added to protect that the last log has been added right after a '\n' from the last log
        # (there is possibility that before blocking last time the log file being open and the last '\n'
        # being removed)
        f.write(f"{current_time} - error -- '{error}'")


def close_open_files():
    pass

    # try:
    #     excel = win32.Dispatch("Excel.Application")
    #     if excel.Workbooks.Count > 0:
    #         excel.DisplayAlerts = False
    #         excel.Workbooks.Close(SaveChanges=True)
    #         excel.Quit()
    # except Exception as e:
    #     with open(error_logs_filepath, 'a') as f:
    #         f.write(f"__ {e}")


def copy_files():
    # make the corresponding directory
    target_directory_path_inside_archive = fr"{ARCHIVE_FILE_DIRECTORY__OF_UNSUCCESSFUL_MONTHLY_REPORT}\{current_time}"
    os.makedirs(target_directory_path_inside_archive)

    # ---------------------- Coping All The Files ---------------------
    # Copy each file
    for file_name in os.listdir(FILES_DIRECTORY):
        src_path = os.path.join(FILES_DIRECTORY, file_name)
        dst_path = os.path.join(target_directory_path_inside_archive, file_name)

        shutil.copy2(src_path, dst_path)  # copy2 preserves metadata


def delete_files():
    for file_name in os.listdir(FILES_DIRECTORY):
        filepath = os.path.join(FILES_DIRECTORY, file_name)
        os.remove(filepath)


# ##############################################################################################

def except_block_code(error):
    st.session_state.report_is_done = False

    st.error(f"{error}\nPlease Contact The Developer Team Of The Tool!")

    log_if_error_happens(error)
    close_open_files()
    copy_files()
    delete_files()


def else_block_code():
    st.session_state.report_is_done = True

    st.session_state.progress_text = "Operation is finished."
    st.session_state.progress_bar.progress(100, text=st.session_state.progress_text)

    time.sleep(0.2)
    st.write("\n")
    st.write("\n")
    st.success("The Report Is Ready.")
    # st.success("The Report Is Ready. You can click the following link to get the excel report file")
    st.write("\n")
    # st.write("\n")
