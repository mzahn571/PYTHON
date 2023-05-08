

import boto3
import os

os.chdir("C:/Users/mzahn/Documents/Scripts/Python/")

from secret import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY



client = boto3.client('s3',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)



#s3 = boto3.resource('s3')
#my_bucket = s3.Bucket('workspace-1234')

for s3_file in os.listdir():
    print(s3_file)
