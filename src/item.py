import csv
import os.path

class InstantiateCSVError(Exception):
    pass

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        '''
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        '''
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __add__(self, other):
        """
        Складывает экземляры класса
        """
        if not isinstance(other, Item):
            raise ValueError
        return self.quantity + other.quantity

    def __repr__(self):
        return f'Item(\'{self.name}\', {self.price}, {self.quantity})'

    def __str__(self):
        return self.__name
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        '''
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        '''
        cls.all.clear()
        try:
            with open(os.path.join(os.path.dirname(__file__),'items.csv')) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                for row in reader:
                    item = cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except Exception:
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(number):
        '''
        Возвращает число из числа-строки
        '''
        try:
            return int(float(number))
        except ValueError:
            raise ValueError('Эта строка не содержит число.')
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_new):
        if len(name_new) > 10:
            self.__name = name_new[:10]
        else:
            self.__name = name_new
