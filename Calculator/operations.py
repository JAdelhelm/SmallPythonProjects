
def sum():
    while True:
        try:
            totalResult = float(input("First Value:\n"))
            values = int(input("How many values do you want to sum?\n"))
            liste = [int(input("Value to sum: ")) for val in range(values) if str(val).isnumeric() == True]

            for value in liste:
                totalResult += value
            return totalResult

        except ValueError:
            print("Input is no value\n")
            if input("Write 'q' to Exit\n") == 'q':
                break

def minus():
    while True:
        try:
            minResult = float(input("First Value:\n"))
            values = int(input("How many values do you want to substract?\n"))
            liste = [int(input("Value to substract: ")) for val in range(values) if str(val).isnumeric() == True]

            for value in liste:
                minResult -= value
            return minResult

        except ValueError:
            print("Input is no value\n")
            if input("Write 'q' to Exit\n") == 'q':
                break

def multiple():
    while True:
        try:
            mulResult = float(input("First Value:\n"))
            values = int(input("How many values do you want to multiply?\n"))
            liste = [int(input("Value to multiply: ")) for val in range(values) if str(val).isnumeric() == True]

            for value in liste:
                mulResult *= value
            return mulResult

        except ValueError:
            print("Input is no value\n")
            if input("Write 'q' to Exit\n") == 'q':
                break
