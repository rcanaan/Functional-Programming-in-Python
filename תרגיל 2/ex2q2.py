#Rinat Canaan 207744012
#exercise 2 question 2


def sumDigits1_Helper(n):
    if n < 0:
        n *= (-1)

    digitList = []
    while n > 0:
        digitList.append(n % 10)
        n = int(n / 10)
    return digitList

def sumDigits1(digitList):
    return sum(digitList)


def sumDigits2_Helper(n):
    if n < 0:
        n *= (-1)
    nInString = str(n)
    digitList = [int(nInString[val]) for val in range(0, len(nInString))]

    return digitList


def sumDigits2(digitList):
    return sum(digitList)


def main():
    number = eval(input("enter number:"))
    if (number, int):
        print ("sumdigits1 result: ", sumDigits1(sumDigits1_Helper(number)))#print the absolute
        print("sumdigits2 result: ", sumDigits2(sumDigits2_Helper(number)))  # print the absolute

#output:
#enter number:>? 12345
#sumdigits1 result:  15
#sumdigits2 result:  15