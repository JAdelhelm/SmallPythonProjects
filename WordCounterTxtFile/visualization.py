import matplotlib.pyplot as plt
# This module is to visualize the Data


class visualizeData():
    def __init__(self,dataset):
        self.dataset = dataset
        print("Zeige", self.dataset)
        self.plot_set()

    def plot_set(self):
        # Zeigt die Styles an die zur Verfügung stehen
        plt.style.available
        fig, ax = plt.subplots()
        # Ein- und Ausgabewerte übergeben
        # print(sorted(wCount.words[:50], key=wCount.words.count, reverse=False))

        # Calls Object wCounter == Dataset, then attribute of wCounter words
        ax.plot(sorted(self.dataset.words[:50], key=self.dataset.words.count, reverse=False), linewidth=3)
        ax.set_title("Most 50 frequent words")
        ax.set_ylabel("Words")
        ax.set_xlabel("Frequence")
        # Schriftgröße der Achsen des Diagramms
        ax.tick_params(axis='both',labelsize=8)
        plt.show()


# newTestData = [val*2 for val in range(0,20)]
# visualizeData(newTestData)
