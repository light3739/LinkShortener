from urllib.parse import quote

from fastapi import UploadFile, File, Depends, HTTPException
from fastapi.responses import UJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import StreamingResponse

from src.URLShortener.constants import UPLOAD_SUCCESS_MESSAGE
from src.URLShortener.crud import add_url_to_db
from src.URLShortener.dependencies import validate_download_data
from src.URLShortener.models import Url
from src.URLShortener.s3_service import stream_file_from_s3, upload_file_to_s3
from src.URLShortener.schemas import FileUpload, FileDownload
from src.URLShortener.utils import generate_short_url, generate_unique_name
from src.database import get_async_session


async def upload_file(file_data: FileUpload, database: AsyncSession = Depends(get_async_session),
                      file: UploadFile = File(...)):
    file_data.short_url = generate_short_url()
    password = generate_short_url() if file_data.is_password else None
    db_url = Url(file_name=file.filename, short_url=file_data.short_url, password=password)
    unique_name = generate_unique_name(file.filename, file_data.short_url)

    try:
        await upload_file_to_s3(unique_name, file)
        await add_url_to_db(database, db_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    response_content = {"message": UPLOAD_SUCCESS_MESSAGE, "url": file_data.short_url}
    if password is not None:
        response_content["password"] = password

    return UJSONResponse(content=response_content, status_code=200)


async def download_file(file_data_download: FileDownload = Depends(), db_url: Url = Depends(validate_download_data)):
    try:
        unique_name = generate_unique_name(db_url.file_name, file_data_download.short_url)
        s3_stream = await stream_file_from_s3(unique_name)
        filename = quote(db_url.file_name)
        response = StreamingResponse(s3_stream(),
                                     headers={'Content-Disposition': f'attachment; filename*=UTF-8\'\'{filename}'})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response
