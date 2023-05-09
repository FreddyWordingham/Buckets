import boto3


# Get list of buckets
s3 = boto3.client("s3")
response = s3.list_buckets()


# List buckets
print("Existing buckets:")
for bucket in response["Buckets"]:
    print(f"\t{bucket['Name']}")
