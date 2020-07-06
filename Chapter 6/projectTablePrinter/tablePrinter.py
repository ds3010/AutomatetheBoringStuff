tableData = [['apples','orange', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = len(tableData[i][0])
        for j in range(1,len(tableData[i])):
            if len(tableData[i][j]) > len(tableData[i][j - 1]):
                colWidths[i] = len(tableData[i][j])
#    for x in range(len(colWidths)):
#       print(colWidths[x])

    for j in range(len(tableData[0])):
        print('')
        for i in range(len(colWidths)):
            print(' ' + tableData[i][j].rjust(colWidths[i]), end='')

printTable()