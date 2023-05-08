from secret import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import boto3


session = boto3.Session(
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
                        


#Then use the session to get the resource
s3 = session.resource('s3')

my_bucket = s3.Bucket('workspace-1234')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)