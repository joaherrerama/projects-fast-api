from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from app.main import app

client = TestClient(app)

def test_create_project_with_polygon():
    project_data = {
        "name": "Test Project",
        "description": "Test Description",
        "start_date": datetime.now().isoformat(),
        "end_date": (datetime.now() + timedelta(days=30)).isoformat(),
        "area_of_interest": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]]]
        }
    }
    response = client.post("/api/projects/", json=project_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == project_data["name"]
    assert "id" in data

def test_create_project_with_multipolygon():
    project_data = {
        "name": "Test MultiPolygon Project",
        "description": "Test Description",
        "start_date": datetime.now().isoformat(),
        "end_date": (datetime.now() + timedelta(days=30)).isoformat(),
        "area_of_interest": {
            "type": "MultiPolygon",
            "coordinates": [
                [[[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]]],
                [[[2, 2], [2, 3], [3, 3], [3, 2], [2, 2]]]
            ]
        }
    }
    response = client.post("/api/projects/", json=project_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == project_data["name"]
    assert "id" in data

def test_invalid_geometry_type():
    project_data = {
        "name": "Invalid Geometry Project",
        "description": "Test Description",
        "start_date": datetime.now().isoformat(),
        "end_date": (datetime.now() + timedelta(days=30)).isoformat(),
        "area_of_interest": {
            "type": "Point",
            "coordinates": [0, 0]
        }
    }
    response = client.post("/api/projects/", json=project_data)
    assert response.status_code == 422