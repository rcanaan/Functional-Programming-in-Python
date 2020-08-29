#rinat canaan 207744012
#exercise 4 question 2

def treateline(lineNr, line):
    ln = line.split()

    def rec(w, result):
        if w == False:  # basic situation
            return -1
        if w == []:  # basic situation
            return 1
        else:  # recursion tail call
            return rec(w[1:], result and isword(w))

    if rec(ln, True) == -1:
        return -1
    else:  # to continue from here
        ls = tuple([func(i) for i in ln])
        return dict(zip(ln, ls))


def isword(wrd):  # returns true if all the letters in the word are letters
    return all(i.isalpha() for i in wrd)


# checka and return what type of letter it is
def whatLetter(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return -1
    if ord(letter) >= 98 and ord(letter) <= 109:
        return 0
    else:
        return 1


def func(wrd):
    lst = list(wrd)

    def rec(w, result1, result2, result3):
        if w == []:  # basic situation
            return (result1, result2, result3)
        elif whatLetter(w[0]) == -1:  # general sitauation
            return rec(w[1:], result1 + [w[0]], result2, result3)
        elif whatLetter(w[0]) == 0:  # general sitauation
            return rec(w[1:], result1, result2 + [w[0]], result3)
        else:  # recursion tail call
            return rec(w[1:], result1, result2, result3 + [w[0]])

    return rec(lst, [], [], [])


def treatexfile(flname):
    name = flname + ".txt"
    file = open(name, "r")
    count = len(file.readlines())
    file.close()
    file = open(name, "r")
    l = []
    l = [list(treateline(i, file.readline()).values()) for i in range(1, count + 1)]
    """
    for i in range(1,count+1):
        string=file.readline()
        l=l+[list(treateline(i, string).values())]
        """
    file.close()
    ls = list(range(1, count + 1))
    return dict(zip(ls, l))


def func2(l):
    return ([len(l[0])], [len(l[1])], [len(l[2])])


"""
def func3(l):
    def rec(l, i, r1, r2, r3):
        if l==[]:
            return (r1, r2, r3)
        if isinstance(l[0], list):
            return rec(l[1:], i, r1, r2, r3)
        else:
            return rec(l[1:], i+1, r1+len(l[i][0]), r2+len(l[i][1]), r3+len(l[i][0]))
    return rec(l, 0 , 0, 0, 0)
"""


def func4(l):
    def rec(l, r1, r2, r3):
        if l == []:  # basic situation
            return (r1, r2, r3)
        else:  # we take the l[0] and we go in the tuple in each list and take that value, #recursion tail call
            return rec(l[1:], r1 + l[0][0][0], r2 + l[0][1][0], r3 + l[0][2][0])

    return rec(l, 0, 0, 0)


def sikumofayim(fldict):
    ls = list(fldict.keys())
    l = list(fldict.values())

    def rec(l):
        if l == []:  # basic situation
            return []
        if isinstance(l[0], list):  # general sitauation
            return [rec(l[0])] + rec(l[1:])
        if isinstance(l[0], tuple):  # general sitauation
            return [(func2(l[0]))] + rec(l[1:])
        else:  # recursion tail call
            return rec(l[1:])

    lt = rec(l)
    lw = [tuple(func4(i)) for i in lt]
    return dict(zip(ls, lw))


def printFunc(i, val):
    print(f"   {i}            {val[0]}                 {val[1]}                      {val[2]}")


def main():
    name = str(input("Enter a file's name: "))
    print("LineNr    nr of vowels    nr of b-m consonants    nr of n-z consonants")
    dic = sikumofayim(treatexfile(name))
    [printFunc(i, val) for i, val in dic.items()]
    print("Nr of Lines in text    total nr of vowels     total nr of b-m consonants     total nr of n-z consonants")

    def rec(dic, r1, r2, r3, number):
        if dic == []:  # basic situation
            return [r1, r2, r3, number]
        else:  # recursion tail call
            return rec(dic[1:], r1 + dic[0][0], r2 + dic[0][1], r3 + dic[0][2], number + 1)

    lw = rec(list(dic.values()), 0, 0, 0, 0)
    print(
        f"        {lw[3]}                      {lw[0]}                        {lw[1]}                              {lw[2]}")


if __name__ == "__main__":
    main()

