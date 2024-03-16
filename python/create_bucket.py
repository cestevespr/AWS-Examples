# Specify the region for the bucket

bucket_name = "my-new-bucket-name"  # Ensure this is unique across all existing bucket names

# Create the S3 bucket
s3.create_bucket(Bucket=bucket_name)