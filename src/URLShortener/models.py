from typing import Optional

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped, declarative_base

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class Url(Base):
    __tablename__ = "files"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    file_name: Mapped[str] = Column(String, index=True)
    short_url: Mapped[Optional[str]] = Column(String, index=True, unique=True)
    password: Mapped[Optional[str]] = Column(String)
