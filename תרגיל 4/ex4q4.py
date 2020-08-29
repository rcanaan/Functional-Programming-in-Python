#rinat canaan 207744012
#exercise 4 question 4

import random

peopleNames = ("Iosi", "Ety", "Manchus", "mufasa", "simba", "scar")  # 1
verbs = ("sees", "plays", "sings", "loves", "eats", "sleep", "feels")  # 2                         #3
adjectives = ("tall", "big", "small", "hard", "red")  # 4                                          #4
adverbs = ("slowly", "tomorrow", "now", "soon", "suddenly")  # 3                                   #2
animateObjects = ("flowers", "oranges", "potatoes", "plates",)  # 5                               #5
inanimateObjects = ("a stone", "a chair", "a baloon", "a potato", "a plate")  # 1


def theHumbletPoet(N):
    myPoemTuple = crPoem(N)

    def theHumbletPoet(N, myPoemTuple):
        if N < 0:
            return
        else:
            print(myPoemTuple[N - 1])
            theHumbletPoet(N - 1, myPoemTuple)

    theHumbletPoet(N, myPoemTuple)


def crPoem(N):
    myPoemSentence = []
    PoemTuple = ()
    mtTempListToTuple = []

    ListOfTuples1 = [inanimateObjects, verbs, adverbs, adjectives, animateObjects]
    ListOfTuples2 = [peopleNames, verbs, adverbs, adjectives, animateObjects]

    def OneSentenceOfPoem():
        choiseOfSentene = random.randrange(1, 3)
        if choiseOfSentene == 1:
            myPoemSentence = [currTuple[random.randint(0, len(currTuple) - 1)] for currTuple in ListOfTuples1]

            # ---------------------------------------------------------------change!!!
            # for currTuple in ListOfTuples1:
            # randomChoise = random.randrange(len(currTuple))
            # myPoemSentence.append(currTuple[randomChoise])
            # ---------------------------------------------------------------change!!!


        elif choiseOfSentene == 2:
            myPoemSentence = [currTuple[random.randint(0, len(currTuple) - 1)] for currTuple in ListOfTuples2]

        # ---------------------------------------------------------------change!!!
        # for currTuple in ListOfTuples2:
        # randomChoise = random.randrange(len(currTuple))
        # myPoemSentence.append(currTuple[randomChoise])
        # ---------------------------------------------------------------change!!!

        MySentence = " ".join(myPoemSentence)
        return MySentence

    mtTempListToTuple = [OneSentenceOfPoem() for i in range(0, N)]
    return tuple(mtTempListToTuple)


def main():
    N = int(input("enter a number: "))
    theHumbletPoet(N)


if __name__ == "__main__":
    main()

# Output:
# enter a number: 3
# a baloon sings soon red oranges
# mufasa eats now red potatoes
# a plate plays now red plates
# a baloon sings soon red oranges
