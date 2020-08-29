#Rinat Canaan 207744012
#exercise 2 question 6

def pi(n):
    return (4*sum(map(lambda i: ((-1)**(i+1))/(2*i-1) ,range(1, n + 1))))

def helpFunc(n):
    dic = dict(zip(range(1,n+1), [pi(i) for i in range(1, n + 1)]))
    [print("the item: ", i, "=", dic[i]) for i in dic.keys()]#using list comprehension


def main():
    n = abs(int(input("Enter a Number: ")))
    print("the sum is: ", pi(n), "\n", "helpFunc result: ", "\n")
    helpFunc(n)





""" 
    output:
    Enter a Number: >? 4
the sum is:  2.8952380952380956 
helpFunc result:  
the item:  1 = 4.0
the item:  2 = 2.666666666666667
the item:  3 = 3.466666666666667
the item:  4 = 2.8952380952380956
    
    
  """


