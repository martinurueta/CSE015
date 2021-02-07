from logic import TruthTable
myTable = TruthTable(['a','b'], ['a and -b'])
myTable.display()
myTable.latex()
myTable2 = TruthTable(['a','b','c'], ['(a and b) or -c'])
myTable2.display()
myTable2.latex()
