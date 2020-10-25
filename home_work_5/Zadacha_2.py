import random
print("Введите число, которое создаст МОЩНЕЙШИЙ СПИСОК ")
n = [random.randint(0,10) for _ in range(15)]
print ("Получившийся список:" + " "+ str(n))
while 0 in n:
    n.remove(0)
print(print ("Получившийся список без нулей:" + " "+ str(n)))
print ("Задание 2 выполнено :D")
