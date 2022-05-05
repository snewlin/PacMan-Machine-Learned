from os import path
import arff

# export JAVA_HOME=$(/usr/libexec/java_home -v1.8)

i = 1  # global counter to keep track of total ticks

def writeData(data, action, nextscore):
    filename = "pacman.arff"
    global i
    if path.exists(filename):  
        with open(filename, 'a+') as arff_file:
            data_split = data.split(",")

            if len(data_split[0]) == 1 and data_split[0] == '2' and i == 1:  # second tick
                arff_file.write(data)
                arff_file.write("'{}'".format(action))
            else:
                # nextscore is added first on the previous line
                arff_file.write(nextscore)
                arff_file.write(data)
                arff_file.write("'{}'".format(action))
        i += 1

    else:  # first tick generated
        tickdata = []
        listdata = []
        data_split = data.split(",")  # make it a list of strings
        data_split.pop()
        for item in data_split:
            listdata.append(int(item))  # make the values numeric
        listdata.append(action)  # append action
        listdata.append(-1)  
        tickdata.append(listdata)
        arff.dump(filename, tickdata, relation="pacmandata", names=['NumOfTicks', 'PacmanX', 'PacmanY', 'Ghost1Dist', 'Ghost2Dist', 'Ghost3Dist', 'Ghost4Dist', 'Ghost1X',
                                                                    'Ghost1Y', 'Ghost2X', 'Ghost2Y', 'Ghost3X', 'Ghost3Y', 'Ghost4X', 'Ghost4Y', 'PacDots', 'Score', 'Action', 'NextScore'])


#def writeData(data1, action, data2):
#    if not path.exists("tickdata.csv"):
#        column_names = ['NumOfTicks', 'PacmanX', 'PacmanY', 'Ghost1Dist', 'Ghost2Dist',
#                        'Ghost3Dist', 'Ghost4Dist', 'Ghost1X', 'Ghost1Y', 'Ghost2X', 'Ghost2Y', 'Ghost3X', 'Ghost3Y', 'Ghost4X', 'Ghost4Y', 'PacDots', 'Score', 'Action', 'NextScore']
#        df = pd.DataFrame(columns=column_names)
#        df.to_csv("tickdata.csv", index=False)
#        with open("tickdata.csv", "a") as csv_file:
#            csv_file.write(data1)
#            csv_file.write(action)
#    with open("tickdata.csv", "a") as csv_file:
#        csv_file.write(data2)
#        csv_file.write(data1)
#        csv_file.write(action)
