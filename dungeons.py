import random

#1d4
def tirage(stat):

    a = random.randint(1,4)
    b = random.randint(1,4)
    c = random.randint(1,4)
    d = random.randint(1,4)

    liste =[a, b, c, d]
    liste.sort()
    del liste[0]
    return sum(liste)

list_stat = ["con", tirage(i)]
print(list_stat())
