

def countConstructCarlos(target,wordBank):
    return countConstructHelper(target,"",wordBank)


def countConstructHelper(target,word,wordBank):
    if len(target)==len(word):
        if target==word:
            return 1
        return 0

    elif len(word)>len(target):
        return 0
        
    elif not sameWordUpTo(target,word):
        return 0
    else:
        val =0
        for addWord in wordBank:
            val+= countConstructHelper(target,word+addWord,wordBank)

        return val

def sameWordUpTo(word1,word2):
    return word1[0:len(word2)]==word2

# Brute Force + Memozitaion
def countConstruct(target,wordBank,memo={}):
    if target in memo:
        return memo[target]
    if target=="":
        return 1

    val =0
    for word in wordBank:
        if word in target and target.index(word)==0:
                sufix = target[len(word):len(target)]
                memo[target]= countConstruct(sufix,wordBank,memo)
                val+=memo[target]

    memo[target] = val        
    return val

print(countConstruct("carlos",["ca","r","los","rlos","l","os"]))
