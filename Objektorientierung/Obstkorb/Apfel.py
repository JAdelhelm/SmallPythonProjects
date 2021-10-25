class Apfel():
    def __init__(self):
        self.apfelAnzahl = 0
        super().__init__()
    
    def apfelEinlagern(self, anzahl):
        if self.einlagernMoeglich(anzahl) == True:
            self.apfelAnzahl += anzahl
            self.inhalt += anzahl
        else: print(f"Die Anzahl {anzahl} überschreitet die Größe des Obstkorbs"); return False
    
    def apfelAuslagern(self, anzahl):
        if self.auslagernMoeglich(anzahl) == True:
            self.apfelAnzahl -= anzahl
            self.inhalt -= anzahl
        else: print("So viel kann nicht ausgelagert werden"); return False

    def getApfel(self):
        # print(f"Get {self.apfelAnzahl} Apfel")
        return self.apfelAnzahl
    
    def setApfel(self,wert):
        # print(f"Set {wert} Apfel")
        if wert > 0: self.inhalt -= self.apfelAnzahl-wert; self.apfelAnzahl = wert; 
        else: return self.apfelAnzahl

    apfelGetSet = property(getApfel, setApfel)