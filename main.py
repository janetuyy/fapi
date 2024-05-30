from contextlib import asynccontextmanager
from core.models import Base, db_helper
import uvicorn
# from items_views import router as items_router
from fastapi import FastAPI
from users.views import router as users_router
from products.views import router as products_router
from auth.jwt_auth import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
# app.include_router(items_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(products_router)

@app.get("/")
def hello_index():
    return {"message": "Hello index!"}


@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
