import click
from fastapi import FastAPI
from uvicorn import Config, Server

from infograph.svc.api_service import create_app


@click.command()
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=8000, help="Port to bind to")
def main(host: str, port: int):
    """Start the FastAPI service."""
    app: FastAPI = create_app()
    config = Config(app=app, host=host, port=port, log_level="info")
    server = Server(config)
    server.run()
