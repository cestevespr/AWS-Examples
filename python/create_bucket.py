response = client.create_bucket(
    Bucket='string',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1',
        'Location': {
            'Type': 'AvailabilityZone',
            'Name': 'string'
        },
        'Bucket': {
            'DataRedundancy': 'SingleAvailabilityZone',
            'Type': 'Directory'
        }
    },
    GrantFullControl='string',
    GrantRead='string',
    GrantReadACP='string',
    GrantWrite='string',
    GrantWriteACP='string',
    ObjectLockEnabledForBucket=True|False,
    ObjectOwnership='BucketOwnerPreferred'|'ObjectWriter'|'BucketOwnerEnforced'
)