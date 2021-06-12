

# def gridTravkeler(m,n,memo={}):
#     if (m,n) in memo:
#         return memo[(m,n)]
#     elif n<1 or m<1:
#         return 0
#     elif n==1 and m==1:
#         return 1
#     else:
#         memo[(m,n)] = gridTravkeler(m-1,n,memo)+gridTravkeler(m,n-1,memo)
#         return memo[(m,n)]

def gridTraveler(m,n):
    table = [[0 for __ in range(n+1)] for _ in range(m+1)]
    table[1][1] = 1
    for row in range(m+1):
        for col in range(n+1):
            addToNeighbours(row,col,table)
    return table[m][n]

def addToNeighbours(row,col,table):
    if not row+1>len(table)-1:
        table[row+1][col]+=table[row][col]
    if not col+1>len(table[0])-1:
        table[row][col+1]+=table[row][col]


print(gridTraveler(3,3))