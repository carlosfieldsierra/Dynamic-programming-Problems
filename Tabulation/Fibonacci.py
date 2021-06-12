# Write a function that returns the n-th number of the Fibonacci sequence

# My solution
def fibCarlos(n):
    lst = [1]*(n+1)
    for i in range(3,n+1):
        lst[i] = lst[i-2]+lst[i-1]
    return lst[n]


# Tabulation
def fib(n):
    table = [0]*(n+1)
    table[1] = 1
    for i in range(n-1):
        table[i+1]+=table[i]
        table[i+2]+= table[i]
    table[-1] += table[-2]
    return table[-1]


print([fib(i) for i in range(1,10)])
print([fibCarlos(i) for i in range(1,10)])