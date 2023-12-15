from fastapi import FastAPI
import uvicorn

import models
from database import engine
from routers import subjects

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(subjects.router, prefix="/subjects")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
