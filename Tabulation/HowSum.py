
# My Attempt
def howSum(targetSum,numbers):
    OuterLst = []
    howSumHelper(targetSum,numbers,[],OuterLst)
    return OuterLst

def howSumHelper(targetSum,numbers,InnerLst,OuterLst,memo={}):
    if targetSum==0:
        return True
    elif targetSum<0:
        return False
    elif targetSum in memo:
        InnerLst+=memo[targetSum]
        OuterLst.append(InnerLst)
    else:
        for num in numbers:
            remainder = targetSum-num
            InnerLst.append(num)
            if howSumHelper(remainder,numbers,InnerLst,OuterLst,memo):
                memo[remainder] = InnerLst
                OuterLst.append(InnerLst[:])
            InnerLst.pop(len(InnerLst)-1)



# Brute Froce + Memoziation
def howSumHis(targetSum,numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0: return []
    if targetSum<0: return None

    for num in numbers:
        remainder = targetSum-num
        res = howSumHis(remainder,numbers,memo)
        if res!=None:
            res.append(num)
            memo[targetSum]= res
            return memo[targetSum]

    memo[targetSum] = None
    return memo[targetSum]


print(howSumHis(8,[1,4,5]))