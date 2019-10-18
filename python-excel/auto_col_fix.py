import openpyxl
import shutil
import copy
import pandas as pd
import os
import sys
import pathlib
from openpyxl import Workbook
import xlsxwriter
import openpyxl as xl
path = 'C:/Users/ab21600/Documents/Python-Remedy-Report/test1.xlsx'

wb = xl.load_workbook(filename=path)
ws = wb.worksheets
wb.active = 0
for column_cells in ws.columns:
    length = max(len(as_text(cell.value)) for cell in column_cells)
    ws.column_dimensions[column_cells[0].column].width = length


wb.save(path)
