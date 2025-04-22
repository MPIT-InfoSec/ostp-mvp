from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import jd
from app.web import web_ui

# -------------------------------------------------------
# FastAPI App Initialization
# -------------------------------------------------------

app = FastAPI(
    title="Job Description Generator API",
    description="An Agentic AI-powered backend to generate structured job descriptions from natural language prompts.",
    version="1.0.0",

    # Contact metadata for Swagger docs
    contact={
        "name": "Pradyumna Das Roy",
        "url": "https://mpitinfosec.com/",
        "email": "pradyumna.roy@mpitinfosec.com",
    },

    # License metadata
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },

    # Swagger and ReDoc URLs
    docs_url="/docs",    # Swagger UI (interactive playground)
    redoc_url="/redoc"   # ReDoc (read-only reference docs)
)

# -------------------------------------------------------
# 🧩 Include API Routes
# -------------------------------------------------------

# Mount the API endpoints under /api
app.include_router(jd.router, prefix="/api")

# Mount the HTML UI (FastAPI + Jinja2)
app.include_router(web_ui.router)

# Serve static files (CSS, JS) for UI at /static/
app.mount("/static", StaticFiles(directory="app/web/static"), name="static")
