from fastapi import APIRouter, Request


class APIRouterBase(APIRouter):
    """Base router that provides shared utilities for all routers."""

    async def get_locale(self, request: Request) -> str:
        """Extract locale from request headers."""
        accept_language = request.headers.get("Accept-Language", "en-US")
        return accept_language.split(",")[0].strip()
