from fastapi import APIRouter


class ServiceAPIRouter(APIRouter):
    """Aggregates all routers for API v1."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
