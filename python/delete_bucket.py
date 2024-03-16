import boto3

# Initialize a boto3 S3 resource
s3 = boto3.resource('s3')

# Specify your unique bucket name
bucket_name = "my-unique-new-bucket-name-1234"


bucket = s3.Bucket(bucket_name)

# Create the S3 bucket
bucket.delete()

print(f"Bucket '{bucket_name}' deleted successfully.")