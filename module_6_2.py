# Создаём класс транспорт
class Vehicle:
# атрибут класса - цветовая гамма
    __COLOR_VARIANTS = ['red', 'green', 'magenta', 'blue', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):

        self.__model = model
        self.__color = color

        self.__engine_power = engine_power
        self.owner = owner
# Каждый объект Vehicle должен содержать следующий методы:
# модель
    def get_model(self):
        return self.__model
# мощность двигателя
    def get_horsepower(self):
        return self.__engine_power
# цвет транспорта
    def get_color(self):
        return self.__color
# Метод set_color - принимает аргумент new_color(str),меняет цвет color на new_color,
# если он есть в списке COLOR_VARIANTS,в противном случае выводит на экран надпись:"Нельзя сменить цвет"
    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

# Метод print_info - распечатывает результаты методов
    def print_info(self):
        print("Модель:", self.get_model())
        print("Мощность:", self.get_horsepower())
        print("Цвет:", self.get_color())
        print("Владелец:", self.owner)

# Класс Седан - наследник класса Vehicle.
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Dimon', 'Volkswagen Passat', 'Black', 180)

vehicle1.print_info()

vehicle1.set_color('Orange')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Kolyan'

vehicle1.print_info()