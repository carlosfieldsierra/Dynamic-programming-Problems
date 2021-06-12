
# My recusive solution <-- wrong only uses each number once
def canSum(targetVal,lst):
    if targetVal==0:
        return True
    elif targetVal<0:
        return False
    elif len(lst)==0:
        return False
    else:
        for i  in range(len(lst)):
            val = lst.pop(i)
            if canSum(targetVal-val,lst):
                return True
            lst.insert(i,val)
    return False


# Brute force 
def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True
    for num in numbers:
        remainder = target_sum - num
        if remainder >= 0:
            if can_sum(remainder, numbers):
                return True
    return False

# Memoized
def can_sum_memo(target_sum, numbers,memo={}):
    if target_sum == 0:
        return True
    elif target_sum<0:
        return False
    elif target_sum in memo:
        return memo[target_sum]
    else:
        for num in numbers:
            remainder = target_sum - num
            memo[remainder] = can_sum_memo(remainder, numbers,memo)
            if memo[remainder]:
                return True
    return False

# Memoized Same thing sytanx differnt
def can_sum_memo1(target_sum, numbers,memo={}):
    if target_sum == 0:
        return True
    elif target_sum<0:
        return False
    elif target_sum in memo:
        return memo[target_sum]
    else:
        for num in numbers:
            remainder = target_sum - num
            if can_sum_memo1(remainder, numbers,memo):
                memo[remainder] = True
                return True
    memo[remainder] = False
    return False


print(can_sum_memo1(7,[5,3,4,7]))