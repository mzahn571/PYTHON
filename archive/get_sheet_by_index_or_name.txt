#!/usr/bin/env python3
"""
Get shees by index or name
"""
from openpyxl import load_workbook

def main():
    # Open the Hello_copies.xlsx
    wb = load_workbook("2.4_Hello_copies.xlsx")
    # Check what indices the sheets have
    for sheet in wb:
        print("{} has the index {}".format(sheet.title, eb.index(sheet)))
    print("-"*20)
    # Get by index method 1 
    ws1 = wb.worksheets[0]
    ws2 = wb.worksheets[1]
    # Get by index method 2 
    worksheets = wb.sheetnames
    ws3 = wb[worksheets[2]]
    print("The first sheet has the title", ws1.title, "\nThe second sheet has the title:", ws2.title \
            , "\nThe third sheet has the title:", ws.title)
    # Get a sheet by name
    ws2 = wb["Hello World!"]
    
if __name__ == "__main__":
    main()