from fastapi import UploadFile, File
from pydantic import BaseModel


class UrlIn(BaseModel):
    filename: str


class FileUpload(BaseModel):
    file: UploadFile = File(...)
    short_url: str
