import os 
import shutil
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
dir_name = "C:/Users/mzahn/Documents/"
dst_dir = ("C:/Users/mzahn/Documents/WorkSpace")
filename = "workspace-"
output_filename = filename + date
output = output_filename
extension = ".zip"
zipfile = output + extension

os.getcwd()
os.chdir("C:/Users/mzahn/")
shutil.make_archive(output, 'zip', dir_name)
shutil.move(zipfile, dst_dir)
