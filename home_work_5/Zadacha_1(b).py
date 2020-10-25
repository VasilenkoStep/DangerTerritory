import random
n = [random.randint(0,20) for _ in range(15)]
print ("Получившийся список:" + " "+ str(n))
sort_n = sorted(n)
posledniy_element = sort_n[0]
print("Минимальное число:" + " " + str(posledniy_element))
while posledniy_element in n:
    n.remove(posledniy_element)
print ("Получившийся список:" + " "+ str(n))
print("Задание 1(б) выполнено :D")
