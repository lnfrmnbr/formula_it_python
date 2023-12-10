import doctest


class Rectangle:
    def __init__(self, side1: float, side2: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param side1: первая сторона прямоугольника
        :param side2: вторая сторона прямоугольника

        Примеры:
        >>> rect = Rectangle(3, 5.22)
        """
        if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float))):
            raise TypeError("стороны прямоугольника должены быть типа int или float")
        if side1 <= 0 or side2 <= 0:
            raise ValueError("стороны прямоугльника должны быть положительными числами")
        self.side1 = side1
        self.side2 = side2

    def area(self) -> float:
        """
         Функция, которая считает площадь прямоугольника

        :return: площадь прямоугольника

        Пример:
        >>> rect = Rectangle(2222, 3)
        >>> rect.area()
        """

    def is_square(self) -> bool:
        """
        Функция, которая проверяет является ли прямоугольник квадратом

        :return: является ли прямоугольник квадратом

        Пример:
        >>> rect = Rectangle(434, 434)
        >>> rect.is_square()
        """


if __name__ == "__main__":
    doctest.testmod()
