import doctest


class Person:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Человек"
        :param name: имя человекка
        :param age: возраст человекка
        Пример:
        >>> person = Person("Jack", 34)
        """
        if not isinstance(age, int):
            raise TypeError("возраст должен быть типа int")
        if age <= 0:
            raise ValueError("возраст должен быть положительным числом")
        self._age = age
        if not isinstance(name, str):
            raise TypeError("имя должно быть str")
        self._name = name

    @property
    def name(self) -> str:
        """
        Геттер для атрибута имя человека
        Пример:
        >>> person = Person("Jack", 34)
        >>> person.name
        'Jack'
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Сеттер для атрибута имя человека
        Пример:
        >>> person = Person("Jack", 34)
        >>> person.name( "Piter" )
        """
        if not isinstance(new_name, str):
            raise TypeError("имя должно быть str")
        else:
            self._name = new_name

    @property
    def age(self) -> int:
        """
        Геттер для атрибута имя человека
        Пример:
        >>> person = Person("Jack", 34)
        >>> person.age
        34
        """
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        """
        Сеттер для атрибута имя человека
        Пример:
        >>> person = Person("Jack", 34)
        >>> person.age(35)
        """
        if not isinstance(new_age, int):
            raise TypeError("возраст должен быть типа int")
        if new_age <= 0:
            raise ValueError("возраст должен быть положительным числом")
        else:
            self._age = new_age

    def __str__(self) -> str:
        return f'Человек "{self._name}"'

    def __repr__(self):
        return f'Person(name=\'{self._name}\', age=\'{self._age}\')'

    def is_child(self) -> bool:
        """
        Функция, которая проверяет является ли человек ребенком
        :return: является ли человек котенком
        Примеры:
        >>> person = Person("Anna", 10)
        >>> person.is_child()
        True
        """
        return self.age < 18

    def can_buy_car(self, fortune: int) -> bool:
        """
        Функция, которая проверяет может ли человек купить машину
        :return: может ли человек купить машину
        Примеры:
        >>> person = Person("Sonya", 45)
        >>> person.can_buy_car(68229)
        False
        """
        return (not self.is_child()) and fortune >= 100000


class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str, num_of_students: int, money_for_student: int):
        """
        Создание и подготовка к работе объекта "Учитель"
        :param name: имя
        :param age: возраст
        :param subject: предмет
        :param num_of_students: количество учеников
        :param money_for_student: ставка за ученика
        Пример:
        >>> teacher = Teacher("Jack", 34, "math", 28, 500)
        """
        super().__init__(name, age)
        if not isinstance(num_of_students, int):
            raise TypeError("количество учеников должно быть типа int")
        if num_of_students < 0:
            raise ValueError("количество учеников должно быть положительным числом")
        if not isinstance(money_for_student, int):
            raise TypeError("ставка за ученика должна быть типа int")
        if money_for_student < 0:
            raise ValueError("ставка за ученика должна быть положительным числом")
        if not isinstance(subject, str):
            raise TypeError("предмет должен быть str")
        self._subject = subject
        self._num_of_students = num_of_students
        self._money_for_student = money_for_student

    @property
    def subject(self) -> str:
        """
        Геттер для атрибута предмет
        Пример:
        >>> teacher = Teacher("Jack", 34, "math", 28, 500)
        >>> teacher.subject
        'math'
        """
        return self._subject

    @subject.setter
    def subject(self, new_subject: str) -> None:
        """
        Сеттер для атрибута предмет
        Пример:
        >>> teacher = Teacher("Jack", 34, "math", 28, 500)
        >>> teacher.subject( "biology" )
        """
        if not isinstance(new_subject, str):
            raise TypeError("имя должно быть str")
        else:
            self._subject = new_subject

    @property
    def num_of_students(self) -> int:
        """
        Геттер для атрибута предмет
        Пример:
        >>> teacher = Teacher("Jack", 34, "math", 28, 500)
        >>> teacher.num_of_students
        28
        """
        return self._num_of_students

    @num_of_students.setter
    def num_of_students(self, new_num_of_students: int) -> None:
        """
        Сеттер для атрибута предмет
        Пример:
        >>> teacher = Teacher("Jack", 34, "math", 28, 500)
        >>> teacher.num_of_students( 30 )
        """
        if not isinstance(new_num_of_students, int):
            raise TypeError("количество учеников должно быть типа int")
        elif new_num_of_students < 0:
            raise ValueError("количество учеников должно быть положительным числом")
        else:
            self._num_of_students = new_num_of_students

    @property
    def money_for_student(self) -> int:
        """
        Геттер для атрибута предмет
        Пример:
        >>> teacher = Teacher("Jack", 34, "math", 28, 500)
        >>> teacher.money_for_student
        500
        """
        return self._money_for_student

    @money_for_student.setter
    def money_for_student(self, new_money_for_student: int) -> None:
        """
        Сеттер для атрибута предмет
        Пример:
        >>> teacher = Teacher("Jack", 34, "math", 28, 500)
        >>> teacher.money_for_student( 30 )
        """
        if not isinstance(new_money_for_student, int):
            raise TypeError("количество учеников должно быть типа int")
        elif new_money_for_student < 0:
            raise ValueError("количество учеников должно быть положительным числом")
        else:
            self._money_for_student = new_money_for_student

    def __str__(self) -> str:
        return f'Учитель "{self._name}" ведет "{self._subject}"'

    def __repr__(self):
        return f'Учитель(name=\'{self._name}\', age=\'{self._age}\', subject= \'{self._subject}\')'

    def can_buy_car(self, fortune: int) -> bool:
        """
        Функция, которая проверяет может ли учитель купить машину
        :return: может ли человек купить машину
        Примеры:
        >>> teacher = Teacher("Jack", 34, "math", 28, 500)
        >>> teacher.can_buy_car(90000)
        True
        """
        salary = self.money_for_student * self.num_of_students
        return fortune + salary >= 100000


if __name__ == "__main__":
    doctest.testmod()
