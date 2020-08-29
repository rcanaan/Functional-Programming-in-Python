#Rinat Canaan 207744012
#ex 3 question 3


def reverseNumRecursive(num):
    if len(num) == 0:
        return num
    else:
        return reverseNumRecursive(num[1:]) + num[0]#num[1:0] = forwarding at the string


def main():
  n = int(input("Enter a Number: "))
  num = str(abs(n))
  print("reverseNum1 result: ", reverseNumRecursive(num))

  """
  output:
  Enter a Number: >? 1245
reverseNum1 result:  5421
  """