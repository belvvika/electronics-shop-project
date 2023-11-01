import pytest
from src.keyboard import KeyBoard

def test_init_keyboard(get_keyboard):
    assert str(get_keyboard) == 'hello'

def test_change_lang(get_keyboard):
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
