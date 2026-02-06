from fastapi import APIRouter

from infograph.svc.api.v1.routers.health_router import HealthRouter


class ServiceAPIRouter(APIRouter):
    """Aggregates all routers for API v1."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        health_router = HealthRouter()
        self.include_router(health_router, tags=["Health"])
