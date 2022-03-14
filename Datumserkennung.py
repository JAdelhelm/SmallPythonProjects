import re 
testFormat = "13/03/2021"

class datumerkennen:
    def __init__(self, text) -> None:
        self.text = text
    def getDay(self):
        regDay = re.compile(r"^[0-3]{1}[0-9]{1}")
        try: return regDay.search(self.text).group()
        except: print("No valid Dateformat"); raise Exception
    def getMonth(self):
        regMonth = re.compile(r"[0-1]{1}[1-12]{1}")
        try: return regMonth.search(self.text).group()
        except: print("No valid Dateformat"); raise Exception
    def getYear(self):
        regYear = re.compile(r"[1000-2999]{4}")
        try: return regYear.search(self.text).group()
        except: print("No valid Dateformat"); raise Exception
    def getDate(self):
        try: return f"{self.getDay()}.{self.getMonth()}.{self.getYear()}"
        except: print(); raise Exception





O1 = datumerkennen(testFormat)
print(O1.getDay())
print(O1.getMonth())
print(O1.getYear())
print(O1.getDate())