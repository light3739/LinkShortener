from typing import Optional

from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession

from src.URLShortener.schemas import FileUpload, FileDownload
from src.URLShortener.service import upload_file, download_file
from src.database import get_async_session

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.post("/upload")
async def upload(is_password: bool = Form(...),
                 file: UploadFile = File(...),
                 database: AsyncSession = Depends(get_async_session)):
    file_data = FileUpload(is_password=is_password)
    return await upload_file(file_data, database, file)


@router.get("/download")
async def download(short_url: str, password: Optional[str] = None, database: AsyncSession = Depends(get_async_session)):
    file_data_download = FileDownload(short_url=short_url, password=password)
    return await download_file(file_data_download, database)