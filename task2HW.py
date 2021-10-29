a = float(input("First: "))
b = float(input("Second: "))
what = input("Выбери операцию(+, -, *, /): ")

if a >= 3 and a <= 23 and b >= 3 and b <= 23:
    if what == "+":
        c = a + b
        print("Result: " + str(c))
    elif what == "-":
        c = a - b
        print("Result: " + str(c))
    elif what == "*":
        c = a * b
        print("Result: " + str(c))
    elif what == "/":
        c = a / b
        print("Result: " + str(c))
else:
    print("Wrong numbers selected!")
