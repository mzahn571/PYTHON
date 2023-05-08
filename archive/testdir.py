import os

# define the namem of the directory tobe created
path = "C:/Users/mzahn/Documents/testdir"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
