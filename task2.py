
name = 'Anton Svir'
name1 = '_'.join(name)
name11 = name1.upper()

	
namelist = [ord(symbol) for symbol in name11]

name2 = name.lower()
namelist2 = [ord(symbol) for symbol in name2]

a = max(namelist)
b = max(namelist2)
c = max(a, b)

print(namelist)

print(namelist2)

print(c)
print(name11)