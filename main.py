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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8001, host="0.0.0.0", reload=True)
