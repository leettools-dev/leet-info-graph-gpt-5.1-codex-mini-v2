from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


from infograph.svc.api.v1.api import ServiceAPIRouter
from infograph.svc.api_router_base import APIRouterBase


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title="Research Infograph Assistant",
        version="0.1.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    api_router = ServiceAPIRouter()
    app.include_router(api_router, prefix="/api/v1")

    @app.exception_handler(Exception)
    async def generic_exception_handler(request, exc):
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"},
        )

    return app
