from fastapi import UploadFile, File

from src.URLShortener.dependencies import s3_session
from src.config import BUCKET_NAME


async def upload_file_to_s3(unique_name: str, file: UploadFile = File(...), ):
    async with s3_session.client("s3") as s3:
        await s3.upload_fileobj(file.file, BUCKET_NAME, unique_name)


async def stream_file_from_s3(unique_name: str):
    async def s3_stream():
        async with s3_session.client("s3") as s3:
            result_object = await s3.get_object(Bucket=BUCKET_NAME, Key=f'{unique_name}')
            async for chunk in result_object['Body']:
                yield chunk

    return s3_stream
