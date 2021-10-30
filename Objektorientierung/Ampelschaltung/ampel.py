import enum
class Ampel(enum.Flag):
    Rot = enum.auto()
    Gelb = enum.auto()
    Gruen = enum.auto()
    Fußgaenger = enum.auto()


neueAmpel = Ampel(bool())

neueAmpel.Rot = True
if neueAmpel.Rot and neueAmpel.Fußgaenger: print("Fußgänger Tod")


neueAmpel.Rot = False
if neueAmpel.Rot and neueAmpel.Fußgaenger: print("Fußgänger Tod")
if not neueAmpel.Rot and neueAmpel.Fußgaenger: print("Fußgänger lebt")
