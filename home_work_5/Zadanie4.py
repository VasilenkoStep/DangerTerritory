import random
n = [random.randint(0,20) for _ in range(15)]
print("Введите сколько угодно чисел, вообще без разницы, все вставлю! Но только через пробел")
print ("Изначальный список:" + " "+ str(n))
b = input()
split = b.split()
numbers = map(int,split)
numbers = list(numbers)
k = 2
for i in numbers:
    n.insert(k,i)
    k=k+1      
print("Получившийся список n:" + " " + str(n))
print("Задание 4 выполнено :D")