import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from loguru import logger

from app.config import config


def upload_to_aws_s3(local_file, bucket, s3_file) -> str:
    s3 = boto3.client(
        "s3",
        # region_name="ap-northeast-1",
        aws_access_key_id=config.aws.get("aws_access_key_id", ""),
        aws_secret_access_key=config.aws.get("aws_secret_access_key", ""),
    )

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        # log the file path
        logger.info(f"Uploaded file to S3: {s3_file}")
        return f"https://{bucket}.s3.amazonaws.com/{s3_file}"
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None
    except ClientError as e:
        print(f"Failed to upload: {e}")
        return None
