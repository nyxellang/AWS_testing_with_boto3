import logging
import os

import boto3
import click
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

console = Console()

table = Table()
table2 = Table()

table.add_column("S3 Buckets")
table2.add_column("EC2 Instances")
table2.add_column("state")


load_dotenv()

logging.basicConfig(level=logging.INFO)

ec2 = boto3.client(
    "ec2",
    endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)


def fetchingS3():
    try:
        response = s3.list_buckets()
        for b in response["Buckets"]:
            table.add_row(b["Name"])
        logging.info("Fetching S3 Buckets successfully")

        console.print(table)

    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        error_msg = e.response["Error"]["Message"]
        logging.error(f"Error: {error_code}: {error_msg}")


def fetchingEC2():
    try:
        response2 = ec2.describe_instances()
        for reservations in response2["Reservations"]:
            for instance in reservations["Instances"]:
                table2.add_row(instance["InstanceId"], instance["State"]["Name"])

        logging.info("Fetching EC2 instances, state and name successfully")
        console.print(table2)

    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        error_msg = e.response["Error"]["Message"]
        logging.error(f"Error: {error_code}: {error_msg}")


@click.command()
@click.option("--service", type=click.Choice(["s3", "ec2"]), default=None)
def cli(service):
    if service == "s3":
        fetchingS3()
    elif service == "ec2":
        fetchingEC2()
    else:
        fetchingS3()
        fetchingEC2()


if __name__ == "__main__":
    cli()
