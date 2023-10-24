# crud.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.URLShortener.models import Url


async def get_url_by_short_url(database: AsyncSession, short_url: str):
    db_url = await database.execute(select(Url).where(Url.short_url == short_url))
    return db_url.scalars().first()


async def add_url_to_db(database: AsyncSession, db_url: Url):
    database.add(db_url)
    await database.commit()
    await database.refresh(db_url)  # Refresh to get the auto-generated ID
    return db_url
