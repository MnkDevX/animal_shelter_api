from fastapi import FastAPI
from app.core.database import Base, engine

from app.routers.animals import router as animals_router
from app.routers.care import router as care_router
from app.routers.adoptions import router as adoptions_router
from app.auth.auth_router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Animal Shelter API")

app.include_router(auth_router)
app.include_router(animals_router)
app.include_router(care_router)
app.include_router(adoptions_router)