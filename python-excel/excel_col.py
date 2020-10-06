import openpyxl
import shutil
import copy
import pandas as pd
import os
import sys
import pathlib
from openpyxl import Workbook
import xlsxwriter
import xlrd




xl = pd.ExcelFile("C:/Users/ab21600/Documents/Python-Remedy-Report/test1.xlsx")
df = xl.parse("test")
df = df.sort(columns="Short Problem Description")

writer = pd.ExcelWriter('C:/Users/ab21600/Documents/Python-Remedy-Report/output.xlsx')
df.to_excel(writer,sheet_name='Sheet1',columns=["Short Problem Description"],index=False)
writer.save()
