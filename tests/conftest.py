import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture
def get_Item():
    return Item('hello', 100, 5 )

@pytest.fixture
def get_Phone():
    return Item('hello', 100, 5, 4)
