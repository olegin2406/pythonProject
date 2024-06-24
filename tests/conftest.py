import pytest
from src.processing import filter_by_state, sort_by_date, original_state

@pytest.fixture
def test_original_state():
    return 'EXECUTED'

@pytest.fixture
def test_original_state_1():
    return original_state