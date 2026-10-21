from copy import deepcopy
from typing import Iterator

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> Iterator[TestClient]:
    original_activities = deepcopy(activities)
    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(original_activities)
