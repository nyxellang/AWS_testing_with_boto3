import boto3
import os
from dotenv import load_dotenv
import json
import logging
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

policy = json.dumps(
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principle": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::test-bucket/*",
            }
        ],
    }
)

try:
    s3.create_bucket(Bucket="test-bucket")
    logging.info("Bucket created successfully")
    s3.put_bucket_policy(Bucket="test-bucket", Policy=policy)
    s3.upload_file("file.txt", "test-bucket", "file.txt")
    logging.info("File uploaded successfully")
    endpoint = os.getenv("AWS_ENDPOINT_URL")
    bucket = "test-bucket"
    filename = "file.txt"
    url = f"{endpoint}/{bucket}/{filename}"
    print(f"File URL: {url}")
except ClientError as e:
    error_code = e.response["Error"]["Code"]
    error_message = e.response["Error"]["Message"]
    logging.error(f"Error {error_code}: {error_message}")
