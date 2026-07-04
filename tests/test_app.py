import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from app import app

client = app.test_client()


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "DevOps Flask CI/CD Pipeline"
    assert data["status"] == "Running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "UP"


def test_ready():
    response = client.get("/ready")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "READY"


def test_version():
    response = client.get("/version")

    assert response.status_code == 200

    data = response.get_json()

    assert data["version"] == "1.0.0"


def test_invalid_route():
    response = client.get("/invalid")

    assert response.status_code == 404

    data = response.get_json()

    assert data["status"] == 404