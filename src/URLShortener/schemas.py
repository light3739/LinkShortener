from typing import Optional

from pydantic import BaseModel, Field


class UrlBase(BaseModel):
    original_url: str = Field(..., description="The original URL to be shortened")


class UrlCreate(UrlBase):
    pass


class Url(UrlBase):
    id: int = Field(..., description="The ID of the shortened URL")
    short_url: Optional[str] = Field(None, description="The shortened URL")

    class Config:
        orm_mode = True
