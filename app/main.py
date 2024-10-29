from fastapi import FastAPI

from app.database.database import engine
from app import models
from app.config import swagger as config
from app.routers import auth,season,anime

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=config.title,
    version=config.version,
    summary=config.summary,
    contact = config.contact,
    terms_of_service=config.terms_of_service,
    servers=config.servers,
    license_info=config.license_info
)

app.include_router(auth.router)
app.include_router(season.router)
app.include_router(anime.router)

