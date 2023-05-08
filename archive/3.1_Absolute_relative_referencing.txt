#!/usr/bin/env python3
"""
Explore relative and absolute referecing of cells
"""
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils.cell import get_column_letter, column_index_from_string

def save_wb(wb, filename):
    # Save a workbook
    wb.save(filename)
    
def create_sheets(wb, sheet_name_list):
    # Adds the sheets in the sheet_name_list to the workbook
    for sheet_name in sheet_name_list:
        wb.create_sheet(sheet)
        
if __name__ == "main__":
    # Create a workbook
    filename = "Absolute_relative.xlsx"
    wb = Workbook()
    create_sheets(wb, ["Sheet2, "Sheet3", "Sheet4"])
    
    # Input some values in the first sheet with Relative references
    ws1 = wb.workhsheet[0]
    ws1["A1"] = 550
    ws1["C3"] = "Caravan"
    
    print("get_column_letter for index 3 is:", get_column_letter(3))
    print("column_index_frim_string for letter C is:", column_index_from_string("C"))
    
    # Input values in Sheet2 using Absolute references
    ws2 = wb["Sheet2"]
    ws2.cell(row=4, column=2, value=10)     # Cell B4
    ws2.cell(, 2).value = "Train"           # Cell B1
    
    # Save the wb 
    save_wb(wb, filename)
    
    