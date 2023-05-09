from botocore.exceptions import ClientError
import argparse
import boto3


# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("bucket_name", help="Which bucket to list")
args = parser.parse_args()


# Delete bucket
s3 = boto3.resource("s3")
try:
    bucket = s3.Bucket(args.bucket_name)
    bucket.delete()
except ClientError as err:
    print(f"Error deleting bucket: {err}")
    exit()


# Success
print(f"Deleted bucket {args.bucket_name}")
