from typing import Union

from fastapi import UploadFile, File
from pydantic import BaseModel, Field


class UrlIn(BaseModel):
    filename: str


class FileUpload(BaseModel):
    short_url: str = None
    is_password: bool = None
