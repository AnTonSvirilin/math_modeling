	
import numpy as np
 
a = np.zeros((2, 3))  #два массива по 3 эл-та(0)
print(a)
 
 	
a[0, 2] = 5     #изменение 3 элемента 1го массиыва 
print(a)

b = np.ones((3, 2))
print(b)


d = np.ndarray((3, 3))     #массив из ничего(минус бесконечности)
print(d)
