# Списковые включения - listcomp - на выходе получаем список
# (хранит в себе все значения сразу):
symbols = 'Python'
symbol_codes = [ord(symbol) for symbol in symbols]
print(symbol_codes) # Список

# Генераторные выражения - genexp - на выходе получаем
# объект-генератор (вычисляет значения по порядку):
symbols = 'Snake'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes) # Объект-генератор

for object in symbol_codes:
    print(object) 