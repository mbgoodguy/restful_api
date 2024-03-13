import uvicorn
from fastapi import FastAPI

from api_v1 import router as router_v1
from app.core.config import settings

# # lifespan_events - интерфейс для обработки создания и остановки приложения (что будет выполнено до и после)
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with db_helper.engine.begin() as connection:
#         await connection.run_sync(Base.metadata.create_all)
#
#     yield


app = FastAPI()
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def root():
    return {"message": "Welcome to restful api!"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
