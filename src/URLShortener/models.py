from typing import Optional

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, Mapped

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Url(Base):
    __tablename__ = "urls"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    original_url: Mapped[str] = Column(String, index=True)
    short_url: Mapped[Optional[str]] = Column(String, index=True, unique=True)
