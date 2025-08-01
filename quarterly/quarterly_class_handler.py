"""
Refer to description of 'monthly_class_handler.py' module
"""

from monthly import HandlerOfMainSheetOfMonthlyReport
from quarterly import MainSheetOfQuarterlyReport
from openpyxl import load_workbook


class HandlerOfMainSheetOfQuarterlyReport(HandlerOfMainSheetOfMonthlyReport):

    # @staticmethod
    def operations_before_iterations_on_worksheets(self):
        MainSheetOfQuarterlyReport.receive_report_persian_name_to_include_in_first_sheet_from_user()
        MainSheetOfQuarterlyReport.receive_header_names_of_numerical_columns_from_user()

    def operations_of_iterations_on_worksheets(self):
        """
        Differences towards the base class corresponding method:

        1-calling '.receive_filename_and_save_needed_values_on_first_sheet()' method
        2-calling 'update_first_sheet_info()' method on the first worksheet
        """

        # The following step belongs to the '.operations_before_iterations_on_worksheets()' method. The reason behind
        # the inclusion over here: 1-needing 'self.filename' to send to the following method; 2-simplicity of
        # inheritance

        # 'MainSheetOfMonthlyReportHandler' class does not have the following
        MainSheetOfQuarterlyReport.extract_needed_values_from_first_sheet(self.filename)

        self.workbook = load_workbook(self.filename)
        sheet_names = self.workbook.sheetnames  # saved in a list for probable future use

        counter = 0
        for sheet_name in sheet_names:
            counter += 1
            sheet = self.workbook[sheet_name]
            main_sheet = MainSheetOfQuarterlyReport(sheet)

            # test line
            # print(isinstance(main_sheet, MainSheetOfQuarterlyReport))  # all outputs ==> 'True'

            main_sheet.remove_values_of_cells_with_numerical_data()
            main_sheet.delete_message_column_content()

            if counter == 1:
                # 'MainSheetOfMonthlyReportHandler' class does not have the following
                main_sheet.update_first_sheet_info()

            main_sheet.header_date_fields_update()
            main_sheet.update_all_formulas()

    def operations_after_iterations_on_worksheets(self):
        MainSheetOfQuarterlyReport.display_sheets_with_issues()

    def operation_of_select_data(self):
        pass

    def save_final_file_operation_after_select_data_phase(self):
        pass
