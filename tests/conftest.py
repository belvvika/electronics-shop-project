import pytest
from src.item import Item

@pytest.fixture
def get_Item():
    return Item('hello', 100, 5 )
