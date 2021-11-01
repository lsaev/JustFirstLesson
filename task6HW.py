a = int(input("First value: "))
b = int(input("Second value: "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)

