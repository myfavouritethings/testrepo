from fastapi.testclient import TestClient
import pytest
from app.main import create_app
from app.core.config import settings

# Create a test client that can be used in tests
@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    with TestClient(app) as client:
        yield client


def test_health_check(test_client):
    """
    Test the health check endpoint.
    """
    response = test_client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
    }
