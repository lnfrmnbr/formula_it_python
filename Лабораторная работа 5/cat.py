import doctest


class Cat:
    def __init__(self, age: float, color: str):
        """
        Создание и подготовка к работе объекта "Кот"

        :param age: возраст кота
        :param color: цвет шерсти кота

        Примеры:
        >>> cat = Cat(2.3, "black")
        """
        if not isinstance(age, (int, float)):
            raise TypeError("возраст кота должен быть типа int или float")
        if age <= 0:
            raise ValueError("возраст кота должен быть положительным числом")
        self.age = age

        if not isinstance(color, str):
            raise TypeError("цвет кота должно быть str")
        self.color = color

    def is_kitten(self) -> bool:
        """
        Функция, которая проверяет является ли кот котенком

        :return: является ли кот котенком

        Примеры:
        >>> cat = Cat(8, "white")
        >>> cat.is_kitten()
        """

    def birthday(self) -> None:
        """
         Функция, которая парибавляет 1 год к возрасту кота

         Примеры:
         >>> cat = Cat(33, "purple")
         >>> cat.birthday()
        """

    def change_color(self, new_color: str) -> None:
        """
        Функция, которая меняет цвет кота


        :param new_color: новый цвет кота

        Примеры:
        >>> cat = Cat(0.2, "orange")
        >>> cat.change_color("green")
        """


if __name__ == "__main__":
    doctest.testmod()
