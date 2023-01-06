#Задача 2
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#Например. Для числа 30 список множителей 1-15, при этом простые из них (=делятся на 1 и сами на себя) 2,3,5

with open ('task_2.txt', 'r', encoding='UTF-8') as file:
    N=int(file.read())
    print (f'Простые множители числа {N} это числа ',end='')
    for i in range(2,N):
        if N%i==0:
            if i==2 or i==3 or i==5 or i==7:
                print(i,end=', ')
            elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
                print('',end='')
            else:
                print(i,end=', ')
   
   # if i!=2 and i!=3 and i!=5 and i!=7 and (i%2==0 or i%3==0 or i%5==0 or i%7==0):