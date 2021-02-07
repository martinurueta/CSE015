#x is the variable for the ten numbers in the list
x = [int(x) for x in input("Enter ten numbers and seperate them by spaces: ").split()]
#create a empty list for even and odd numbers
even_list = []
odd_list = []
#This loop will seperate the numbers in the list x to even and odd list
for i in x:
    if (i % 2 == 0):
        even_list.append(i)
    else:
        odd_list.append(i)
#If the odd list has numbers it will say to the user "No ODD Numbers" or else it will tell you the largest number value that is odd
if odd_list == []:
    print("No ODD Numbers were entered")    
else:
    y = max(odd_list)
    print("The Largest ODD number is: " + str(y))
    

    
