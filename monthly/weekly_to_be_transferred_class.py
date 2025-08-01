from monthly import MainSheetOfMonthlyReport


class MainSheetOfWeeklyReportToTransferDataToMonthlyReport(MainSheetOfMonthlyReport):
    """
    we will later have abstract class to be implemented and this class will inherit from that
    (instead of 'MainSheetOfMonthlyReport')
    """

    NUMBER_OF_LAST_REPORT_NUMERICAL_COLUMNS = 2

    def __init__(self, sheet):
        """
        instance attributes over this class(not the super one):
        """

        super().__init__(sheet)

        # # test line
        # print(f"'self.list_of_numerical_cells_coordinates' = {self.list_of_numerical_cells_coordinates}")
        # ----------------------------------------------------

        # ### {{ inherited after going for implementing the step of transferring data from forth weekly excel file ####
        #                   ########################################################################

        # self.list_of_messages = list()   # within a certain sheet of the weekly report: message items will all be
        # # stored in a list that will later will be copied to the main report file

        # ###  inherited after going for implementing the step of transferring data from forth weekly excel file }} ####
        #                   ########################################################################

        self.make_list_of_messages()     # within the class of upper level(the one that calls this class:
        # 'TransferDataFromWeeklyToMonthly') ; we prefer to not call it for the sake of simplicity, so we call it in
        # initiator of this class to make its result ready to use in 'TransferDataFromWeeklyToMonthly' class, as the
        # name suggests it makes 'self.list_of_messages', so right after an object is instantiated from this class,
        # 'self.list_of_messages' is in handy

        self.list_of_last_week_values = list()  # within a certain sheet of the weekly report: last_week_values will all
        # be stored in a list that will later be copied to the main report file
        self.make_list_of_last_week_values()    # identical to 'self.make_list_of_messages()' code line

        self.list_of_this_week_values = list()  # within a certain sheet of the weekly report: this_week_values will all
        # be stored in a list that will later be copied to the main report file
        self.make_list_of_this_week_values()    # identical to 'self.make_list_of_messages()' code line

    # def make_list_of_messages(self):
    #     """
    #     inherited after going for implementing the step of transferring data from forth weekly excel file
    #     """
    #     if self.sheet_has_issue is True:
    #         return None
    #
    #     for row in self.sheet.iter_rows(min_row=self.sheet[self.coordinate_of_up_left_number_boundary].row,
    #                                     max_row=self.sheet[self.coordinate_of_down_left_number_boundary].row,
    #                                     min_col=self.sheet[self.coordinate_of_up_left_number_boundary].column - 1,
    #                                     max_col=self.sheet[self.coordinate_of_down_left_number_boundary].column - 1
    #                                     ):
    #         self.list_of_messages.append(row[0].value)   # every row has only one cell

    def make_list_of_last_week_values(self):
        if self.sheet_has_issue is True:
            return None

        # row == row_of_coordinates
        self.list_of_last_week_values = [self.sheet[row[1]].value for row in self.list_of_numerical_cells_coordinates]

    def make_list_of_this_week_values(self):
        if self.sheet_has_issue is True:
            return None

        # row == row_of_coordinates
        self.list_of_this_week_values = [self.sheet[row[0]].value for row in self.list_of_numerical_cells_coordinates]
