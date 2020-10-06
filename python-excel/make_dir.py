

	
	
#The Current Working Directory

import os 
import sys
import openpyxl
import xlutils


>>> import os
>>> os.path.join('velomp1g', 'home', 'Moloch Project #1', 'data')


os.getcwd()
os.chdir('H:\\velomp1g\home\Moloch Project #1\data\')



Creating New Folders with os.makedirs()

Your programs can create new folders (directories) with the os.makedirs() function. Enter the following into the interactive shell:

>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')

