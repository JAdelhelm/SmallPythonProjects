from Objekte import *

class VerwalteterBargeldbetrag(VerwalteterGeldbetrag):
    def __init__(self, bargeldbetrag):
        if bargeldbetrag < 0:
            # print("Betrag: ", bargeldbetrag)
            bargeldbetrag = 0
        # ruft den Konstruktor auf und übergibt bargeldbetrag dem Objekt
        super().__init__(bargeldbetrag)

    def auszahlenMoeglich(self, betrag):
        if betrag >= 0:
            # Betrag Geldbörse mindestens so hoch wie der Betrag der ausgezahlt werden soll
            # Attribut der Basisklasse "Betrag" vom VerwalteterGeldbetrag
            return (self.Betrag >= betrag)
    
class Geldboerse(VerwalteterBargeldbetrag):
    def __init__(self, bargeldbetrag):
        self.geldboerse = 0
        super().__init__(bargeldbetrag)

    def auszahlen(self, betrag):
        if (self.Betrag > betrag):
            self.geldboerse += betrag
            self.Betrag -= betrag

    def zeigeGeldBoerse(self):
        print("Aktueller Wert der Geldbörse: {:.2f}".format(self.geldboerse))
    
        

# Erzeugt eine Instanz, welche aus Geldboerse, VerwalteterBargeldbetrag und Verwalteterbetrag besteht
# Geldboerse enthält also Methoden der beiden Klassen sowie ihre Attribute
konto1 = Geldboerse(1000)
# zeige() der Klasse Verwalteter Geldbetrag
konto1.zeige()
konto1.auszahlen(200)
konto1.zeige()
konto1.zeigeGeldBoerse()
