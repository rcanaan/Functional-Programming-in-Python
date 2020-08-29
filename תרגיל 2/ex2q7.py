#Rinat Canaan 207744012
#exercise 2 question 7

#returns a list of prime numbers till N
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
    istwins = list(map(isTwin, primeList, primeList[2:]))  # to create the 1ist couple. sending the prime list as first variable, and as the second - the prime list from 2
    istwins2 = list(map(isTwin,primeList,primeList[1:]+[-1]))#for the rest of the numbers
    istwins.extend(istwins2)#using extend to dismantle  the form of the list -adding it as seperated numbers
    return dict(list(filter(lambda x: x != "none", istwins)))#the filter func filters with boolian func


def isTwin(a,b):
    if abs(a-b) == 2:
        return(a,b)
    else:
        return "none"


def main():
    N = abs(int(input(("enter a number: "))))
    twins = twinPrime(N)
    [print("prime number is : ", i, " its twin ", twins[i]) for i in twins.keys()]  # using list comprehension



"""
output:
enter a number: >? 11
prime number is :  1  its twin  3
prime number is :  3  its twin  5
prime number is :  5  its twin  7
main()
enter a number: >? 399
prime number is :  1  its twin  3
prime number is :  3  its twin  5
prime number is :  5  its twin  7
prime number is :  11  its twin  13
prime number is :  17  its twin  19
prime number is :  29  its twin  31
prime number is :  41  its twin  43
prime number is :  59  its twin  61
prime number is :  71  its twin  73
prime number is :  101  its twin  103
prime number is :  107  its twin  109
prime number is :  137  its twin  139  
    
    
"""