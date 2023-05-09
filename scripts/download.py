from botocore.exceptions import ClientError
import argparse
import boto3
import botocore


# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("bucket_name", help="Which bucket to list")
parser.add_argument("file_name", help="Which file to download from S3")
args = parser.parse_args()


# Download file
s3 = boto3.resource("s3")
try:
    s3.Bucket(args.bucket_name).download_file(args.file_name, args.file_name)
except botocore.exceptions.ClientError as err:
    print(f"Error downloading file: {err}")


# Success
print(f"Downloaded file {args.file_name} from bucket {args.bucket_name}")
