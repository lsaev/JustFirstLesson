v = str("прямоугольник")
t = str("треугольник")
k = str("круг")
p = 3.14

x = input('Выбери фигуру: прямоугольник, треугольник или круг! ')
if x == v:
    a = float(input('Введи длину первой стороны: '))
    b = float(input('Введи длину второй стороны: '))
    s = (a * b)
    print("Площадь прямоугольника: " + str(s))

if x == t:
    a = float(input('Введи длину первой стороны: '))
    b = float(input('Введи длину второй стороны: '))
    c = float(input('Введи длину третьей стороны: '))
    n = ((a + b + c) / 2)
    print("Площадь треугольника: " + str((n * (n -a) * (n - b) * (n - c)) ** 0.5))

if x == k:
    r = float(input('Введи радиус: '))
    print("Площадь круга: " + str(p * r ** 2))
