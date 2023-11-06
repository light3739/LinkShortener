from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession

from src.URLShortener.dependencies import validate_download_data
from src.URLShortener.models import Url
from src.URLShortener.schemas import FileUpload, FileDownload
from src.URLShortener.service import upload_file, download_file
from src.database import get_async_session

router = APIRouter(
    tags=["Operation"]
)


@router.post("/upload")
async def upload(is_password: bool = Form(...),
                 file: UploadFile = File(...),
                 database: AsyncSession = Depends(get_async_session)):
    file_data = FileUpload(is_password=is_password)
    return await upload_file(file_data, database, file)


@router.get("/download")
async def download(file_data_download: FileDownload = Depends(), db_url: Url = Depends(validate_download_data)):
    return await download_file(file_data_download, db_url)
