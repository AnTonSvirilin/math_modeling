fio = 'Anton Svir Kir'

fiolower = fio.lower()
fiolower1 = [ord(symbol) for symbol in fiolower]

fioupper = fio.upper()
fioupper1 = [ord(symbol) for symbol in fioupper]


a = sum(fiolower1)
b = sum(fioupper1)
c = a + b

print(c)