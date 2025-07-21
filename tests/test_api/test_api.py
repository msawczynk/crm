from fastapi.testclient import TestClient

from api import app
from retrieval import index


def test_query_endpoint() -> None:
    index({"http://a": "hello world"})
    client = TestClient(app)
    response = client.get("/query", params={"q": "hello"})
    assert response.status_code == 200
    data = response.json()
    assert data[0]["url"] == "http://a"
