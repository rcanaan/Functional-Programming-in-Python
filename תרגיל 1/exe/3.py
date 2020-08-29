#Rinat Canaan 207744012

def IsANum(num):
    try:
        if type(num) == list:
            return False

        num2 = int(num)
        return True
    except ValueError:
        try:
            num2 = float(num)
            return True
        except ValueError:
            return False


# function for section b part 2 of question 3=> first version
def FindTwoMiddlesVer1(x, y, z, w):
    a = int(x)
    b = int(y)
    c = int(z)
    d = int(w)
    l1 = [a, b, c, d]
    l2 = sorted(l1)
    # l3 = [l2[1], l2[2]]

    print(l2)
    return l2[1], l2[2]  # l3


# function for section b part 2 of question 3=> second version
def FindTwoMiddlesVer2(l):
    l2 = [0, 0]

    for num1 in l:
        count = 0
        for num2 in l:
            if num2 < num1:
                count = count + 1
        if count == 1:
            l2[0] = num1
        elif count == 2:
            l2[1] = num1

    return l2


# function for section b part 3 of question 3
def printMiddleNums(l):
    print("first middle number: " + str(l[0]))
    print("second middle number: " + str(l[1]))


# function for section c part 2 of question 3 version 1
def findMiddlesInListWithSort(l):
    l = sorted(l)
    length = len(l)

    if length <= 2:
        return l
    if length:
        return l[int(length / 2)], l[int(length / 2) + 1]
    else:
        return "ERROR"


# function for section c part 2 of question 3 vertion 2
def findMiddlesInListWithoutSort(l):
    n = len(l)
    # Traverse through all list elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the list from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return l[int(n / 2)], l[int(n / 2) + 1]


def main():
    # checking the first number
    firstNum = input("Enter the first number: ")
    if IsANum(firstNum) == True:
        print("Input is a number. Number = ", firstNum)
    else:
        print("No.. input is not a number. It's a string")

    # checking the second number
    secNum = input("Enter the second number: ")
    if IsANum(secNum) == True:
        print("Input is a number. Number = ", secNum)
    else:
        print("No.. input is not a number. It's a string")

    # checking the third number
    thirdNum = input("Enter the third number: ")
    if IsANum(thirdNum) == True:
        print("Input is a number. Number = ", thirdNum)
    else:
        print("No.. input is not a number. It's a string")

    # checking the fourth number
    fourthdNum = input("Enter the fourth number: ")
    if IsANum(fourthdNum) == True:
        print("Input is a number. Number = ", fourthdNum)
    else:
        print("No.. input is not a number. It's a string")

    a = int(firstNum)
    b = int(secNum)
    c = int(thirdNum)
    d = int(fourthdNum)
    l = [a, b, c, d]

    printMiddleNums(FindTwoMiddlesVer1(firstNum, secNum, thirdNum, fourthdNum))

    printMiddleNums(FindTwoMiddlesVer2(l))

    # for section c part 1 in question 3
    print("--------------------------------------")
    print("write 'stop' to stop adding into list")
    i = input("Enter a value please: ")
    listt = []

    while i != "stop":
        if IsANum(i):
            listt.append(i)
        i = input("Enter a value please: ")

    printMiddleNums(findMiddlesInListWithSort(listt))
    printMiddleNums(findMiddlesInListWithoutSort(listt))


if __name__ == "__main__":
    main()
