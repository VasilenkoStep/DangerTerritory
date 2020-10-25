print("Введите число, которое создаст МОЩНЕЙШИЙ СПИСОК ")
n = int(input())
print("Введите неугодное вашей душе число")
neugodnoe_chislo = int(input())
a = []
for i in range(n + 1):
    a.append(i)
print("Получившийся список:" + " " + str(a))
a.remove(neugodnoe_chislo)
print("Получившийся список без этого убого числа:" + " " + str(a))
print ("Задание 3 выполнено :D")