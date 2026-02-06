from infograph.svc.api_router_base import APIRouterBase


class HealthRouter(APIRouterBase):
    """Health check endpoints."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.get("/health")
        async def health_check() -> dict:
            return {"status": "ok"}
