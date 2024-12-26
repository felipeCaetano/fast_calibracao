from http import HTTPStatus
from fastapi import FastAPI
from calibracao.schemas import Message, UserPublic, UserSchema

app = FastAPI()

@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    ...