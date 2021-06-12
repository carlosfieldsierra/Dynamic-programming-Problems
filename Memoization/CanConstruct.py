
# My First Try ---------------------------------
def canConstructCarlos(word,wordBank):
    return canConstructHelper(word,"",wordBank)

def canConstructHelper(word,makeWord,wordBank):
    if len(makeWord)>len(word): # Base Case
        return False

    if len(makeWord)==len(word):# Base Case
        if makeWord==word:
            return True
        return False

    elif sameWordUpTo(word,makeWord): # Recursive Case
        for addWord in wordBank:
            if canConstructHelper(word,makeWord+addWord,wordBank):
                return True

        return False
    else: # Base Case
        return False


def sameWordUpTo(word1,word2):
    return word1[0:len(word2)]==word2
# ---------------------------------


# Brute Force + Memozitaion
def canConstruct(target,wordBank,memo={}):
    if target in memo:
        return memo[target]
    if target=="":
        return True

    for word in wordBank:
        if word in target and target.index(word)==0:
                sufix = target[len(word):len(target)]
                memo[target]= canConstruct(sufix,wordBank,memo)
                if memo[target]:
                    return True

    memo[target] = False          
    return False



import time

start = time.time()
print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(time.time()-start)

start = time.time()
print(canConstructCarlos("abcdef",["ab","abc","cd","def","abcd"]))
print(time.time()-start)

