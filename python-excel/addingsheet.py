import openpyxl
import shutil
import copy
import pandas as pd
import os
import sys
import pathlib

import openpyxl as xl

MyList = ['OSHRC','SSS','NARA','NCPC','DOC-BEA','GSA','DOC-NTIS','VA','DOC-USPTO','SSA','NEA','DOC-BIS','RRB','IAF','DOC-HCHB','CFPB','FRTIB','DOC-NIST','EDU','OPM','DOE-JLAB',
          'NASA','TREAS','DOS','DOE-KCP','DOE-BNL','HHS-CSIRC','DOE-BPA','DOJ-FBI','HHS-HRSA','HHS-CMS','HHS-NIH','TREAS-IRS','HHS-IHS','NSF','HHS-FDA','HHS-CDC','HHS-NLM',
		  'DOC-ITA','FERC','DOT-FAA','DOC-NOAA','USITC','DOE-SRS','DOE-NNSS','DOE-PPPL','DOE-LLNL','OSC','FDIC','NASA-JPL','DOE-OSTI','DOE-NREL','FEC','DOE-SWPA','FED','PT',
		  'DOE-ORNL','ONHIR','TREAS-OCC','DOC-CENSUS','DOE-INL','DOE-LANL','DOE-PNNL','NCUA','DOE-SPR','SEC','STB','DOE-NPO','TVA','DOC-OIG','DOE-NRO','DOE-ANL','DOE-EMCBC',
		  'DOE-ETTP','DOE-WIPP','USCCR','USPS OIG','NRC','FLRA']





i = 0

path = 'C:/Users/ab21600/Documents/example2.xlsx'
print(len(MyList))

wb = xl.load_workbook(filename=path)
wb.active = 3

#for ws in wb.worksheets:

for i in sorted(MyList):
    ws = wb.create_sheet(title=i)

wb.active = 0

wb.get_sheet_names()
std=wb.get_sheet_by_name('Sheet3')
wb.remove_sheet(std)
std=wb.get_sheet_by_name('Sheet2')
wb.remove_sheet(std)
std=wb.get_sheet_by_name('Sheet1')
wb.remove_sheet(std)    
wb.save(path)



for ws in wb:
    print(ws.title)
    
len(wb.worksheets)



    
    
    
          

          

