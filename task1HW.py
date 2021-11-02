a = input("Первый аргумент: ")
b = input("Второй аргумент: ")

try:
    if float(a) % 1 == 0:
        a = int(a)
    else:
        a = float(a)

    if float(b) % 1 == 0:
        b = int(b)
    else:
        b = float(b)

    if (3 <= a <= 21) and (3 <= b <= 21):
        print('Result:', abs(a - b))
    else:
        print('Result:', str(a) + str(b))
except:
    print('Result:', str(a) + str(b))


