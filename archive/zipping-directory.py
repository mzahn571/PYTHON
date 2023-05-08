import os 
import shutil

output_filename = "archive"
dir_name = "C:/Users/mzahn/Documents/Scripts/"

os.getcwd()
os.chdir("C:/Users/mzahn/Documents/")
shutil.make_archive(output_filename, 'zip', dir_name)
