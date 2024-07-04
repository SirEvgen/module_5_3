class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        elif isinstance(other, House):
            return House(self.name + '+' + other.name, self.number_of_floors + other.number_of_floors)
        else:
            print('Некорректный ввод данных')

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, other):
        return House(self.name, self.number_of_floors + other)

    def __eq__(self, other):
        if isinstance(other, int) or self.number_of_floors:
            return isinstance(other, House) and self.number_of_floors == other.number_of_floors
        elif isinstance(other, House):
            return House(self.name == other.name and self.number_of_floors == other.number_of_floors)
        else:
            print('Некорректный ввод данных')

    def __gt__(self, other):
        if isinstance(other, int) or self.number_of_floors:
            return isinstance(other, House) and self.number_of_floors > other.number_of_floors
        elif isinstance(other, House):
            return House(self.number_of_floors > other.number_of_floors)
        else:
            print('Некорректный ввод данных')

    def __ge__(self, other):
        if isinstance(other, int) or self.number_of_floors:
            return isinstance(other, House) and self.number_of_floors >= other.number_of_floors
        elif isinstance(other, House):
            return House(self.number_of_floors >= other.number_of_floors)
        else:
            print('Некорректный ввод данных')

    def __lt__(self, other):
        if isinstance(other, int) or self.number_of_floors:
            return isinstance(other, House) and self.number_of_floors < other.number_of_floors
        elif isinstance(other, House):
            return House(self.number_of_floors < other.number_of_floors)
        else:
            print('Некорректный ввод данных')

    def __le__(self, other):
        if isinstance(other, int) or self.number_of_floors:
            return isinstance(other, House) and self.number_of_floors <= other.number_of_floors
        elif isinstance(other, House):
            return House(self.number_of_floors <= other.number_of_floors)
        else:
            print('Некорректный ввод данных')

    def __ne__(self, other):
        if isinstance(other, int) or self.number_of_floors:
            return isinstance(other, House) and self.number_of_floors != other.number_of_floors
        elif isinstance(other, House):
            return House(self.number_of_floors != other.number_of_floors)
        else:
            print('Некорректный ввод данных')


h1 = House("ЖК Эверест", 10)
h2 = House('ЖК Мегаизба', 20)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
