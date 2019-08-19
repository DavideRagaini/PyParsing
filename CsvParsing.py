"""Questa funzione gli viene fornita una stringa e un separatore ed elimina dalla stringa tutti i separatori.
Ogni volta che incontra una occorrenza del separatore elimina dalla stringa tale occorrenza e la mette in un nuovo elemento di una lista.
Al termine restituisce una lista contenente la stringa meno i separatori."""
def NewList(s,sep=","):
    return s.split(sep)

def CheckErrorRows(nRowCount,lRows):
    if nRowCount is not (len(lRows)-1):
        print('errore: numero di colonne\n', nRowCount, '\t', len(lRows))

def CountRows(f):
    return f.count('\n')

def CountColumns(f):
    return (f[0].count(',') + 1)

def asdf(s):
    i = 0
    while i<=s.find('\n'):
        "print(s[i])"
        i = i+1
    return s.count(' ', 0, i)

def ListOfRows(s,sep='\n'):
    return s.split(sep)

file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')
s = file.read()

rows = CountRows(s)
l = NewList(s)

lRows = ListOfRows(s)
columns = CountColumns(lRows)

CheckErrorRows(rows,lRows)
print('rows = ', rows, '\tcolumns = ', columns)
file.close()
