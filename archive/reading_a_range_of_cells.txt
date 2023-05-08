#!/usr/bin/env python
"""
from openpyxl impirt load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
"""

def save_wb(wb, filename):
    # save a workbook
    wb.save(filename)
    
def create_sheet(wb, sheet_name_list):
    # Adds the sheets in the sheet_name_list to the workbook
    for sheet_name in sheet_name_list:
        wb.create_sheet(sheet_name)
        
if __name__ == "__main__":
    #create a workbook an sheets
    filename = "Absolute_relative.xlsx"
    wb = Workbook()
    create_sheet(wb, ["Sheet2", "Sheet3", "Sheet4"])
    ws1 = wb["Sheet"]
    
    # Set values in the cells
    ws1["A1"] = "A1"
    ws1["A2"] = "A2"
    ws1["B1"] = "B1"
    ws1["B2"] = "B2"
    ws1["C1"] = "C1"
    ws1["C2"] = "C2"
    
    # Create a range with Relative referencing
    cell_range = ws1['A1':'C2']
    # Create a range with Absolute referencing
    cell_reange2 = ws1[get_column_letter(1)+"1":get_column_letter(3)+"2"]
    
    print("A", "B")
    for c1, c2, c3 in cell_range:
        print(c1,value, c2.value, c3.value)
    print()
    for c1, c2, c3 in cell_range2:
        print(c1.value, c2.value, c3.value)
    print(type(cell_range))
    
    ## A cell range is stored as a tuple of rows (A1, B1, C1), (A2, B2,C2)
    ## A1 B1 C1
    ## A2 B2 C2
    #print(cell_range)
    
    # Save the wb
    save_wb(wb, filename)
    
    