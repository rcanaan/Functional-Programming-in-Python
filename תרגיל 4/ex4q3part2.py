#rinat canaan 207744012
#exercise 4 question 3 part 2

def sortedZip(L):
    def reqursive(L):
        if L == []:
            return []
        else:
            return [reversed(L[0])] + reqursive(L[1:])

    resList = reqursive(L)
    return zip(*resList)


def main():
    L = eval(input("please enter a list of lists: "))
    print(list(sortedZip(L)))


if __name__ == "__main__":
    main()

# Output:
# please enter a list of lists: [[3,1,2],[5,6,4],['a','b','c']]
# [(2, 4, 'c'), (1, 6, 'b'), (3, 5, 'a')]

