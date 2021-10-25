class VerwalteterGeldbetrag:
    def __init__(self, anfangsbetrag):
        self.Betrag = anfangsbetrag
    def einzahlenMoeglich(self, betrag):
        return True

    def auszahlenMoeglich(self, betrag):
        return True

    def einzahlen(self, betrag):
            if betrag < 0 or not self.einzahlenMoeglich(betrag):
                return False
            else:
                self.Betrag += betrag
                return True

    def auszahlen(self, betrag):
        if betrag < 0 or not self.auszahlenMoeglich(betrag):
            return False
        else:
            self.Betrag -= betrag
            return True

    def zeige(self):
        print("Betrag: {:.2f}".format(self.Betrag))

class AllgemeinesKonto(VerwalteterGeldbetrag):
    def __init__(self, kundendaten, kontostand):
        super().__init__(kontostand)
        self.Kundendaten = kundendaten

    def geldtransfer(self, ziel, betrag):
        # Ruft die Methoden auszahlenmoeglich und einzahlenmoeglich auf und prüft ob der Betrag passt
        if self.auszahlenMoeglich(betrag) and ziel.einzahlenMoeglich(betrag):
            self.auszahlen(betrag)
            ziel.einzahlen(betrag)
            return True
        else:
            return False
        
    def zeige(self):
        self.Kundendaten.zeige()
        VerwalteterGeldbetrag.zeige(self)

class AllgemeinesKontoMitTagesUmsatz(AllgemeinesKonto):
    def __init__(self, kundendaten, kontostand, max_tagesumsatz=1500):
        # Erbt die Attribute vom Konstruktor des ALlgemeinenKontos
        super().__init__(kundendaten, kontostand)
        self.MaxTagesumsatz = max_tagesumsatz
        self.UmsatzHeute = 0.0
    def transferMoeglich(self, betrag):
        return (self.UmsatzHeute + betrag <= self.MaxTagesumsatz)
    def auszahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag)
    def einzahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag)
    def einzahlen(self, betrag):
        # Wenn True dann zahle Betrag ein
        if AllgemeinesKonto.einzahlen(self, betrag):
            self.UmsatzHeute += betrag
            return True
        else:
            return False
    def auszahlen(self, betrag):
        if AllgemeinesKonto.auszahlen(self, betrag):
            self.UmsatzHeute += betrag
            return True
        else:
            return False
    def zeige(self):
        AllgemeinesKonto.zeige(self)
        print("Heute schon {:.2f} von {:.2f} Euro umgesetzt".format(self.UmsatzHeute, self.MaxTagesumsatz))

class GirokontoKundendaten:
    def __init__(self,inhaber, kontonummer):
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer
    def zeige(self):
        print("Inhaber:", self.Inhaber)
        print("Kontonummer:",self.Kontonummer)

# Enthält alle Methoden der anderen Klassen
class GirokontoMitTagesumsatz(AllgemeinesKontoMitTagesUmsatz):
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=1500):
        kundendaten = GirokontoKundendaten(inhaber, kontonummer)
        super().__init__(kundendaten, kontostand, max_tagesumsatz)

k1 = GirokontoMitTagesumsatz("Heinz Ketchup", 563789, 12350)
k2 = GirokontoMitTagesumsatz("Klaus Kleber",45686, 15000)
# GirokontoMitTagesumsatz erbt von AllgemeinesKontoMitTagesUmsatz
# AllgemeinesKontoMitTagesUmsatz erbt von AllgemeinesKonto
# AllgemeinesKonto erbt von VerwalteterGeldbetrag

# k1.geldtransfer(k2, 160)
# k2.geldtransfer(k1,1000)
# k2.geldtransfer(k1, 500)
# k2.einzahlen(500)
# k1.zeige()
# k2.zeige()

