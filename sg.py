import boto3
import os
import logging
from dotenv import load_dotenv
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

load_dotenv()

ec2 = boto3.client(
    "ec2",
    endpoint_url=os.getenv("‍‍‍‍AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)


def getting_SG():
    try:
        all_SG = []

        response = ec2.describe_security_groups(MaxResults=100)
        all_SG.extend(response.get("SecurityGroups", []))

        logging.info("response worked")

        while "NextToken" in response:
            response = ec2.describe_security_groups(
                MaxResults=100, NextToken=response["NextToken"]
            )

            all_SG.extend(response.get("SecurityGroups", []))
            logging.info("fetching number in account works")
            print(f"The amount of Security Groups in account: {len(all_SG)}")

        for sg in all_SG:
            print(sg["GroupId"])
            print(sg["GroupName"])
            print("---")
        return all_SG
    except ClientError as e:
        er_code = e.response["Error"]["Code"]
        er_msg = e.response["Error"]["Message"]
        logging.error(f"Error: {er_code} : {er_msg}")


getting_SG()
