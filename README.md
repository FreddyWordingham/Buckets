# Buckets

<p align="center">
    <img src="./resources/images/logo.png" />
</p>

Scripts for using AWS S3 buckets.

## Quick Start

Download the repository and change the current working directory to the project root:

```shell
git clone https://github.com/FreddyWordingham/Buckets.git
cd Buckets
```

Install the project using Poetry:

```shell
poetry install
```

You must be logged into the AWS CLI tool.
Use the following command to configure your access keys:

```shell
aws configure
```

## Usage

### Create bucket

Create a new bucket.
Note that bucket names must be unique across all of AWS and must [adhere to the naming convention](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).

```shell
poetry run python scripts/create_bucket.py <bucket>
```

### List buckets

List all buckets in the current AWS account.

```shell
poetry run python scripts/list_buckets.py
```

### Delete bucket

Delete a bucket and all of its contents.

```shell
poetry run python scripts/delete_bucket.py <bucket>
```

### Upload file

Upload a file to a bucket.

```shell
poetry run python scripts/upload.py <bucket> <file>
```

### Download file

Download a file from a bucket.

```shell
poetry run python scripts/download.py <bucket> <file>
```

### Delete file

Delete a file from a bucket.

```shell
poetry run python scripts/delete_file.py <bucket> <file>
```
