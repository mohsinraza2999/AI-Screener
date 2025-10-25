from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

#from app.core.config import settings
from app.core.logger import get_logger
from app.api.routes import screening, health

logger = get_logger(__name__)

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Screener",
        description="AI-powered CV and Job Description screener",
        version="1.0.0"
    )

    # CORS (allow frontend to connect)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # tighten this in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routes
    app.include_router(health.router, tags=["health"])
    app.include_router(screening.router, tags=["Screening"])

    return app

app = create_app()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Serve index.html at root
@app.get("/")
def read_index():
    return FileResponse(os.path.join("frontend", "index.html"))
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 AI Screener API starting up...")
    logger.info(f"Select Default model: settings.MODEL_TYPE")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 AI Screener API shutting down...")
