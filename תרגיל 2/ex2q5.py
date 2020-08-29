#Rinat Canaan 207744012
#exercise 2 question 5

def m(n):
    return sum(map(lambda i: i/(i+1), range(1,n+1)))#the equation

def helpFunc(n):
    dic = dict(zip(range(1,n+1), [m(i) for i in range(1, n + 1)]))
    [print("the item: ", i, "=", dic[i]) for i in dic.keys()]#using list comprehension


def main():
    n = abs(int(input("Enter a Number: ")))
    print("the sum is: ", m(n), "\n")
    print("helpFunc result: ", "\n",helpFunc(n))

"""     
output:
Enter a Number: >? 3
the sum is:  1.9166666666666665 

the item:  1 = 0.5 
the item:  2 = 1.1666666666666665
the item:  3 = 1.9166666666666665
helpFunc result: """