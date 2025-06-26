import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    """DRF APIClient for making HTTP requests in tests."""
    return APIClient()