import matplotlib.pyplot as plt
class Square():
    def __init__(self):
        pass

    def firsLineDiagram(self):
        # Shows the design styles of matplotlib
        print(plt.style.available)

        inputValues = [val for val in range(1,6)]
        squaredValues = [val**2 for val in range(1,6)]
        plt.style.use('ggplot')

        # Splits plots in figure and axes
        fig, ax  = plt.subplots()

        # Watch single points with scatter
        # to display a series of Points, you can insert a list of values
        ax.scatter([val for val in range(1,6)],[val**3 for val in range(1,6)], s=100, )

        # Insert Input- and Output data for correct display
        ax.plot(inputValues, squaredValues, linewidth=3)
        ax.set_xlabel("Values")
        ax.set_ylabel("Squared Values")
        ax.tick_params(axis='both',labelsize=14)
        ax.set_title("Square numbers",fontsize=24)
        plt.show()


wuerfel = Square()
wuerfel.firsLineDiagram()
