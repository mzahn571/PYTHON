#!/usr/bin/python3
# Date: 4/27/2022
# Name: devdsk-bkup-to-S3.py
# Backup dev-desktop to S3 Bucket

from secret import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME
from datetime import datetime
import boto3
import tarfile
import os
import sys
import posixpath
from boto3.s3.transfer import S3Transfer

date = datetime.now().strftime("%Y-%m-%d-")

# Directory on dev-dsk must specify the direct path not the link.
directory = "/local/home/mzahn"
dirname = os.path.split(directory)[-1]
filename = date + dirname

if posixpath.isdir(directory):
    tarname = '/tmp/{}.tar.gz'.format(filename)
    tar = tarfile.open(tarname,'w:gz')
    tar.add(directory)
    tar.close()

# S3 Uploading started
    client = boto3.client('s3',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    transfer = S3Transfer(client)
    transfer.upload_file(tarname, BUCKET_NAME, 'backup/{}.tar.gz'.format(filename))

# Remove temporary backup from local
    #os.remove(tarname)
