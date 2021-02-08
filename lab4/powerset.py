powerset = ()
sets = set([])
state = False
element = list(powerset)

while True:
    a = input('Enter one more element? [Y/N]: ')

    if a.capitalize() == "Y":
        state = True
    if a.capitalize() == "N":
        state = False
        break
    if state:
        x = input('Enter the new element in the set: ')
        element.append(x)

powerset = tuple(element)
for x in powerset:
    sets.add(x)

b = 0
c = 1
d = 0

while(b < len(powerset)):
    for x in powerset [c:len(powerset)]:
        temp = (powerset[d], x)
        sets.add(temp)

    b = b + 1
    c = c + 1
    d = d + 1

sets.add(powerset)

print(sets)
