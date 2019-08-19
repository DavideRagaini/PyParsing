from Final_csvParsing.py import CountRows
from Final_csvParsing.py import CountColumns
from Final_csvParsing.py import Newlist

file = open("dataset/Demographic_Statistics_By_Zip_Code.csv",'r')
s = file.read()
nRows = CountRows(s)
l = NewList(s)
nColumns = CountColumns(ListOfRows)
print('rows = ', nRows, '\tcolumns = ', nColumns)
file.close()

