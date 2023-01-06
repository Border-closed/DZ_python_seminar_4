#Задача 4
#НЕОБЯЗАТЕЛЬНАЯ Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:- k=2 => 2*x² + 4*x + 5 = 0 или k=3 => 4*x3 + 2*x² + 4*x + 5 = 0

k=int(input('Задайте натуральную степень '))
koeff=[] #Генерация коэффициентов уравнения
import random
for i in range (k+1):
    koeff.append(int(random.uniform(1,10)))
# print(koeff)
stepen=[] #Создание списка со степенями и сортировка их в обратном порядке
for i in range (1,k+1):
    stepen.append(i)
# print(stepen)
stepen.sort(reverse=True)
# print(stepen)
uravnenie=''
for i in range(len(koeff)): #Вывод уравнения на экран
    if i<len(koeff)-1:
        print(f'{koeff[i]}*x**{stepen[i]} + ',end='')
        uravnenie=uravnenie+f'{koeff[i]}*x**{stepen[i]} + '
    else:
        print(f'{koeff[i]} = 0')
        uravnenie=uravnenie+f'{koeff[i]} = 0'
with open ('task_4_uravnenie.txt', 'w', encoding='UTF-8') as file:
    file.write(uravnenie)