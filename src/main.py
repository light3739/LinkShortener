from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse

from src.URLShortener.models import Url
from src.URLShortener.router import router as url_router
from src.database import get_async_session

BUCKET_NAME = 'fastdropbucket'

app = FastAPI()

origins = [
    "http://localhost:3000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{short_url}")
async def get_original_url(short_url: str, database: AsyncSession = Depends(get_async_session)):
    db_url = await database.execute(select(Url).where(Url.short_url == short_url))
    db_url = db_url.scalars().first()

    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(db_url.original_url)


app.include_router(url_router)
