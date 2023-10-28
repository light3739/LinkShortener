from aioboto3 import Session
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.URLShortener.crud import get_url_by_short_url
from src.URLShortener.schemas import FileDownload
from src.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

s3_session = Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


async def validate_download_data(file_data_download: FileDownload, database: AsyncSession):
    db_url = await get_url_by_short_url(database, file_data_download.short_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    if db_url.password and db_url.password != file_data_download.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return db_url  # ensure to return db_url
