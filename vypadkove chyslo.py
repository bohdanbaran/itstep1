import random

def function():
    v = int(input('Vvedit naibilshe\n'))
    m = int(input('Vvedit naimenshe\n'))
    list_1 = list()
    list_1.append(m)
    a = m
    while a < v:
        a+=1
        list_1.append(a)
        print(list_1)
        r = random.choice(list_1)
        print(r)

function()
