"""Smoke tests for Mon Gâteau Flask app. Uses mocked MongoDB for CI."""
from unittest.mock import MagicMock, patch


def _make_mock_collection():
    """Create a mock MongoDB collection with common operations."""
    coll = MagicMock()
    coll.find.return_value = []
    coll.find_one.return_value = None
    coll.count_documents.return_value = 0
    coll.insert_one.return_value = MagicMock(inserted_id="abc123")
    coll.update_one.return_value = MagicMock(matched_count=1)
    coll.delete_one.return_value = MagicMock(deleted_count=1)
    return coll


def _make_mock_client():
    """Create a mock MongoClient that returns the mock collection for cakedb.cakes."""
    client = MagicMock()
    db = MagicMock()
    coll = _make_mock_collection()
    db.__getitem__.return_value = coll
    client.__getitem__.return_value = db
    return client


@patch("pymongo.MongoClient")
def test_app_imports(mock_mongo):
    """Verify the app module can be imported with mocked MongoDB."""
    mock_mongo.return_value = _make_mock_client()
    from app import app
    assert app is not None


@patch("pymongo.MongoClient")
def test_index_returns_200(mock_mongo):
    """Verify the index route returns 200."""
    mock_mongo.return_value = _make_mock_client()
    from app import app
    with app.test_client() as c:
        r = c.get("/")
        assert r.status_code == 200


@patch("pymongo.MongoClient")
def test_api_cakes_returns_list(mock_mongo):
    """Verify the /api/cakes endpoint returns JSON list."""
    mock_mongo.return_value = _make_mock_client()
    from app import app
    with app.test_client() as c:
        r = c.get("/api/cakes")
        assert r.status_code == 200
        assert r.json == []
