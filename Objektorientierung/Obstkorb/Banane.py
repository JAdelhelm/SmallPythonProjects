class Banane():
    def __init__(self):
        self.bananenAnzahl = 0
        super().__init__()

    def bananeEinlagern(self, anzahl):
        if self.einlagernMoeglich(anzahl) == True: 
            self.bananenAnzahl += anzahl
            self.inhalt += anzahl
        else: print(f"Die Anzahl {anzahl} überschreitet die Größe des Obstkorbs"); return False

    def bananeAuslagern(self, anzahl):
        if self.auslagernMoeglich(anzahl) == True: 
            self.bananenAnzahl -= anzahl
            self.inhalt -= anzahl
        else: print("So viel kann nicht ausgelagert werden"); return False
    
    def getBanane(self):
        # print(f"Get {self.bananenAnzahl} Banana")
        return self.bananenAnzahl
    
    def setBananen(self,wert):
        # print(f"Set {wert} Banana")
        if wert > 0: self.inhalt -= self.bananenAnzahl-wert; self.bananenAnzahl = wert; 
        else: return self.bananenAnzahl

    bananaGetSet = property(getBanane, setBananen)