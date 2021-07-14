import matplotlib.pyplot as plt
class Square():
    def __init__(self):
        pass

    def firsLineDiagram(self):
        squares = [val**2 for val in range(1,6)]
        fig, ax  = plt.subplots()
        ax.plot(squares, linewidth=3)
        ax.set_title("Square numbers",fontsize=24)
        plt.show()


wuerfel = Square()
wuerfel.firsLineDiagram()
