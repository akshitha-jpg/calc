import pytest
from fastapi.testclient import TestClient
from app import app  # Make sure app.py is in the root

@pytest.fixture
def client():
    """Create a TestClient for testing."""
    return TestClient(app)

def test_home_status_code(client):
    """The home endpoint should return 200 OK."""
    response = client.get("/")
    assert response.status_code == 200

def test_home_content(client):
    """The home endpoint should contain the movie list."""
    response = client.get("/")
    html = response.text

    # Check header
    assert "<h1>🎬 Simple Movie Site</h1>" in html

    # Check each movie is listed
    movies = [
        "The Shawshank Redemption",
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Avengers: Endgame"
    ]

    for movie in movies:
        assert movie in html
