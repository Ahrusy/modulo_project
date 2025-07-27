# modulo.py

def modulo(a: int, b: int) -> int:
    """
    Возвращает остаток от деления a на b.

    :param a: Делимое (целое число)
    :param b: Делитель (целое число, не равный 0)
    :return: Остаток от деления a на b
    :raises ZeroDivisionError: Если b == 0
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a % b
