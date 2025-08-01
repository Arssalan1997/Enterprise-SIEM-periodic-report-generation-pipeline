from monthly import MainSheetOfWeeklyReportToTransferDataToMonthlyReport


class AggregationListSheet(MainSheetOfWeeklyReportToTransferDataToMonthlyReport):

    NUMBER_OF_LAST_REPORT_NUMERICAL_COLUMNS = 1   # overrides the 'NUMBER_OF_LAST_REPORT_NUMERICAL_COLUMNS = 4' line of
    # code in 'MainSheetOfMonthlyReport' class(the grandfather class)

    def __init__(self, sheet):

        super().__init__(sheet)

        # Overrides the following instance attributes in its super class(parent class), and:
        # The following have no functionality in this class, thus they are set to None for the sake of code readability
        self.list_of_last_week_values = None
        self.list_of_this_week_values = None

        self.make_list_of_messages()    # to make available '.list_of_messages' that will be used within:
        # 'transfer_data_from_aggregation_list_to_monthly_report_class.py'

        # ----------------------------------------------------
        self.list_of_aggregation_values = list()  # defined in this class only(not within parent and grandfather
        # classes).

        self.make_list_of_aggregation_values()    # to make available '.list_of_aggregation_values' that will be used
        # within: 'transfer_data_from_aggregation_list_to_monthly_report_class.py'

    def make_list_of_messages(self):
        if self.sheet_has_issue is True:
            return None

        for row in self.sheet.iter_rows(min_row=self.sheet[self.coordinate_of_up_left_number_boundary].row,
                                        max_row=self.sheet[self.coordinate_of_down_left_number_boundary].row,
                                        min_col=self.sheet[self.coordinate_of_up_left_number_boundary].column - 2,
                                        max_col=self.sheet[self.coordinate_of_down_left_number_boundary].column - 2
                                        ):
            self.list_of_messages.append(row[0].value)   # every row has only one cell

    def make_list_of_last_week_values(self):
        """
        Has no functionality in this class, so overrides the corresponding method in parent class

        Quick Note: There is a bunch of other instance methods in grandfather class that can be candidates of
        overriding, but ignored for the sake of simplicity
        """

        pass

    def make_list_of_this_week_values(self):
        """
        Has no functionality in this class, so overrides the corresponding method in parent class

        Quick Note: There is a bunch of other instance methods in grandfather class that can be candidates of
        overriding, but ignored for the sake of simplicity
        """

        pass

    def make_list_of_aggregation_values(self):
        if self.sheet_has_issue is True:
            return None

        self.list_of_aggregation_values = [self.sheet[row[0]].value for row in self.list_of_numerical_cells_coordinates]
