# backend/main.py

"""
The backend is responsible for:
- Receiving commands from the iOS app
- Sending commands to the SPIKE Prime hub
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes.api import router as api_router

app = FastAPI()

app.include_router(api_router)
