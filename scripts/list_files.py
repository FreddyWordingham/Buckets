from botocore.exceptions import ClientError
import argparse
import boto3


# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("bucket_name", help="Which bucket to list")
args = parser.parse_args()


# Get list of files
s3 = boto3.client("s3")
try:
    response = s3.list_objects_v2(Bucket=args.bucket_name)
except ClientError as err:
    print(f"Error listing files: {err}")
    exit()


# Print list of files
print(f"Contents of {args.bucket_name}:")
for object in response["Contents"]:
    print(f"\t{object['Key']}")
