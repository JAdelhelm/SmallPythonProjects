from gettext import gettext
import re
from pyparsing import Regex, pyparsing_unicode 
import pyperclip
defaultText = """Dieter: !@mydomain.net
Klaus: test+mysite@a.com
Bernd: address.test@example.com
Rolf: "test"@example.com
Rolando: multiple@domain.parts.com
Gerd: multiple@domain.parts.co.uk
Mark: ip@[IPv6:2002:DB8::1]
Leon: nodot@xx
"""

class telEmail:
    def __init__(self):
        self.text = ""
        self.mails = ""
        self.names = ""
    """Gets the text from copyboard"""
    def getText(self):
        try:
            self.text = pyperclip.paste()
            if len(self.text) < 2: 
                self.text = "".join(defaultText.splitlines())
                return self.text
            else: 
                self.text = " ".join(self.text.splitlines())
                return self.text
        except Exception: print("Text could not be pasted")
    """Get the valid mail adresses"""
    def getMails(self):
        try:
            regMails = re.compile(r'''(
                [a-zA-Z0-9.+]+
                [@]{1}
                [a-zA-Z0-9.+]+[\.]{1,4}\w+
            )''',re.VERBOSE)
            text = re.findall(regMails, self.getText())
            self.mails = text
            return self.mails

        except SyntaxError:
            print("No valid mail adress found")
    def getNames(self):
        try:
            regexNames = re.compile(r'''
            ([A-Z]\w+[a-z][:])
            ''', re.VERBOSE)
            names = re.findall(regexNames,self.getText())
            self.names = names
            return self.names
        except SyntaxError:
            print("No names found")
    def getNamesAndMails(self):
        regexNamesMails = re.compile(r'''(
        [A-Z]\w+[a-z][:]\s+
        [a-zA-Z0-9.+]+
        [@]{1}
        [a-zA-Z0-9.+]+[\.]{1,4}\w+
        )''',re.VERBOSE)
        namesAndMails = re.findall(regexNamesMails, self.getText())
        return namesAndMails
    """Print the different attributes"""
    def printText(self):
        print("Printed copyboard".center(40,"-"),"\n")
        print(self.text)
        print("\n","Printed copyboard".center(40,"-"),"\n")
    def printMails(self):
        print("Print all Mail addresses".center(40,"-"),"\n")
        print(self.mails)
        print("\n","Print all Mail adresses".center(40,"-"),"\n")
    def printNames(self):
        print("Print all Names".center(40,"-"),"\n")
        print(self.names)
        print("\n","Print all Names".center(40,"-"),"\n")
    def printMailsAndNames(self):
        print("Print Names and Mail adresses".center(40,"-"),"\n")
        print(self.getNamesAndMails())
        print("\n","Print Names and Mail adresses".center(40,"-"),"\n")            


        
O1 = telEmail()
# O1.printText()
# print(O1.getNames())
# print(O1.getMails())
O1.getMails()
O1.getNames()
O1.getNamesAndMails()
# O1.printMails()
# O1.printNames()
O1.printMailsAndNames()

