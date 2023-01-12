from fastapi import FastAPI
from routers import codigoPostalRouter

app = FastAPI()
app.include_router(codigoPostalRouter.router)