import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ec2 = boto3.client(
    "ec2",
    endpoint_url=os.getenv("‍‍‍‍AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

response = ec2.describe_instances()
for reservations in response["Reservations"]:
    for instance in reservations["Instances"]:
        print(instance["InstanceId"])
        print(instance["InstanceType"])
        print(instance["State"]["Name"])
