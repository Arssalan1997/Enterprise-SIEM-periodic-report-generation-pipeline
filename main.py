from monthly import HandlerOfMainSheetOfMonthlyReport
from quarterly import HandlerOfMainSheetOfQuarterlyReport
import streamlit as st
import os
from CONSTANTS import FILES_DIRECTORY_OF_MONTHLY, FILES_DIRECTORY_OF_QUARTERLY
import time
from returns.result import safe


@safe
def main_function__to_be_called():

    def receive_needed_data_from_user_to_do_the_report():

        report_type_ = st.session_state.report_type.lower()   # The options are capitalized in streamlit radio widget
        # of 'pages/1-determine kind of report.py' module

        filename_ = str()
        if report_type_ == "monthly":
            filename_ = os.path.join(fr"{FILES_DIRECTORY_OF_MONTHLY}\{st.session_state.CURRENT_TIME}", st.session_state.monthly_report_file.name)
        elif report_type_ == "quarterly":
            filename_ = os.path.join(fr"{FILES_DIRECTORY_OF_QUARTERLY}\{st.session_state.CURRENT_TIME}", st.session_state.quarterly_report_file.name)

        # ---------- { progress bar   ----------
        for percent_complete in range(4, 6):
            st.session_state.progress_text = f"Operation in progress. Please wait, initiating the processes" \
                                             f"...{percent_complete}%"
            st.session_state.progress_bar.progress(percent_complete, text=st.session_state.progress_text)
            time.sleep(0.01)
        # ----------   progress bar } ----------

        return report_type_, filename_

    def call_report_class_handlers(report_type_, filename_):
        # Depending on report_type, the class that is called will vary, so to reduce to use if condition with
        # indentations, a dictionary solution is adopted to do a mapping.
        mapping_dict_of_report_type_to_class = {
                                                'monthly': HandlerOfMainSheetOfMonthlyReport,
                                                'quarterly': HandlerOfMainSheetOfQuarterlyReport
                                               }
        report_class_handler_object = mapping_dict_of_report_type_to_class[report_type_](report_type_, filename_)

        # ---------- { progress bar  ----------
        for percent_complete in range(5, 11):
            st.session_state.progress_text = f"Operation in progress. Please wait, initiating the processes" \
                                             f"...{percent_complete}%"
            st.session_state.progress_bar.progress(percent_complete, text=st.session_state.progress_text)
            time.sleep(0.01)
        # ----------   progress bar } ---------

        # ################################

        # An object from the corresponding class handler is instantiated, it is time to go for sequential stages of
        # operations
        report_class_handler_object.operations_before_iterations_on_worksheets()

        # ---------- { progress bar  ----------
        for percent_complete in range(11, 18):
            st.session_state.progress_text = f"Operation in progress. Please wait, operations before iterations on " \
                                             f"worksheets are executing...{percent_complete}%"
            st.session_state.progress_bar.progress(percent_complete, text=st.session_state.progress_text)
            time.sleep(0.01)
        # ----------   progress bar } ---------

        # ################################

        report_class_handler_object.operations_of_iterations_on_worksheets()

        # ---------- { progress bar  ----------
        for percent_complete in range(17, 40):
            st.session_state.progress_text = f"Operation in progress. Please wait, operations of iterations on " \
                                             f"worksheets are executing...{percent_complete}%"
            st.session_state.progress_bar.progress(percent_complete, text=st.session_state.progress_text)
            time.sleep(0.01)
        # ----------   progress bar } ---------

        # ################################

        report_class_handler_object.operations_after_iterations_on_worksheets()

        # ---------- { progress bar  ----------
        for percent_complete in range(39, 59):
            st.session_state.progress_text = f"Operation in progress. Please wait, operations after iterations on " \
                                             f"worksheets are executing...{percent_complete}%"
            st.session_state.progress_bar.progress(percent_complete, text=st.session_state.progress_text)
            time.sleep(0.01)
        # ----------   progress bar } ---------

        # ################################

        report_class_handler_object.save_file_operation_before_select_data_phase()

        # ---------- { progress bar  ----------
        for percent_complete in range(58, 81):
            st.session_state.progress_text = f"Operation in progress. Please wait, saving export file before " \
                                             f"executing select-data phase...{percent_complete}%"
            st.session_state.progress_bar.progress(percent_complete, text=st.session_state.progress_text)
            time.sleep(0.01)
        # ----------   progress bar } ---------

        # ################################

        report_class_handler_object.operation_of_select_data()

        # ---------- { progress bar  ----------
        for percent_complete in range(80, 93):
            st.session_state.progress_text = f"Operation in progress. Please wait, executing select-data phase..." \
                                             f"{percent_complete}%"
            st.session_state.progress_bar.progress(percent_complete, text=st.session_state.progress_text)
            time.sleep(0.01)
        # ----------   progress bar } ---------

        # ################################

        report_class_handler_object.save_final_file_operation_after_select_data_phase()

        # ---------- { progress bar  ----------
        for percent_complete in range(92, 101):
            st.session_state.progress_text = f"Operation in progress. Please wait, saving final file..." \
                                             f"{percent_complete}%"
            st.session_state.progress_bar.progress(percent_complete, text=st.session_state.progress_text)
            time.sleep(0.01)
        # ----------   progress bar } ---------

    # ----------------------------------------------------------------------------------------------------
    report_type, filename = receive_needed_data_from_user_to_do_the_report()
    call_report_class_handlers(report_type, filename)
