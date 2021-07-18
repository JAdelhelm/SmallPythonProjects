import matplotlib.pyplot as plt
class Square():
    def __init__(self):
        pass

    def firsLineDiagram(self):
        inputValues = [val for val in range(1,6)]
        squaredValues = [val**2 for val in range(1,6)]
        fig, ax  = plt.subplots()
        # Ein- und Ausgabedaten übergeben, damit die Visualisierung richtig ist
        ax.plot(inputValues, squaredValues, linewidth=3)
        ax.set_xlabel("Values")
        ax.set_ylabel("Squared Values")
        ax.tick_params(axis='both',labelsize=14)
        ax.set_title("Square numbers",fontsize=24)
        plt.show()


wuerfel = Square()
wuerfel.firsLineDiagram()
