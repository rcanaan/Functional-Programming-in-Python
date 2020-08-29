#Rinat Canaan 207744012
#ex 3 question 5



def m(n):
   f = lambda i: i/(i+1) #the wanted equation

   def recursiveSumFunc(k):
       if k == 0:
           return 0
       else:
          return recursiveSumFunc(k - 1) + f(k)
   return recursiveSumFunc(n)


def main():
    n = abs(int(input("Enter a Number: ")))
    print("the sum is: ", m(n), "\n")


"""     
output:
Enter a Number: >? 3
the sum is:  1.9166666666666665 

the item:  1 = 0.5 
the item:  2 = 1.1666666666666665
the item:  3 = 1.9166666666666665
helpFunc result: """