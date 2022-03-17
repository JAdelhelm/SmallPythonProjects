from collections import OrderedDict
import numpy as np
import random, time, re, os, sys
from IPython.display import clear_output
from pathlib import Path
import pyinputplus as pyip
capital=OrderedDict({
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
})
pathTest = f"{Path.cwd()}\\Test\\Test"
pathSolution = f"{Path.cwd()}\\Solution\\Solution"
pathStudent = f"{Path.cwd()}\\Student\\Solution_Student"

class test:
    def __init__(self, nrTasks=2):
        self.name = ""
        self.testNumber = ""
        self.nrTasks = nrTasks
    def createTests(self):
        if Path(f"{Path.cwd()}\\Test").is_dir() == False: Path(f"{Path.cwd()}\\Test").mkdir()
        if Path(f"{Path.cwd()}\\Solution").is_dir() == False: Path(f"{Path.cwd()}\\Solution").mkdir()
        if Path(f"{Path.cwd()}\\Student").is_dir() == False: Path(f"{Path.cwd()}\\Student").mkdir()

        for i in range(35):
            quizFile = open(f"{pathTest+str(i)}.txt","w")
            quizFile.write(f"This is a test from {self.name}\n\n")
            solFile = open(f"{pathSolution+str(i)}.txt","w")
            for i in range(50):
                # Lösung für die Antwort
                randomQuiz = random.randint(0,49)
                quizFile.write(f"Aufgabe {i} : Was ist der Bundestaat von {list(capital.items())[randomQuiz][0]}?\n")
                # Zufällige Antworten werden erstellt, die allerdings nicht die gleichen sind wie die richtige Lösung
                randChoices = [list(capital.items())[random.randint(0,49)][1] for val in range(0,3) if val != list(capital.items())[randomQuiz][0]]
                # Zufällige Antworten anhängen
                randChoices.append(list(capital.items())[randomQuiz][1])
                # Numpy Array konvertieren und shufflen
                npChoices = np.array(randChoices)
                np.random.shuffle(npChoices)
                # Reinschreiben
                quizFile.write(f"{npChoices}\n\n")
                # Lösungsbogen
                solFile.write(f"{i}:\n{list(capital.items())[randomQuiz][1]}\n\n")
            quizFile.close()
            solFile.close()
    def startName(self):    
        name = pyip.inputStr("Please enter your name:\n")
        self.name = name
        print(f"Hello {name}! Welcome to your Test!\n")
        time.sleep(1)
    def startTest(self):
        testNr = str(random.randint(0,34))
        self.testNumber = testNr
        # Einlesen des Tests
        test = open(pathTest+testNr+".txt")
        testText = test.read()
        test.close()

        solutions = open(pathSolution+testNr+".txt")

        fragenReg = re.compile(r"([A-Za-z\d:].*\w+\?)")
        antwortenReg = re.compile(r"(\'.*\')")
      
        w = open(pathStudent+testNr+".txt","w+")
        w.write("Name of the Student: "+self.name+"\n\n")
        w.close()
        for i in range(0,self.nrTasks):
            clear_output(wait=True)
            antworten_N = antwortenReg.findall(testText)[i]
            antworten_N = re.sub(r"\'\s",r",",antworten_N)
            antworten_N = re.sub(r"\'","",antworten_N)
            antworten_N = antworten_N.split(",")
            # Frage printen
            print(fragenReg.findall(testText)[i])
            try:
                antworten_N = list(set(antworten_N))
                checkS = pyip.inputMenu(choices=antworten_N, timeout=4, limit=2)
            except pyip.TimeoutException:
                checkS = ""
            except pyip.RetryLimitException:
                checkS = ""

            print(f"\nYour answer was: {checkS} \n")
            w = open(pathStudent+testNr+".txt","a")
            w.write(checkS+"\n")
            w.close()
    def validTest(self):
        stud_read_Object = open(pathStudent+self.testNumber+".txt","r")
        stud_right_read_object = open(pathSolution+self.testNumber+".txt")
        # Answers from Student
        studAnswers = stud_read_Object.readlines()[2:]
        studAnswers = list(map(lambda s: s.strip(),studAnswers))
        # Right Answers
        text_rightSolutions = stud_right_read_object.read()
        solReg = re.compile(r"[A-Za-z].*")
        cleanedR = solReg.findall(text_rightSolutions)
        # Check how much right answers
        correctAnswers = 0
        for answer in range(0,len(studAnswers)):
            if studAnswers[answer] == cleanedR[answer]:
                correctAnswers += 1
        print(f"{self.name} you have had {correctAnswers} correct answers out of {self.nrTasks}!")
        stud_right_read_object.close()
        stud_read_Object = open(pathStudent+self.testNumber+".txt","a")
        stud_read_Object.write(f"\n{correctAnswers} // {self.nrTasks} correct answers")
        stud_read_Object.close()
        
        
 
        
        


t = test(nrTasks=10)
t.createTests()
t.startName()
t.startTest()
t.validTest()
    