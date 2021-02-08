



# creates the domain
A = set(['a','b','c','d'])
# creates the codomain
B = set([1,2,3,4,5,6])



# creates the graph of a function
f = set([('a',3),('b',4),('c',5),('d',1)])
g = set([('b',4),('a',3),('d',1),('c',5)])
h = set([(2,'bird'),(4,'cat'),(3,'dog'),(5,'fish')])
# This corresponds to the following function
# f(dog) = 1
# f(cat) = 1
# f(frog) = 5
# f(fish) = 4

# prints domain and codomain as sets
print('Domain A')
print(A)
print('Codomain B')
print(B)



# prints the graph of the function as a set
print('Graph of the function')
print('funtion f')
print(f)
print('funtion g')
print(g)
print('funtion h')
print(h)

    

def is_injective(A,B,f):
    """
    Determines if f is the graph of an injective function.
    We assume that f is a valid graph.

    Note: in this case parameters are not necessary and not even used. 
    However they are included for uniformity with the questions you have to 
    answer in the lab.
    Parameters
    ----------
    A: set
        A is the domain of the function
    B: set
        B is the codomain of the function
    f : set of tuples
        f is the graph of a function.

    Returns
    -------
    bool
        True if f is the graph of an injective function and False if it is not.

    """
    for element in f: # analyze all elements in the graph
        a = element[0] # first element in the tuple (not needed -- just for clarity)
        b = element[1] # second element: b = f(a)
        for other in f: # consider other elements in the graph
            if other != element: 
                bprime = other[1]  # Same as above
                if b == bprime: # if two elements have the same image, the function is not injective
                    return False
    # if this point is reached, all elements have been analyzed and it has not
    # found two elements with the same image; so the function is injective
    return True  
def equal_functions(f, g):
    print('function f:')
    print(f)
    print('function g:')
    print(g)
    print(' ')
    if f == g:
        return True
    else:
        return False
def is_partial_function(A, f):
    print('set A:')
    print(A)
    print('function f:')
    print(f)
    print(' ')

    count = 0
    b = len(A)
    for element in f:
        a = element[0]
    i = len(a)
    while count != i:
        count = count + 1

    if count < b:
        return True
def composite_function(f, h):
    j = set({})
    for element in f:
        for item in h:
            if element[1] == item[0]:
                j.add((element[0], item[1]))
    print('function f and h')
    print(f, h)
    print(' ')
    print('Composite function:')
    return j
print(composite_function(f, h))


check1 = equal_functions(f, g)
if check1 == True:
    print('egual funcions')
else:
    print('not equal function')
check2 = is_partial_function(A, f)
if check2 == True:
    print('partial function')
else:
    print('not partial function')
