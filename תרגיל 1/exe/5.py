#rinat canaan 207744012

def tuplesToList(L):
    li=[]
    for i in L:
        if (isinstance(i,tuple)):#if this is tuple
            for j in i:#for every char
                li.append(j)#add to the new list
    return li

def tupleOfLists(L):
    tupe = []
    for i in L:
        if(isinstance(i,list)):#if this is list
            for j in i:#for every char
                tupe.append(j)#add to the new tuple
    return tuple(tupe)

def findObjectIn(i,L):
    for i in L:
        if isinstance(i, tuple) or isinstance(i, list):
            if object in i:
                  return True
    return False

def findStr(L):
    l=[]
    for i in L:
        if (isinstance(i,str)):
            if not findObjectIn(i, L):
                l.append(i)

    return l

def findNumbers(L):
    t = []
    for i in L:
       # if (isinstance(i, (float, int,complex))):
       if isinstance(i, int) or isinstance(i, float):
            if not findObjectIn(i, L):
                t.append(i)
    return tuple(t)


def printByType(l):#print all functions output
    print("Tuples in the list:\n", tuplesToList(l))
    print("Tuple of lists in the list:\n", tupleOfLists(l))
    print("Strings that are not in lists and tuples of the list:\n", findStr(l))
    print("Numbers that are not in lists and tuples of the list:\n", findNumbers(l))
    return




def main ():
    l = eval(input("enter your input in here:\n"))
    printByType(l)#this func will print according to the type of the output


if __name__ == "__main__":
    main()


"""

Enter your input:
[1,2,'a',(11,2,'b'),[22,'c'],(33,),['d'],'e']
Tuples in the list:
 [11, 2, 'b', 33]
Tuple of lists in the list:
 (22, 'c', 'd')
Strings that are not in lists and tuples of the list:
 ['a', 'e']
Numbers that are not in lists and tuples of the list:
 (1,)
 """