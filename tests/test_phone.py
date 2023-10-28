import pytest
from src.item import Phone
def test_init_phone(get_phone):
    assert str(get_phone) == 'hello'

def test_repr(get_phone):
    assert repr(get_phone) == "Phone('hello', 100, 5, 4)"

def test_number_of_sim(get_phone):
    assert get_phone.number_of_sim == 4
    get_phone.number_of_sim = 2
    assert get_phone.number_of_sim == 2
    with pytest.raises(ValueError):
        get_phone.number_of_sim = 0
