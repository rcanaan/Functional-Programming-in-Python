#Rinat Canaan 207744012
#exercise 2 question 3

#func from q2 to 3.b
def sumDigits1_Helper(n):
    if n < 0:
        n *= (-1)

    digitList = []
    while n > 0:
        digitList.append(n % 10)
        n = int(n / 10)
    return digitList

def reverseNum1(n):
    num = str(abs(n))
    numReversed = num[::-1]
    return numReversed

def reverseNum2(n):
   return sumDigits1_Helper(n)

def main():
  n = int(input("Enter a Number: "))
  print("reverseNum1 result: ", reverseNum1(n))
  print("reverseNum2 result: ", reverseNum2(n))

#output:
#Enter a Number: >? 1234
#reverseNum1 result:  4321
#reverseNum2 result:  4 ,3 ,2 ,1