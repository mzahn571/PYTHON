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
import numpy



xl = pd.ExcelFile("C:/Users/ab21600/Documents/Python-Remedy-Report/test1.xlsx")
df = xl.parse("test")
#df = df.sort_values(columns="Short Problem Description")
#df = df.sort_values(by=["Short Problem Description", "NTM Ticket ID", "Create Date", "Last-Modified-Date", "Service ID", "Priority", "Last External Comment Time"])
df = df.sort_values(by=["Short Problem Description"])
                        
writer = pd.ExcelWriter('C:/Users/ab21600/Documents/Python-Remedy-Report/output.xlsx')
df.to_excel(writer,sheet_name='Sheet1',columns=["NTM Ticket ID", "Create Date", "Last-Modified-Date", "Service ID", "Short Problem Description", "Priority", "Last External Comment Time"],index=False)
writer.save()

