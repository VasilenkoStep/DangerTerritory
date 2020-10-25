import random
n = [random.randint(-20,20) for _ in range(20)]
print (n)
sort_n = sorted(n)
below_zero = []
above_zero = []
for i in range(0,10):
    if sort_n[i]<0: 
        below_zero.append(sort_n[i])
    else:
        above_zero.append(sort_n[i])
sum_pozitive =sum(above_zero)/2
sum_negative =sum(below_zero)/2
print(above_zero)
print(below_zero)
print("Средне-арифметическое отрицательных чисел списка n : " + str(sum_negative))
print("Средне-арифметическое положительных чисел списка n : " + str(sum_pozitive))
print("Задание 8 выполнено :D")