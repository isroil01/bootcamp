import uvicorn
from fastapi import FastAPI

from app.setting import Settings

settings = Settings()

app = FastAPI()


def main():
    uvicorn.run("app.main:app", host=settings.host_address, port=settings.port, log_level="debug")
