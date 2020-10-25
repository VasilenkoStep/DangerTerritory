import random
A = int(input("Введите отрицательное число от -10 до -1"))
n = [i for i in range(-10,10)]
print (n)
a = n.index(A) 
b = 0
i = 0
while i <= len(n[a:11]):
    b = b + n[a+1]
    a+=1
    i+=1
print ("Cумма отрицательных чисел больше"+ " " + str(A) + ":" + " " + str(b))
print ("Длина отрицательных чисел больше"+ " " + str(A) + ":" + " " + str(len(n[c:9])))
print("Задание 7 выполнено :D")