#!/usr/bin/env python3
"""
Open an existing workbook, copy one sheet
Copy data from one sheet to another
"""
from openpyxl import load_workbook

def main():
    #Create the Workbook object
    wb = load_workbook("2.3_Hello_sheet.xlsx")
    
    #Copy sheets
    source = wb["Sheet nr 2"]
    new_sheet = wb.copy_worksheet(source)
    new_sheet.title = "Copy of Sheet nr 2"
    
    # Check what sheets exists in the workbook
    print("Sheets in workbook:")
    for sheet in wb:
        print(sheet.title)
        
    wb.save("2.4_Hello_copies.xlsx")
    
if __name__ == "__main__":
    main()
