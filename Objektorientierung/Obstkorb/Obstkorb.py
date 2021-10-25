from Apfel import *
from Banane import *

class Obstkorb(Banane, Apfel):
    def __init__(self, groeße):
        # super().__init__() ruft den Konstruktor von Apfel, Banane etc. auf und dessen Attribute
        super().__init__()
        self.groeße = groeße
        self.inhalt = 0

    def einlagernMoeglich(self, anzahl):
         if anzahl + self.inhalt > self.groeße: return False
         else: return True

    def auslagernMoeglich(self, anzahl):
        if self.inhalt - anzahl < 0: return False
        else: return True

    def einlagern(self, anzahl):
        if anzahl + self.inhalt > self.groeße: return False
        else: self.inhalt += anzahl; return True
    
    def auslagern(self, anzahl):
        if self.inhalt - anzahl < 0: return False
        else: self.inhalt -= anzahl

    def zeigeInhalt(self):
        print(f"{self.inhalt} Obst im Obstkorb, davon")
        print(f"{super().apfelGetSet} Äpfel und {super().bananaGetSet} Bananen")


print("".center(60, "♥"))
obst1 = Obstkorb(100)
obst1.apfelEinlagern(4)
obst1.bananeEinlagern(20)
obst1.zeigeInhalt()
print()
print(" Esse alle Bananen auf bis auf 3 ".center(60, "♥"))
print()
obst1.bananaGetSet = 3
obst1.zeigeInhalt()
# obst1.apfelEinlagern(40)
