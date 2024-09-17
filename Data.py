from calculator import Ccalculator  # Импортировал метод из файла calculator.py

if __name__ == "__main__":
    # Принял три значения от пользователя
    a = int(input("Введите вес груза: "))
    b = int(input("Введите номер этажа: "))
    c = str(input("У вас есть лифт?"))

    # Вызывал метод из calculator.py и вывел результат
    result = Ccalculator(a, b)
    print(f"Результат: {result}")