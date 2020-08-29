#Rinat Canaan 207744012
#exercise 2 question 4

def isPolindrom(n):
    s = str(n)
    return s == s[::-1]


def main():
    n = abs(int(input("Enter a Number: ")))
    ans = isPolindrom(n)
    if (ans):
        print("it is a polindrom!!")
    else:
        print("it is not a polindrom")