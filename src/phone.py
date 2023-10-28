from src.item import Item


class Phone(Item):
    """
    Класс для представления товара в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim
    def __repr__(self):
        return f'Phone(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if number > 0 and isistance(number, int):
            self.__number_of_sim = number
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
