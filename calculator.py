import math

#Метод рассчета суммы
def Ccalculator(x, y, z):
    if z == "да" or "Да":
        l = 0
    else:
        l = 1

    multiple = math.ceil(x / 100)
    if x <= 50:
        return 300 + 300 * multiple * (y - 1) * l
    elif x <= 100:
        return 1000 + 300 * multiple * (y - 1) * l
    elif x <= 300:
        return 2000 + 300 * multiple * (y - 1) * l
    elif (x <= 0 or x > 300) or y < 1:
        return "error" 