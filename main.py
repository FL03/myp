from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api import index

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
