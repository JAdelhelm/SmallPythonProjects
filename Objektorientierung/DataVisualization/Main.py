from View import *
from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser()
    """Main class for argument parse in shell"""
    parser.add_argument("-f","--filepath",default="alice.txt",type=str)
    parser.add_argument("-c","--chart",default="pie", type=str)
    parser.add_argument("-w","--words",default=10, type=int)
    parser.add_argument("-n","--name",default=None, type=str)
    args = parser.parse_args()
    argumentFilepath = args.filepath
    argumentCharttype = args.chart
    argumentsWords = args.words
    argumentName = args.name

    v = View(argumentFilepath,argumentsWords)
    if args.chart == "pie":
        v.pieVisualize(name=args.name)
    elif args.chart == "graph":
        v.graphVisualize(name=args.name)
