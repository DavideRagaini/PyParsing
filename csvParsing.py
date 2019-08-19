def NewList(s,sep=","):
    return s.split(sep)

def CheckErrorRows(nRowCount,lRows):
    if nRowCount is not (len(lRows)-1):
        print('errore: numero di colonne\n', nRowCount, '\t', len(lRows))

def CheckErrorColumns(lRows):
    i=0
    while (lRows[i].count(',') is not lRows[i+1].count(',')) and i>0 and i<max(len(lRows[i]),len(lRows[i])):
        print('riga ', i, 'e', i+1, 'sono diverse')

def CountRows(s):
    return s.count('\n')

def CountColumns(s):
    return (s[0].count(',') + 1)

def asdf(s):
    letters_counter = 0
    while letters_counter<=s.find('\n'):
        letters_counter = letters_counter+1
    return s.count(' ', 0, letters_counter)

def CreateListOfRows(s,sep='\n'):
    return s.split(sep)

def CreateTuple(file):
    sv = []
    for i in file:
        i = i.strip().split(',')
        sv.append(i)
    return sv

file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')
Tuple = CreateTuple(file)
file.close()

file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')
s = file.read()
nRows = CountRows(s)
l = NewList(s)
ListOfRows = CreateListOfRows(s)
nColumns = CountColumns(ListOfRows)
CheckErrorRows(nRows,ListOfRows)
CheckErrorColumns(ListOfRows)
print('rows = ', nRows, '\tcolumns = ', nColumns)
file.close()

file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')
k = file.readlines()
print(k is not l)
file.close()
