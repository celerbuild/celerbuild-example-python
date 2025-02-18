from fastapi import FastAPI
from typing import Dict
from app.config import settings  # Import settings from config.py

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,  # Use app_name from settings
    version=settings.version  # Use version from settings
)

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World from CelerBuild!"}

@app.get("/version")
async def version() -> Dict[str, str]:
    return {"version": settings.version}  # Use version from settings