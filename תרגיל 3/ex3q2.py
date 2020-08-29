#Rinat canaan 207744012
#ex 3 question 2

def sumDigits1_Helper(n):
    if n == 0:
        return 0
    else:
        # Mod (%) by 10 gives you the rightmost digit (227 % 10 == 7),
        # while doing integer division by 10 removes the rightmost
        # digit (227 // 10 is 22)

        return (n % 10) + sumDigits1_Helper(n // 10)

def main():
    number = eval(input("enter number:"))
    if (number, int):
        print ("sumdigits1 result: ", sumDigits1_Helper(number))#print the absolute