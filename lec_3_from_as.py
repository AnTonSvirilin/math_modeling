from lec_3_my_module import earth_mass as em
from lec_3_my_module import gravity_constant as G
from lec_3_my_module import sigma_steff_bolc as sigma

g = 500 * G / 10**2
print(g)

x = em * G * sigma
print(x)


# from lec_3_my_module import b
# from lec_3_import_as import b будкет взято второе б, тк в по очереди 
 
# print(b)
 
import lec_3_my_module as mm          #поэтому называем по-разному
import lec_3_import_as as l3
 
print(mm.b + l3.b)