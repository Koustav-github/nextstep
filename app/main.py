from fastapi import FastAPI
from app.api.routes import root

from app.db.base import Base
from app.db.session import engine

app = FastAPI()

app.include_router(root.router)

Base.metadata.create_all(bind=engine)
