"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_init_item(get_Item):
    assert get_Item

def test_calculate_total_price(get_Item):
    assert get_Item.calculate_total_price() == 500

def test_apply_discount(get_Item):
    item = get_Item
    item.pay_rate = 0.8
    assert item.apply_discount() == 80

def test_instantiate_from_csv():
   pass
def test_string_to_number():
    pass

