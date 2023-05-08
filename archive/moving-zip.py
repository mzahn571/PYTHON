import os, shutil


os.getcwd()
os.chdir("C:/Users/mzahn/Documents/")

dst_dir = ("C:/Users/mzahn/Documents/WorkSpace")

filename = "archive.zip"

shutil.move(filename, dst_dir)
