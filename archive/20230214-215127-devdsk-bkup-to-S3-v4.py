from secret import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

import boto3
import os
import time
import logging
import shutil
from datetime import datetime

bucket_name = "mzahn-devdsk-backup"
filename = "devdsk-bkup-"
date = datetime.now().strftime("%Y-%m-%d")
username = os.environ.get('USER')
local_path = "/local/home/"
homedir = local_path + username
output_filename = filename + date
output = output_filename
extension = ".zip"
zipfile = output + extension


log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
             "%(filename)s::%(lineno)d::%(message)s"

logging.basicConfig(
    filename = homedir + date + "-bkup.log", format=log_format)

try:
    os.chdir(homedir)
    shutil.make_archive(output_filename, 'zip', homedir)
except Exception as Argument:
    logging.exception("Error occurred with out_filename, zip or homedir")

try:
    client = boto3.client('s3',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
except Exception as Argument:
    logging.exception("Error occurred with AWS keys")
                        
try:
    for file in os.listdir():
        if '.zip' in file:
            upload_file_bucket = bucket_name
            upload_file_key = str(file)
            client.upload_file(file, upload_file_bucket, upload_file_key)
except Exception as Argument:
    logging.exception("Error occurred uploading file to S3")

try:
    for file in os.listdir():
        if file.endswith('-bkup.log'):
            upload_file_bucket = bucket_name
            upload_file_key = str(file)
            client.upload_file(file, upload_file_bucket, upload_file_key)
except Exception as Argument:
    logging.exception("Error occurred uploading bkup.log")

finally:
# Cleanup
    os.remove(zipfile)
    for file in os.listdir():
        if file.endswith('-bkup.log'):
            os.remove(file)
