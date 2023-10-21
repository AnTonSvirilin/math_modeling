print(bool(2))    #True

print(bool('Good'))  #True

print(bool([1, 4, 5]))   #True

print(bool(0))    #False

print(bool(''))   #False

print(bool([]))   #False

print(bool([[]]))  #True





if 1:
    print('hello 1')
  #hello 1


a = 3
if a > 1:
    print(f'hello {a}')

#hello 3


	
b = 5
if b == 5: # Операция сравнения,     = это присваевание, не путать 
    print(f'hello {b}')



	
a = 3
if a > 4:
    print('hello 4')
else:
    print(f'hello {a}')
    #hello 3





	
a = 3
if a > 5:
    print('hello 5')
elif a < 2:
    print('hello 2')
else:
    print('Tupo hello')
    #Tupo hello  



##############ЛОГИЧЕСКИЕ ОПЕРАЦИИ

a = 3
b = 4
c = 5
 
if a > 4 and b == 2: # and - операция логического "И"
    print('Good')
elif b > 3 or c == 5: # or - операция логического "ИЛИ"
    print('Best')
else:
    print('Bad')

    #Best 




############Конструкция цикла for


for i in 1, 3, 4:
    print(i**2, end=' ')
 #1 9 16

for i in 1, 3, 4:
    print(i**2, end='\n')
  #1
  #9
  #16

for i in 1, 3, 4:
    print(i, i**2, sep=' - ')
 #1 - 1
#3 - 9
#4 - 16

a = [1, 5, 7, 10]
for i in a:
    print(f'{i}**3 = {i**3}')

#1**3 = 1
#5**3 = 125
#7**3 = 343
#10**3 = 1000