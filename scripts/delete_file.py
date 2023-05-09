from botocore.exceptions import ClientError
import argparse
import boto3


# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("bucket_name", help="Target bucket")
parser.add_argument("file_name", help="Target file")
args = parser.parse_args()


# Delete file
s3 = boto3.client("s3")
try:
    s3.delete_object(Bucket=args.bucket_name, Key=args.file_name)
except ClientError as err:
    print(f"Error deleting file: {err}")
    exit()


# Success
print(f"Deleted file {args.file_name} to bucket {args.bucket_name}")
