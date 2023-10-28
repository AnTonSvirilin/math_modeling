a = [4, 16, 10, 5, 7, 1, 8]
sslice = a[2:5:1]   #вырезаем кусок списка. начало, конец, шаг. нч, кн не вкл
print(sslice)

import numpy as np

a = [1, 5, 3, 6]
sslice = a[0:2:1]
print(sslice)


sllice = a[3:0:-1]    #6 3 5 
print(sllice)


slice = a[::-1]
print(slice)        #переворачивает список 


b = np.array([a, np.array(a)*3])
print(b)

slicce = b[::, 1]
print(slicce)

slicee = b[1,2:3:1]         # 2й массив между 2 и 3 с шагом 1 
print(slicee)

slllice = b[1,2::1]
print(slllice)