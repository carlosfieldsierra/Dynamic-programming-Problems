

def gridTravkeler(m,n,memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    elif n<1 or m<1:
        return 0
    elif n==1 and m==1:
        return 1
    else:
        memo[(m,n)] = gridTravkeler(m-1,n,memo)+gridTravkeler(m,n-1,memo)
        return memo[(m,n)]


print([str(gridTravkeler(i,i))[-1] for i in range(100)])