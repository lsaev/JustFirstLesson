a = float(input('Вклад в размере: '))
b = float(input('Срок: '))

for i in range(int(b)):
    x = a + a * 0.1
    a = x

print("Result: " + str('%.2f' % x))
