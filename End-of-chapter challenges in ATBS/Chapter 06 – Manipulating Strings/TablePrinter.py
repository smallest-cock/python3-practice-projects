tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['cock', 'dick', 'pp', 'penis']]


def printTable(tableList):
    maxCharLength = {}
    for list in range(len(tableList)):
        maxCharLength.setdefault('column ' + str(list), 1)
    for i in range(len(tableList[0])):
        for list in range(len(tableList)):
            if len(tableList[list][i]) > len(tableList[list][i - 1]):
                maxCharLength['column ' + str(list)] = len(tableList[list][i])
    for i in range(len(tableList[0])):
        for list in range(len(tableList)):
            print(tableList[list][i].rjust(maxCharLength['column ' + str(list)]), end= "".join(" "))
        print(" ")

printTable(tableData)

