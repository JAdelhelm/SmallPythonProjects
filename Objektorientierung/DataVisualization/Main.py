from View import *
from argparse import ArgumentParser
if __name__ == "__main__":
    """Main class for argument parse in shell
    Go to the python script directory, use follow syntax: python Main.py ...Arguments
    Use -f to declare the filepath
    Use -c to declare the chart type
    Use -w to declare the number of words you want to analyze
    Use -n to delcare the name of the creator
    Use -s to declare the path to save the image of the visualization"""
    parser = ArgumentParser()
    parser.add_argument("-f","--filepath",default="alice.txt",type=str)
    parser.add_argument("-c","--chart",default="pie", type=str)
    parser.add_argument("-w","--words",default=10, type=int)
    parser.add_argument("-n","--name",default=None, type=str)
    parser.add_argument("-s","--save",default=None,type=str)
    args = parser.parse_args()
    argumentFilepath = args.filepath
    argumentCharttype = args.chart
    argumentsWords = args.words
    argumentName = args.name
    argumentSaveName = args.save

    if args.filepath.endswith(".txt"):
        v = View(argumentFilepath,argumentsWords)
        if args.chart == "pie":
            v.pieVisualize(name=args.name, output=argumentSaveName)
        elif args.chart == "graph":
            v.graphVisualize(name=args.name, output=argumentSaveName)
    elif args.filepath.endswith(".pdf"):
        print("Please convert your document in a textfile")
    else:
        print("Wrong filepath")
