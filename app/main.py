from fastapi import FastAPI

from app.database.database import engine
from app import models
from app.routers import auth,season,anime


models.Base.metadata.create_all(bind=engine)

title = 'Projeto Aprendendo FastAPI'
version = '0.1.0'
summary = 'Projeto base com Auth em JWT, encriptação, e gestão de usuários'

contact = {
    "name": "Kleberson da Silva Romero",
    #"url": "https://romerosolutions.com.br",
    "email": "klebersondsromero@gmail.com"
}

servers = [
    {"url": "http://127.0.0.1:8000", "description": "Development environment"},
    {"url": "https://prod.example.com", "description": "Production environment"},
]

terms_of_service = "http://example.com/terms/"

license_info={
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}

app = FastAPI(
    title=title,
    version=version,
    summary=summary,
    contact = contact,
    terms_of_service=terms_of_service,
    servers=servers,
    license_info=license_info
)


app.include_router(auth.router, prefix='/auth', tags=['Authentication'])
app.include_router(season.router, prefix='/seasons', tags=['Season'])
app.include_router(anime.router, prefix='/animes', tags=['Animes'])

