#Rinat canaan 207744012

def tupleType(L):
    li = []
    count = 0
    for i in L:
        if (isinstance(i, tuple)):  # if this is tuple
                li.append(i)  # add to the new list
                count = count + 1
    return count

def listType(L):
    li = []
    count = 0
    for i in L:
        if (isinstance(i, list)):  # if this is list
                li.append(i)  # add to the new tuple
                count = count + 1
    return count

def  stringType(L):
    li = []
    count = 0
    for i in L:
        if (isinstance(i, str)):
                li.append(i)
                count = count + 1
    return count

def  floatType(L):
    li = []
    count = 0
    for i in L:
        if (isinstance(i, float)):
            li.append(i)
            count = count + 1
    return count

def  intType(L):
    li = []
    count = 0
    for i in L:
        if (isinstance(i, int)):
            li.append(i)
            count = count + 1
    return count


def main():
    L = eval(input("enter your input in here:\n"))
    tupleNum = tupleType(L)
    listNum = listType(L)
    stringNum = stringType(L)
    floatNum = floatType(L)
    intNum = intType(L)
    dic = {"list: ": listNum, "int: ": intNum, "float: ": floatNum, "string: ": stringNum, "tuple: ": tupleNum}
    print (dic)


if __name__ == "__main__":
    main()