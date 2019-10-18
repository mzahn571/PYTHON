import openpyxl
from string import ascii_uppercase

newfile = 'C:/Users/ab21600/Documents/DA/CFPB.xlsx'

wb = openpyxl.load_workbook(filename = newfile)
worksheet = wb.active

for col in worksheet.columns:
     max_length = 0
     column = col[0].column # Get the column name
     for cell in col:
         try: # Necessary to avoid error on empty cells
             if len(str(cell.value)) > max_length:
                 max_length = len(cell.value)
         except:
             pass
     adjusted_width = (max_length + 2) * 1.2
     worksheet.column_dimensions[column].width = adjusted_width
wb.save(newfile)
