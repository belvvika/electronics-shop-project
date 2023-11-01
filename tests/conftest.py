import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard, Key_Lang

@pytest.fixture
def get_item():
    return Item('hello', 100, 5 )

@pytest.fixture
def get_phone():
    return Phone('hello', 100, 5, 4)

@pytest.fixture
def get_keyboard():
    return KeyBoard('hello', 100, 5, 'EN')
