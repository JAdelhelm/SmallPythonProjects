class Quadrat():
    def __init__(self, zahl):
        self.zahl = zahl

    def __str__(self):
        return str(self.zahl)

    """other ist wie ein Objekt und löst dann quasi das "self" ab"""
    def __add__(self, other):
        z = self.zahl*self.zahl
        y = other.zahl * other.zahl
        x = z+y
        return Quadrat(x)


# Objekte müssen zuerst erstellt werden
a1 = Quadrat(4)
a2 = Quadrat(3)
print(a1+a2)