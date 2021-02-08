



# creates the domain
A = set(['dog','cat','fish','frog','pig','rabbit'])
# creates the codomain
B = set([1,2,3,4,5,6])



# creates the graph of a function
f = set([('dog',1),('cat',2),('frog',5),('fish',4),('pig',2),('rabbit',6)])



# prints domain and codomain as sets
print('Domain A')
print(A)
print('Codomain B')
print(B)



print('Graph of the function')
print(f)

for element in f:
    print(element)
    
for element in f:
    print(element[0])
    
    
for element in f:
    print(element[1])
    


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
    
def is_surjective(A,B,f):
        count = 0
        b = element
        for other in f:
            count += other.count(b)
        if count == 0:
            return False
        return True
def is_a_graph(A,B,f):
    for element in f:
        b = element[0]
        for other in f:
            if other != element:
                bprime = other[0]
                if b == bprime:
                    return False
        return True
    
print("f: A --> B")
check5 = is_a_graph(A,B,f)
if check5 == True:
    print('Function f is a graph')
else:
     print('Function f is not a graph')
     
check3 = is_surjective(A,B,f)
if check3 == True:
    print('Function f is surjective')
else:
     print('Function f is not surjective')

check1 = is_injective(A,B,f)
if check1 == True:
    print('Function f is injective')
else:
     print('Function f is not injective')

# change f to make it injective and surjective
f = set([('dog',1),('cat',2),('frog',5),('fish',4),('pig',3),('rabbit',6)])

check2 = is_injective(A,B,f)
if check2 == True:
    print('Function f is injective')
else:
    print('Function f is not injective')

f = set([('dog',1),('cat',2),('frog',5),('fish',4),('pig',3),('rabbit',6)])
check4 = is_surjective(A,B,f)
if check4 == True:
    print('Function f is surjective')
else:
     print('Function f is not surjective')
