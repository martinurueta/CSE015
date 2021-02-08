from logic import TruthTable
t = 0
userinput = input('write your quantifer: ')
myTable = TruthTable([userinput])
a = myTable.table
myTable.display()
print (a)
p = len(a)
print('row equals: ' + str(p))
for i in a:
    c = i[1][0]
    print (c)
    if (c == 1):
        t = t + 1
print ('number equals : ' + str(t))

if (t == p):
    print ("Tautology")
elif(t == 0):
    print ("Contradiction")
else:
    print ("Contingency")
