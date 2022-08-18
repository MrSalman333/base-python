from fastapi.testclient import TestClient

from tests.data import SeedData


def test_auth_errors(client: TestClient, seed_data: SeedData):
    """
    TODO: right tests here
    """
