from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.cosmogram_router import get_cosmogram_api_router
from app.db.db import database
import uvicorn
from app.core.config import settings
import swisseph as swe

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    swe.set_ephe_path(settings.SWISSEPH_PATH)
    yield
    await database.disconnect()

app = FastAPI(
    title="Naimix",
    version="0.1.0",
    lifespan=lifespan, 
    swagger_ui_parameters={"syntaxHighlight": settings.SWAGGER_SYNTAX_HIGHLIGHT}
)

router = get_cosmogram_api_router()
app.include_router(router)

def main():
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.REST_PORT, reload=True)

if __name__ == "__main__":
    main()