
# Brute Force + Memozitaion
def allConstruct(target,wordBank):
    
    if target=="":
        return [[]]

    res = []
    for word in wordBank:
        if word in target and target.index(word)==0:
                sufix = target[len(word):len(target)]
                sufixWays = allConstruct(sufix,wordBank)
                targetways = [[word]+ways for ways in sufixWays]
                res+=targetways
    return res


print(allConstruct("carlos",["ca","r","los","rlos","l","os"]))

