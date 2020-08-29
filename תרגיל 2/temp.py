# section A of Question 2
def digitListFuncA(n):
    if n < 0:
        n *= (-1)

    digitList = []
    while n > 0:
        digitList.append(n % 10)
        n = int(n / 10)
    return digitList


# section  B of Question 2
def digitListFuncB(n):
    if n < 0:
        n *= (-1)
    nInString = str(n)
    digitList = [int(nInString[val]) for val in range(0, len(nInString))]

    return digitList


# for both A,B sections of question 2
def sumDigits(digitList):
    return sum(digitList)


# for section Cin Question 2
def main():
    n = int(input("Enter a Number: "))

    print(sumDigits(digitListFuncA(n)))
    print(sumDigits(digitListFuncB(n)))


if _name_ == "_main_":
    main()

# Output:
# Enter a Number: 321
# 6
# 6