import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()

ec2 = boto3.client(
    "ec2",
    endpoint_url=os.getenv("‍‍‍‍AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)


try:
    response = ec2.describe_instances(
        Filters=[{"Name": "tag:Name", "Values": ["my-server"]}]
    )

    for reservations in response["Reservations"]:
        for instance in reservations["Instances"]:
            print(instance["InstanceId"])
            print(instance["InstanceType"])
            print(instance["State"]["Name"])
            instance_id = instance["InstanceId"]

            ec2.start_instances(InstanceIds=[instance_id])
            logging.info("started successfully")
            ec2.stop_instances(InstanceIds=[instance_id])
            logging.info("Stopped successfully")
            ec2.reboot_instances(InstanceIds=[instance_id])
            logging.info("Rebooted successfully")
except ClientError as e:
    error_code = e.response["Error"]["Code"]
    error_msg = e.response["Error"]["Message"]
    logging.error(f"Error {error_code} : {error_msg}")
