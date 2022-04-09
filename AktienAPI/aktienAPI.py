import json
import pandas as pd
import requests as r
import math
import re


millnames = ['',' Tausend',' Millionen',' Milliarden',' Trillionen']

class aktienAPI():
    def __init__(self, aktienKategorie="", APIKEY=""):
        self.aktienkategorie = aktienKategorie
        self.APIKEY = APIKEY
        self.headers = {'x-api-key': self.APIKEY }

    def banken(self):
        url = "https://yfapi.net/v6/finance/quote"
        # Banken Eintragen zum Analysieren
        querystring = {"symbols":"DBK.DE,CBK.DE"}

        response = r.request("GET", url, headers=self.headers, params=querystring)

        jsonBanken = json.loads(response.text)
        jsonBanken = jsonBanken["quoteResponse"]
        dfBanken = pd.DataFrame(jsonBanken["result"])

        self.printWerte(dfBanken)

    def millify(self,n):
        n = float(n)
        millidx = max(0,min(len(millnames)-1,
                            int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
        return '{:.2f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
      
    def trendUSTOP10(self):
        url_Symbols = "https://yfapi.net/v1/finance/trending/US"
        response_Trend_Symbols = r.request("GET", url_Symbols, headers=self.headers)
        jsonF = json.loads(response_Trend_Symbols.text)
        # Get symbols
        compileR = re.compile(r"[A-Z]{2,}")
        getSymbols = compileR.findall(str(jsonF))
        getSymbols = ",".join(getSymbols)
        queryTrends = {'symbols':str(getSymbols)}

        url_TotalRevenue = "https://yfapi.net/v11/finance/quoteSummary/DBK.DE?lang=en&region=US&modules=financialData%20"

        #Analyse symbols
        url_Analyse = "https://yfapi.net/v6/finance/quote"
        querystring = ",".join(compileR.findall(str(jsonF)))
        response_Analyse_trends = r.request("GET", url_Analyse, headers=self.headers, params=queryTrends)

        jsonTrends = json.loads(response_Analyse_trends.text)
        jsonTrends = jsonTrends["quoteResponse"]
        dfTrends = pd.DataFrame(jsonTrends["result"])

        self.printWerte(dfTrends)
    
    def printWerte(self,df):
        actualC = ""
        try:
            for val in range(len(df)):
                if df['currency'][val] == "EUR": actualC = "€"
                # Name
                print(f"{df['longName'][val]}".center(40,"_"))
                # Allgemeine Daten
                print(f"Marktkapital:           {self.millify(df['marketCap'][val])}")
                print(f"Aktienvolumen:          {self.millify(df['marketCap'][val]/df['regularMarketPrice'][val])}")
                print(f"Dividende:              {df['trailingAnnualDividendRate'][val]}",+15*" ", f"Angekündigt: {df['trailingAnnualDividendYield'][val]}")
                # Wert der Aktie
                print("Aktueller Wert: "+ "------->  " + " {:.2f}{}".format(df['regularMarketPrice'][val],actualC)+" <-- ")
                print(f"52 Wochen        Tief:"+ " {:.2f}{}".format(df['fiftyTwoWeekLow'][val],actualC)+" // Hoch: "+"{:.2f}{}".format(df['fiftyTwoWeekHigh'][val],actualC))
                print()
        except:
            print("Could not be printed")



apiStart = aktienAPI(APIKEY="Insert your API KEY")

# apiStart.banken()
apiStart.trendUSTOP10()
