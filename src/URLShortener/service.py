from urllib.parse import quote

from fastapi import UploadFile, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import StreamingResponse

from src.URLShortener.crud import get_url_by_short_url, add_url_to_db
from src.URLShortener.models import Url
from src.URLShortener.s3_service import stream_file_from_s3, upload_file_to_s3
from src.URLShortener.schemas import FileUpload
from src.URLShortener.utils import generate_short_url, generate_unique_name, generate_and_hash_password


async def upload_file(file_data: FileUpload, database: AsyncSession, file: UploadFile = File(...)):
    file_data.short_url = generate_short_url()
    password = None
    if file_data.is_password:
        password = generate_and_hash_password()
    db_url = Url(file_name=file.filename, short_url=file_data.short_url, password=password)  # Store the password
    unique_name = generate_unique_name(file.filename, file_data.short_url)
    await upload_file_to_s3(unique_name, file)
    await add_url_to_db(database, db_url)
    return "all done"


async def download_file(database: AsyncSession, short_url: str):
    db_url = await get_url_by_short_url(database, short_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    unique_name = generate_unique_name(db_url.file_name, short_url)
    s3_stream = await stream_file_from_s3(unique_name)
    filename = quote(db_url.file_name)
    response = StreamingResponse(s3_stream())
    response.headers['Content-Disposition'] = f'attachment; filename*=UTF-8\'\'{filename}'
    return response
