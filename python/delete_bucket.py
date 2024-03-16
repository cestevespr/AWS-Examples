# Specify the region for the bucket
region = "us-east-1"  # Example: 'us-west-2' for Oregon
bucket_name = "my-new-bucket-name"  # Ensure this is unique across all existing bucket names

# Create the S3 bucket
s3.delete_bucket(Bucket=bucket_name,
                 CreateBucketConfiguration={'LocationConstraint': region})