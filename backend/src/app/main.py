from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api.v1.router import api_router
from app.core.config import settings
from app.utils.logging import get_logger

# Initialize logger
logger = get_logger("main")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI-driven Marketing Tool API",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    logger.info(f"Configuring CORS with origins: {settings.BACKEND_CORS_ORIGINS}")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)
logger.info(f"API router included with prefix: {settings.API_V1_STR}")

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to AI Marketing Tool API"}

if __name__ == "__main__":
    logger.info("Starting application server")
    # For development with self-signed certificate
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
    #     ssl_keyfile="./certs/key.pem",
    #     ssl_certfile="./certs/cert.pem",
    )