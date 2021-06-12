
# My Attempt Doesnt work f(8,[1,4,5]) --> [1,1,1,5]
def bestSumCarlos(targetSum,numbers):
    if targetSum==0: return []
    if targetSum<0: return None
    numbers.sort(reverse=True) # O(Nlog(N))
    for num in numbers:
        remainder = targetSum-num
        res = bestSumCarlos(remainder,numbers)
        if res!=None:
            res.append(num)
            return res

    return None


# Brute Force + Memoziation
def bestSum(targetSum,numbers,memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum==0: return []
    if targetSum<0: return None
    
    shortestCombo = None
    for num in numbers:
        remainder = targetSum-num
        remainderCombo = bestSum(remainder,numbers,memo)
        
    
        if remainderCombo!=None:
            combo = remainderCombo+[num]

            if shortestCombo==None:
                shortestCombo = combo
            elif (len(combo)<len(shortestCombo)):
                shortestCombo = combo

    memo[targetSum] = shortestCombo
    return shortestCombo



print(bestSum(8,[1,4,5]))