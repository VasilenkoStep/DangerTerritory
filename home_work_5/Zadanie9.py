import random
n = [random.randint(-20,20) for _ in range(20)]
print(n)
sort_n = sorted(n)
below_zero = []
above_zero = []
for i in range(0,20):
    if sort_n[i]<0: 
        below_zero.append(sort_n[i])
    else:
        above_zero.append(sort_n[i])
print("Максимальное число :" + " " + str(above_zero[-1]))
print("Минимальное число :" + " " + str(below_zero[0]))
Min = n.index(below_zero[0]) 
Max = n.index(above_zero[-1])
k , j =1,1
if Max > Min+1:
    while k <=len(n[Min:Max])-1:
        n[Min+k]="Fox"
        k+=1
    while "Fox" in n:
        n.remove("Fox")
    print(n)
elif Min > Max+1:
    while j <=len(n[Max:Min])-1:
        n[Max+j]="Fox"
        j+=1
    while "Fox" in n:
        n.remove("Fox")
    print(n)
else:
    print("Между Max и Min значениями к счастью нету чисел ^_^ нету чисел")  
print("Задание 9 выполнено :D")