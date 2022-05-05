import pandas as pd
from os import path
import arff


def writeData(data1, data2):
    filename = "pacman.arff"
    if path.exists(filename):
        with open(filename, 'a') as arff_file:
            arff_file.write(data2)  # nextscore
            arff_file.write(data1)  # other data

    else:
        tickdata = []
        listdata = []
        data1_split = data1.split(",")
        data1_split.append(-1)
        for string in data1_split:
            listdata.append(int(string))
        #data2_split = data2.split(",")
        #listdata.append(data2)
        tickdata.append(listdata)
        print(tickdata)
        arff.dump(filename, tickdata, relation="pacmandata", names=[
            'NumOfTicks', 'PacmanX', 'PacmanY', 'PacmanDirection', 'NextAction',
            'Ghost1', 'Ghost2', 'Ghost3', 'Ghost4', 'PacDots', 'Score', 'NextScore'])

        #with open(filename, 'a') as arff_file:
        #    arff_file.write(data2)  # nextscore


#def writeData(information):
#    if not path.exists("tickdata.csv"):
#        column_names = ['PacmanX', 'PacmanY', 'PacmanDirection', 'NextAction', 'Ghost1', 'Ghost2', 'Ghost3', 'Ghost4', 'PacDots', 'Score']
#        df = pd.DataFrame(columns=column_names)
#        df.to_csv("tickdata.csv", index=False)
#    with open("tickdata.csv", "a") as csv_file:
#        csv_file.write(information)


def writeData(data1):
    filename = "pacman.arff"
    if path.exists(filename):
        with open(filename, 'a') as arff_file:
            arff_file.write(data1)  # other data

    else:
        tickdata = []
        listdata = []
        data1_split = data1.split(",")
        data1_split.append(-1)
        for string in data1_split:
            listdata.append(int(string))
        #data2_split = data2.split(",")
        #listdata.append(data2)
        tickdata.append(listdata)
        arff.dump(filename, tickdata, relation="pacmandata", names=[
            'NumOfTicks', 'PacmanX', 'PacmanY', 'PacmanDirection', 'NextAction',
            'Ghost1', 'Ghost2', 'Ghost3', 'Ghost4', 'PacDots', 'Score', 'NextScore'])

#def writeData(information):
#    if not path.exists("tickdata.csv"):
#        column_names = ['PacmanX', 'PacmanY', 'PacmanDirection', 'NextAction', 'Ghost1', 'Ghost2', 'Ghost3', 'Ghost4', 'PacDots', 'Score']
#        df = pd.DataFrame(columns=column_names)
#        df.to_csv("tickdata.csv", index=False)
#    with open("tickdata.csv", "a") as csv_file:
#        csv_file.write(information)
