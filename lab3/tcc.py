#download file logic.py
from logic import TruthTable
#create a user input for Quantifiers
logical = input("Enter Logical Expression:")
#plugin the input for truth table
myTable = TruthTable([logical])
#list in truth table
a = myTable.table
#number of item in list (rows)
b = len(a)
#display truth table of the user input
myTable.display()
myTable.latex()
# amount of truth of each row in the expression
true = 0
# a for loop to find every truth and false of each expression if true add one to the t for each row
for x in a:
    c = x[1][0]
    if (c == 1):
        true = true + 1
        
if(true == b):
    print ("This is Tautology")
elif(true == 0):
    print ("This is Contradiction")
else:
    print ("This is Contingency")
