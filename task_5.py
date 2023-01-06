#Задача 5
#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
#Пример. В одном файле многочлен: х**2+5х, во втором файле многочлен: x**3+2x**2+3. Сумма многочленов: x**3+3x**2+5x+3 

#считываем и создаем массив
with open ('task_5.1.txt','r',encoding='utf-8') as file1:
    text1=file1.read().split('+')
    print(text1)
mn_1=list(text1)
with open ('task_5.2.txt','r',encoding='utf-8') as file2:
    text2=file2.read().split('+')
    print(text2)
mn_2=list(text2)
#создаем массив **коэффициентов**
koeff_1=[]
for i in range (len(mn_1)):
    if 'x' in mn_1[i]:
        koeff_1.append(int(mn_1[i][0]))
    else:
        koeff_1.append(int(mn_1[i]))
koeff_2=[]
for i in range (len(mn_2)):
    if 'x' in mn_2[i]:
        koeff_2.append(int(mn_2[i][0]))
    else:
        koeff_2.append(int(mn_2[i]))
#создаем массив **степеней**
st_1=[]
for i in range (len(mn_1)):
    if 'x' in mn_1[i]:
        st_1.append(int(mn_1[i][-1]))
    else:
        st_1.append(int(0))
st_2=[]
for i in range (len(mn_2)):
    if 'x' in mn_2[i]:
        st_2.append(int(mn_2[i][-1]))
    else:
        st_2.append(int(0))
#Добавление пустых значений в списки **коэффициентов**
if len(koeff_1)>len(koeff_2):
    for i in range (len(koeff_1)-len(koeff_2)):
        koeff_2.insert(0,0)
else:
    for i in range (len(koeff_2)-len(koeff_1)):
        koeff_1.insert(0,0)
#Добавление пустых значений в списки **степеней**
if len(st_1)>len(st_2):
    for i in range (len(st_1)-len(st_2)):
        st_2.insert(0,0)
else:
    for i in range (len(st_2)-len(st_1)):
        st_1.insert(0,0)
# вывод суммы многочленов
summ=''
for i in range(len(koeff_1)):
    if st_1[0]!=0:
        if i<len(koeff_1)-1:
            summ=summ+f'{koeff_1[i]+koeff_2[i]}*x**{st_1[i]} + '
        if i==len(koeff_1)-1:
            summ=summ+f'{koeff_1[i]+koeff_2[i]}'
    else:
        if i<len(koeff_1)-1:
            summ=summ+f'{koeff_1[i]+koeff_2[i]}*x**{st_2[i]} + '
        if i==len(koeff_1)-1:
            summ=summ+f'{koeff_1[i]+koeff_2[i]}'
print(summ)
with open ('task_5_summa.txt', 'w', encoding='UTF-8') as file:
    file.write(summ)