import pathlib
from typing import Final, Generator

from fastapi import APIRouter, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


HOST: Final[str] = 'https://dmitrvk.ml'


app = FastAPI(
    docs_url='/api/docs',
    openapi_url='/api/openapi.json',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=(
      'http://localhost:3000',
      'https://dmitrvk.ml',
    ),
    allow_credentials=True,
    allow_methods=('*',),
    allow_headers=('*'),
)

router = APIRouter()


class Note(BaseModel):
    title: str
    pages: list[str]


@router.get('/notes/{slug}/', response_model=Note)
async def get_note(slug: str) -> Note:
    pages_dir: pathlib.Path = pathlib.Path(f'/public/notes/{slug}/pages/')
    pages: Generator = (f'{HOST}{path}' for path in pages_dir.iterdir())

    if pages_dir.exists():
        return Note(
            title=slug.capitalize(),
            pages=sorted(pages),
        )

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


app.include_router(router, prefix='/api')
