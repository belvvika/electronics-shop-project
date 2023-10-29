"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone

def test_init_item(get_item):
    assert get_item

def test_calculate_total_price(get_item):
    assert get_item.calculate_total_price() == 500

def test_apply_discount(get_item):
    item = get_item
    item.pay_rate = 0.8
    assert item.apply_discount() == 80

def test_instantiate_from_csv(get_item):
   Item.instantiate_from_csv()
   assert len(Item.all) == 5

def test_string_to_number(get_item):
    assert get_item.string_to_number('5.1') == 5
    assert get_item.string_to_number('55.5') == 55
    with pytest.raises(ValueError):
        assert get_item.string_to_number('hello')

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'

def test_init_phone(get_phone):
    assert str(get_phone) == 'hello'

def test_add(get_item, get_phone):
    assert get_phone + get_phone == 10
    with pytest.raises(ValueError):
        assert get_phone + 4