from fastapi import FastAPI
from src.main.routes import books
from src.database.connect import engine
from src.database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["books"])
