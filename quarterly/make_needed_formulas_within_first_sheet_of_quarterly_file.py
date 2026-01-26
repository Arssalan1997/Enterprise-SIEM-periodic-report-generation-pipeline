from CONSTANTS import SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES


def make_needed_formulas(workbook):
    sheet_to_change = workbook["All detected attacks"]

    # --------------------------------

    coordinate1 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRules"][0]
    sheet_to_change["B2"].value = f"=ArcSightRules!{coordinate1}"

    coordinate2 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRules"][1]
    sheet_to_change["C2"].value = f"=ArcSightRules!{coordinate2}"

    coordinate3 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRules"][2]
    sheet_to_change["D2"].value = f"=ArcSightRules!{coordinate3}"

    # ------------------------

    coordinate1 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRulesBMI"][0]
    sheet_to_change["B3"].value = f"=ArcSightRulesBMI!{coordinate1}"

    coordinate2 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRulesBMI"][1]
    sheet_to_change["C3"].value = f"=ArcSightRulesBMI!{coordinate2}"

    coordinate3 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRulesBMI"][2]
    sheet_to_change["D3"].value = f"=ArcSightRulesBMI!{coordinate3}"

    # ------------------------

    coordinate1 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRulesMY"][0]
    sheet_to_change["B4"].value = f"=ArcSightRulesMY!{coordinate1}"

    coordinate2 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRulesMY"][1]
    sheet_to_change["C4"].value = f"=ArcSightRulesMY!{coordinate2}"

    coordinate3 = SHEET_NAMES__AND__CORRESPONDING_MONTHLY_SUM_COORDINATES["ArcSightRulesMY"][2]
    sheet_to_change["D4"].value = f"=ArcSightRulesMY!{coordinate3}"
