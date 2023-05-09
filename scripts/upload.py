from botocore.exceptions import ClientError
import argparse
import boto3


# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("bucket_name", help="Which bucket to list")
parser.add_argument("file_name", help="Which file to upload to S3")
args = parser.parse_args()


# Upload file
s3 = boto3.client("s3")
try:
    s3.upload_file(args.file_name, args.bucket_name, args.file_name)
except ClientError as err:
    print(f"Error uploading file: {err}")
    exit()


# Success
print(f"Uploaded file {args.file_name} to bucket {args.bucket_name}")
