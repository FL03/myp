from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

from app.api import index
from app.core.session import session

app: FastAPI = FastAPI()


@app.on_event("startup")
async def startup():
    print("Initializing connections...")


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.on_event("shutdown")
async def shutdown():
    print("Terminating application...")


app.include_router(router=index.router)
register_tortoise(
    add_exception_handlers=True,
    app=app,
    db_url=session.settings.databases[0].uri,
    generate_schemas=True,
    modules=dict(models=["app.data.models"])
)
