def NewList(s,sep=","):
    return s.split(sep)

def CountRows(s):
    return s.count('\n')

def CountColumns(s):
    return (s[0].count(',') + 1)

def CreateTuple(file):
    sv = []
    for i in file:
        i = i.strip().split(',')
        sv.append(i)
    return sv


"""
file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')
Tuple = CreateTuple(file)
file.close()

file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')
k = file.readlines()
file.close()

file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')

file.close()

file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')
s = file.read()
nRows = CountRows(s)
l = NewList(s)
nColumns = CountColumns(ListOfRows)
print('rows = ', nRows, '\tcolumns = ', nColumns)
file.close()"""
