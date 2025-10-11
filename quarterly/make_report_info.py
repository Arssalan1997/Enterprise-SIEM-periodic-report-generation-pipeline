import streamlit as st
import pandas as pd


def make_list_of_sheet_names_with_issues_in_report_file(list_of_sheet_names_with_issues):

    # to easily access at display time
    st.session_state.df__sheet_names_with_issues_in_report_file = pd.DataFrame({
        'SheetNames With Issues': list_of_sheet_names_with_issues
    })

    # makes row indexing start from '0'(instead of '1')
    st.session_state.df__sheet_names_with_issues_in_report_file.index += 1


def make_sheet_names_with_issues_in_weekly_report_files(filename_as_key__and__sheet_names_with_issue_as_value):

    # it is a variable of 'st.session_state' so that I can easily access to it to display in '8-display report info.py'
    # files of 'pages' directory, I have get inspired from streamlit tutorial to make pandas DataFrames to have tables
    # that will be displayed with little effort using streamlit module
    st.session_state.df__sheet_names_with_issues_in_monthly_report_files = pd.DataFrame({
        'Monthly Report Filename': filename_as_key__and__sheet_names_with_issue_as_value.keys(),
        'SheetNames With Issues': filename_as_key__and__sheet_names_with_issue_as_value.values()
    })

    # makes row indexing start from '0'(instead of '1')
    st.session_state.df__sheet_names_with_issues_in_monthly_report_files.index += 1


def make_sheet_names_not_found_in_mapping_file(filename_as_key_and_sheet_names_in_file_but_not_in_mapping_file_as_value):
    """
    A more clear function name but not used for the sake of shortness:
    'display_sheet_names_that_include_in_at_least_one_of_monthly_report_files__but__exclude_in_corresponding_mapping_file'
    """

    # same as the comment of first code line in 'make_sheet_names_with_issues_in_weekly_report_files()' function of
    # this module
    st.session_state.df__sheet_names_not_found_in_mapping_file = pd.DataFrame({
        'Monthly Report Filename': filename_as_key_and_sheet_names_in_file_but_not_in_mapping_file_as_value.keys(),
        'SheetName': filename_as_key_and_sheet_names_in_file_but_not_in_mapping_file_as_value.values()
    })

    # makes row indexing start from '0'(instead of '1')
    st.session_state.df__sheet_names_not_found_in_mapping_file.index += 1
