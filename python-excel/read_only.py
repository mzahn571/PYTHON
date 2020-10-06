
import openpyxl
from string import ascii_uppercase

newfile = 'C:/Users/ab21600/Documents/DA/CFPB.xlsx'

wb = openpyxl.load_workbook(filename = newfile)
worksheet = wb.active

for column in ascii_uppercase:
    if (column=='A'):
        worksheet.column_dimensions[column].width = 30
    elif(column=='B'):
        worksheet.column_dimensions[column].width = 30
    elif(column=='C'):
        worksheet.column_dimensions[column].width = 30
    elif(column=='D'):
        worksheet.column_dimensions[column].width = 30
    elif(column=='E'):
        worksheet.column_dimensions[column].width = 30
    elif(column=='F'):
        worksheet.column_dimensions[column].width = 30
    elif(column=='D'):
        worksheet.column_dimensions[column].width = 30
wb.save(newfile)
