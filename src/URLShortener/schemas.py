from typing import Optional

from pydantic import BaseModel


class FileUpload(BaseModel):
    short_url: str = None
    is_password: bool = None


class FileDownload(BaseModel):
    short_url: str
    password: Optional[str] = None
