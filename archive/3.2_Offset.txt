#!/usr/bin/env python3
"""
Cell offset
"""
from openpyxl import load_workbook
from openpyxl import Workbook

def save_wb(wb, filename):
    # SAve a workbook
    wb.save(filename)
    
def create_sheets(wb, sheet_name_list):
    # Adds the sheets in the sheet_name_list to the workbook
    for sheet_name in sheet_name_list:
    wb.create_sheet(sheet_name)
    
if __name__ == " __main__":
    # Create a workbook an sheets
    filename = "Absolute_relative.xlsx"
    wb = Workbook()
    create_sheets(wb, ["Sheet2", "Sheet3", "Sheet4"])
    ws1 = wb["Sheet"]
    
    # Set value of cell B1 to Train
    ws1.cell(1, 2).value = "Train"
    # Set value of cell C1 to Train cart
    ws1.cell(1, 2).offset(0,1.value = "Train cart"
    
    # Create cell objects for easier referances
    mother_cell = ws1.cell(3,3) # Cell C3
    child_cell = mother_cell.offset(1,0) #Cell C4
    mother_cell.value = "Mother"
    child_cell.value = "Child"
    
    # Save the wb
    save_wb(wb, filename)
    
    