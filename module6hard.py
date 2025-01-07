from math import pi

class Figure:
    sides_count = 0

    def __init__(self, r, g, b, *sides, filled = True):
        self.__color = [r, g, b]
        self.__sides = list(sides)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if not isinstance(i, int) or i <= 0:
                    return False
            return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, r, g, b, *sides, filled = True):
        super().__init__(r, g, b,*sides, filled = True)
        if len(self._Figure__sides) != self.sides_count:
            self._Figure__sides = [1]
        self.__radius = round(((self.__len__())/(2*pi)), 2)

    def get_square(self):
        return round(((self.__len__())**2)/(4*pi), 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, r, g, b, *sides, filled = True):
        super().__init__(r, g, b,*sides, filled = True)
        if len(self._Figure__sides) != self.sides_count or (self._Figure__sides[0] + self._Figure__sides[1] < self._Figure__sides[2] or self._Figure__sides[0] + self._Figure__sides[2] < self._Figure__sides[1] or self._Figure__sides[2] + self._Figure__sides[1] < self._Figure__sides[0]):
            self._Figure__sides = [1, 1, 1]

    def get_square(self):
        p = (self.__len__())/2
        return round((p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))**0.5, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, r, g, b, *sides, filled = True):
        super().__init__(r, g, b,*sides, filled = True)
        if len(self._Figure__sides) != 1:
            self._Figure__sides = [1] * self.sides_count
        else:
            self._Figure__sides = self._Figure__sides * self.sides_count

    def get_volume(self):
        return self._Figure__sides[0] ** 3

# circle1 = Circle(200, 200, 100, 10) # (Цвет, стороны)
# cube1 = Cube(222, 35, 130, 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())
