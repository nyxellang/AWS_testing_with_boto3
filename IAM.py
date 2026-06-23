import boto3
import os
from dotenv import load_dotenv
import logging
from botocore.exceptions import ClientError

load_dotenv()
logging.basicConfig(level=logging.INFO)

IAM = boto3.client(
    "iam",
    endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

try:
    response = IAM.list_users()
    logging.info("Listing users successfully")
    for user in response["Users"]:
        print(user["UserName"])
        print(user["UserId"])

        policies = IAM.list_attached_user_policies(UserName=user["UserName"])
        for policy in policies["AttachedPolicies"]:
            print(f"  Policy: {policy['PolicyName']}")

    roles = IAM.list_roles()

    for role in roles["Roles"]:
        print(f"Role: {role['RoleName']}")

        attached = IAM.list_attached_role_policies(RoleName=role["RoleName"])

        for policy in attached["AttachedPolicies"]:
            print(f"  Policy: {policy['PolicyName']}\n")

    logging.info("Fetched attached roles successfully")
except ClientError as e:
    error_code = e.response["Error"]["Code"]
    error_msg = e.response["Error"]["Message"]
    logging.error(f"Error {error_code} : {error_msg}")
