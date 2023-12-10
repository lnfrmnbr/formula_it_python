import doctest


class Pen:
    def __init__(self, number_of_ink: float, ink_color: str):
        """
        Создание и подготовка к работе объекта "Ручка"

        :param number_of_ink: количество чернив в мл
        :param ink_color: цвет чернил

        Пример:
        >>> pen = Pen(2, "black")
        """
        if not isinstance(number_of_ink, (int, float)):
            raise TypeError("количество чернил должно быть типа int или float")
        if number_of_ink < 0:
            raise ValueError("количество чернид должно быть положительным числом или 0")
        self.number_of_ink = number_of_ink

        if not isinstance(ink_color, str):
            raise TypeError("цвет чернил должен быть str")
        self.ink_color = ink_color

    def is_empty(self) -> bool:
        """
        Функция, которая проверяет является ли ручка непишущей

        :return: является ли ручка непишущей

        Пример:
        >>> pen = Pen(0, "green")
        """

    def add_ink(self, added_ink: float, color_of_added_ink: str) -> None:
        """
        Функция, которая добавляет чернила в ручку, только если цвета чернил совпадают

        :param added_ink: количество добавляемых чернил
        :param color_of_added_ink: цвет добавляемых чернил

        Пример:
        >>> pen = Pen(0.2, "blue")
        >>> pen.add_ink(333, "black")
        """
        if not isinstance(added_ink, (int, float)):
            raise TypeError("Добавляемые чернила должны быть типа int или float")
        if added_ink < 0:
            raise ValueError("Добавляемые чернила должны положительным числом")
        if not isinstance(color_of_added_ink, str):
            raise TypeError("цвет добавляемых чернил должен быть str")


if __name__ == "__main__":
    doctest.testmod()
