from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from src.URLShortener.schemas import FileUpload
from src.URLShortener.service import upload_file, download_file
from src.database import get_async_session

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.post("/upload")
async def upload(file: UploadFile = File(...),
                 database: AsyncSession = Depends(get_async_session)):
    file_data = FileUpload(short_url="string", is_password=True)
    return await upload_file(file_data, database, file)


@router.get("/download")
async def download(short_url: str, database: AsyncSession = Depends(get_async_session)):
    return await download_file(database, short_url)
