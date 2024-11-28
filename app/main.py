from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import database
from . import routes as routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(routes.items_router, prefix="/items", tags=["Items"])
app.include_router(routes.assets_stocks_router, prefix="/stocks", tags=["Stocks"])
