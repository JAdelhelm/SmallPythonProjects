"""Generatoren"""
def jungsnamen(maedels=False):
    yield "Jörg"
    yield "Dieter"
    yield "Otto"
    if maedels == True:
        print("Mädels:")
        yield "Anna"
        yield "Claudia"

for name in jungsnamen(maedels=True):
    pass
    # print(name)

"""Generator hoch 4"""
def hochVier(length=0):
    a = 1
    while a <= length:
        yield a*4
        a += 1

for i in hochVier(5):
    pass
    # print(i)

"""Fibonacci Generator
n = n-1 + n-2"""

def fibonacciGen(length=3):
    n1 = 0
    n2 = 1
    yield 0
    # Das Element davor wird zur Summe des Elements danach
    # Startwert ist die 0 und das Element danach die 1
    # 0+1, 1+1, 1+2, 2+3
    while n1-n2 <= length:
        # n1 = 0 ; n2 = 1
        yield n1 + n2 # 0 + 1
        n2 += n1 # Im ersten Durchlauf noch unrelevant da mit 0 addiert wird
        yield n1 + n2 # 0 + 1
        n1 += n2 # 1 + 1
    
for i in fibonacciGen(5):
    print(i)