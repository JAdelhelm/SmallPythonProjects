import operations
"""
A class of Calculators which has modules from the operations.py module that
includes arithmetic operations.
"""
class Calculator():
    def __init__(self):
        pass

    def describe(self):
        print("This is a native calculator that includes standard arithmetic operations.\n")

    def start(self):
        options = {
        1.0: "Total",
        2.0: "Substraction",
        3.0: "Multiple",
        "q": "Exit"
        }

        while True:
            try:
                print(options,"\n")
                quit = input("What option do you want to select?\n")
                auswahl = float(quit)


                for i in range(0,10):
                    if auswahl == 1:
                        print("Total: ",operations.sum(),"\n")
                        break
                    elif auswahl == 2:
                        print("Substraction: ",operations.minus(),"\n")
                        break
                    elif auswahl == 3:
                        print("Multiple: ",operations.multiple(),"\n")
                        break

            except IOError:
                print("Exit")
                break

            except ValueError:
                if quit == 'q':
                    break
                print("Wrong Input")
