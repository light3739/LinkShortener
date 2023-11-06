from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse

from src.URLShortener.models import Url
from src.URLShortener.router import router as url_router
from src.database import get_async_session

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
origins = [
    "http://localhost:3000",
]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

  #TODO
# @app.get("/{short_url}")
# async def get_original_url(short_url: str, database: AsyncSession = Depends(get_async_session)):
#     db_url = await database.execute(select(Url).where(Url.short_url == short_url))
#     db_url = db_url.scalars().first()
#
#     if db_url is None:
#         raise HTTPException(status_code=404, detail="URL not found")
#
#     return RedirectResponse(db_url.original_url)


app.include_router(url_router)
