from calculator import Cсalculator  # Импортировал метод из файла calculator.py

if __name__ == "__main__":
    # Принял два значения от пользователя
    a = int(input("Введите вес груза: "))
    b = int(input("Введите номер этажа: "))

    # Вызывал метод из calculator.py и вывел результат
    result = Ccalculator(a, b)
    print(f"Результат: {result}")