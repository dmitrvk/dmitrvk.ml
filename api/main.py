from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr


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


class SendMail(BaseModel):
    email: EmailStr


@router.post('/mail')
async def send_mail(request_body: SendMail) -> None:
    print(f'Received email "{request_body.email}"')


app.include_router(router, prefix='/api')
