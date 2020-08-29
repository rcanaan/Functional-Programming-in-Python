#rinat canaan 207744012
#exercise 4 question 3 part 3

def funczip(func, L):
    def reqursive(L):
        if L == []:
            return []
        else:
            return [func(L[0])] + reqursive(L[1:])

    resList = reqursive(L)
    return zip(*resList)


def main():
    L = eval(input("please enter a list of lists: "))

    # for example:
    print(list(funczip(sorted, L)))
    print(list(funczip(reversed, L)))


if __name__ == "__main__":
    main()

# Output:
# please enter a list of lists: [[3,1,2],[5,6,4],['a','b','c']]
# [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]
# [(2, 4, 'c'), (1, 6, 'b'), (3, 5, 'a')]
