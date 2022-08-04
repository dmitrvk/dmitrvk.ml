from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=('http://localhost:3000',),
    allow_credentials=True,
    allow_methods=('*',),
    allow_headers=('*'),
)


class SendMail(BaseModel):
  email: EmailStr


@app.post('/mail')
async def send_mail(request_body: SendMail) -> None:
  print(f'Received email "{request_body.email}"')
