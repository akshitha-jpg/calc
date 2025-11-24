import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_status_code(client):
    """Home page should return 200 OK."""
    response = client.get("/")
    assert response.status_code == 200

def test_home_content(client):
    """Home page should contain the movie list."""
    response = client.get("/")
    html = response.get_data(as_text=True)

    assert "<h1>🎬 Simple Movie Site</h1>" in html
    assert "The Shawshank Redemption" in html
    assert "Inception" in html
    assert "Interstellar" in html
    assert "The Dark Knight" in html
    assert "Avengers: Endgame" in html
