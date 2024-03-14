import uvicorn
from fastapi import FastAPI

from api_v1 import router as router_v1
from app.core.config import settings
from app.core.database import engine
from app.core.models import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(router=router_v1, prefix="/api_v1")
    create_tables()
    return app


app = start_application()


@app.get("/")
def root():
    return {"message": "Welcome to restful api!"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
