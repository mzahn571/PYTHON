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



chdir =os.chdir("c:/Users/ab21600/Documents/DA")
dirlist = os.listdir("c:/Users/ab21600/Documents/DA")
main_workbook = "c:/Users/ab21600/Documents/DA/main.xlsx"
path2 = "C:/Users/ab21600/Documents/example2.xlsx"




for x in sorted(dirlist):
    print(x)
    #load = xl.load_workbook(x)
