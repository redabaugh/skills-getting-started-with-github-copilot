import pytest
from fastapi.testclient import TestClient
import copy
from src.app import app, activities as app_activities


@pytest.fixture
def client():
    """Create a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test"""
    # Store original activities
    original_activities = copy.deepcopy(app_activities)
    
    # Yield control to the test
    yield
    
    # Restore activities after test
    app_activities.clear()
    app_activities.update(original_activities)
