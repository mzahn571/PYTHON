from secret import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

import boto3
import os
import time
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


os.chdir(homedir)
shutil.make_archive(output_filename, 'zip', homedir)

client = boto3.client('s3',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
                        

for file in os.listdir():
    if '.zip' in file:
        upload_file_bucket = bucket_name
        upload_file_key = str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)

# Cleanup
os.remove(zipfile)
