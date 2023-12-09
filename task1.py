import matplotlib.pyplot as plt

x = [1, 1]
y = [1, 5]
y1 = [5, 1]
y2 = [5, 5]
plt.plot(x, y, color='lightcoral', label='Graf 1', marker='o', ms=6)
plt.plot(y, x, color='lightcoral', label='Graf 2', marker='o', ms=6)
plt.plot(y2, y, color='lightcoral', label='Graf 3', marker='o', ms=6)
plt.plot(y, y2, color='lightcoral', label='Graf 4', marker='o', ms=6)
# --- Украшательства ---
plt.xlabel('Coord: x') # Подись оси ОХ
plt.ylabel('Coord: y') # Подпись оси ОУ
plt.title('square') # Общая подпись графика
plt.savefig('fig_5.png')