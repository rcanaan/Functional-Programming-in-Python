#Rinat Canaan 207744012
#Exercise 3 question 7

#eratosthenes func - returns a list of prime numbers till N
def napa(N):
    rishoni = [True]*N
    rishoni[0] = False

    for i in range (2,N):
        if rishoni[i]:
            for mlt in range(i*2,N,i):
                rishoni[mlt] = False

    res = []
    for i,item in enumerate(rishoni):
        if item:
            res.append(i)
    return res


def twinPrime(N):
    primeList = napa(N+1)
    def helpFunc(result, i, primeList):
        if len(primeList) == 1:
            return result
        else:
            if isTwin(primeList[i], primeList[i+1]) != "none":
                result[primeList[i]] = primeList[i+1]
                return helpFunc(result, 0, primeList[1:])
            else:
                return helpFunc(result, 0, primeList[1:])
    return helpFunc({}, 0, primeList)#result = {}



def isTwin(a,b):
    if abs(a-b) == 2:
        return(a,b)
    else:
        return "none"

#def printFunc(twins):
 #   if len(twins) == 0:
  #      return ""
  #  else:
   #     print(twins[0]+1)
    #    return printFunc(twins[1:])

def main():
    N = abs(int(input(("enter a number: "))))
    twins = twinPrime(N)
    [print("prime number is : ", i, " its twin ", twins[i]) for i in twins.keys()]  # using list comprehension

