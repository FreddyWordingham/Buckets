from botocore.exceptions import ClientError
import argparse
import boto3
import configparser
import os
import re


# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("bucket_name", help="ID of the bucket to create")
args = parser.parse_args()


# Validate bucket name
if not re.match(r"(?!(^xn--|.+-s3alias$))^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$", args.bucket_name):
    raise ValueError("Illegal bucket name")


# Configuration
path = os.path.expanduser("~/.aws/config")
config = configparser.ConfigParser()
config.read(path)
region = config["default"]["region"]


# Create the S3 bucket with specific ACL
s3 = boto3.resource("s3")
try:
    s3.create_bucket(
        Bucket=args.bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": region
        }
    )
except ClientError as err:
    print(f"Error creating bucket: {err}")
    exit()


# Success
print(f"Created bucket {args.bucket_name} in region {region}")
