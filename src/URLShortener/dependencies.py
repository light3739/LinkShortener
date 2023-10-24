from aioboto3 import Session

from src.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

s3_session = Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
