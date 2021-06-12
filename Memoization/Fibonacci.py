# Write a function that returns the n-th number of the Fibonacci sequence


# Recursive Fib 
def fibRecursive(n): # O(2^N)
    if n<=2:
        return 1
    return fibR(n-1) + fibR(n-2)


# My attempt at dynamic Fib
def fibDynamic(n): # O(N)
    lst = [1]*n
    for i in range(2,n):
        lst[i] =lst[i-1]+lst[i-2]
    return lst[n-1]

# Memoization
def fibMemoization(n,memo={}): # O(N)
    if n in memo: return memo[n]
    if n<2: return 1
    memo[n]=fibMemoization(n-1,memo)+fibMemoization(n-2,memo)    
    return memo[n]

print(fibMemoization(50))