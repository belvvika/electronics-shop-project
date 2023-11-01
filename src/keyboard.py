from src.item import Item

class Key_Lang():
    def __init__(self, language: str = 'EN'):
        self.__language = language
    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, Key_Lang):
    def __init__(self, name: str, price: float, quantity: int, language: str =  'EN') -> None:
        super().__init__(name, price, quantity)
        Key_Lang.__init__(self, language)
