#rinat canaan 207744012
#exercise 4 question 3 part 1

from functools import reduce


def sortedZip(L):
    def reqursive(L):
        if L == []:
            return []
        else:
            return [sorted(L[0])] + reqursive(L[1:])

    resList = reqursive(L)
    print(resList)

    return zip(*resList)


def main():
    L = eval(input("please enter a list of lists: "))
    print(list(sortedZip(L)))


if __name__ == "__main__":
    main()

# Output:
# please enter a list of lists: [[3,1,2],[5,6,4],['a','b','c']]
# [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]
# [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]
