import random
n = [random.randint(0,20) for _ in range(15)]
print ("Получившийся список:" + " "+ str(n))
copy_n = n.copy()
for _ in range(len(n)):
    for i in range(0, len(n)-1):
        a = n[i]
        b = n[i+1]
        if a>b:
            n[i] , n[i+1] = b , a
foxy = copy_n.index(n[-1])
copy_n = copy_n[:foxy]
print ("Числа стоящие до 1-го! максимального элемента массива:" + " " + str(copy_n))
print("Задание 6 выполнено :D ")