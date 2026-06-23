 # Simple BOTO3 scripts

Hello, first of all thank you for being here.
This is repo is just going to be uploading my AWS scripts (BOTO3 on python) to github.


## Scripts
- `boto3test.py` — lists, start, stop, and reboot EC2 instances that are filtered
- `S3.py` — creates a S3 bucket, uploads a simple file (file.txt), and sets for it set public policy
- `IAM.py` — list IAM users and attached policies
- `IAM.py` — list IAM users, attached policies, and roles
- `sg.py` — describe security groups in default VPC
- `cloudinfo.py` — cloud info CLI using click and rich

## Setup
```bash
pip install boto3 python-dotenv click rich
```

or you can use ```uv```

You have ot create a `.env` file:
```
AWS_ACCESS_KEY_ID=test          # enter your key ID 
AWS_SECRET_ACCESS_KEY=test      # you key
AWS_DEFAULT_REGION=us-east-1    # choose what ever
AWS_ENDPOINT_URL=http://localhost:4566
```

## Usage
```bash
python cloudinfo.py                # shows all
python cloudinfo.py --service s3   # S3 only
python cloudinfo.py --service ec2  # EC2 only
```

yep thats it thank you for reading :P

