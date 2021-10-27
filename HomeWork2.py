n = abs(int(input('Ввод: \n ')))

h = (n // 3600)
m = ((n % 3600) // 60)
s = (n % 3600 % 60)

print( 'Сейчас ' + str(h) + ':' + str(m) + ':' + str(s))