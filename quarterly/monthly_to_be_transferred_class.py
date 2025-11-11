from monthly import MainSheetOfMonthlyReport


class MainSheetOfMonthlyReportToTransferDataToQuarterlyReport(MainSheetOfMonthlyReport):

    def __init__(self, sheet, number_of_numerical_columns):
        MainSheetOfMonthlyReportToTransferDataToQuarterlyReport.NUMBER_OF_LAST_REPORT_NUMERICAL_COLUMNS = number_of_numerical_columns
        super().__init__(sheet)
