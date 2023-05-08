import boto3
from botocore.exceptions import ClientError
 
#
# option 2: S3 resource object will return list of all bucket resources.
# This is useful if we want to further process each bucket resource.
#

from secret import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY




client = boto3.client('s3',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)


s3 = boto3.resource('s3')
buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket)
