#!/usr/bin/env python3
"""
Opern a Workbook object with OpenPyXL
"""
from openpyxl import load_workbook

def main():
    #Open the workbook
    wb = load_workbook('2.1_Hello_world.xlsx', data_only=True)
    #Check what sheets are in it 
    for sheet in wb:
        print(sheet.title)
      
if __name__ == " __main__":
    main()
    