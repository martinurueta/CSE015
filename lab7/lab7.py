def compute_f(n):
    if n == 0:
        return 2
    else:
        return compute_f(n-1)+2

n = int(input("Enter value for n: "))
answer = compute_f(n)
print("answer: ")
print(answer)

L = [4, 5, 9, 7, 7, 1, 9, 7, 2]
def count_instances(L, x):
    if L == []:
        return 0
    if L[0] == x:
        return 1 + count_instances(L[1:], x)
    else:
        return 0 + count_instances(L[1:], x)
print("Number of occurrences: ")
print(count_instances(L, 0))