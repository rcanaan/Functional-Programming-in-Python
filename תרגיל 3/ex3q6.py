#Rinat Canaan 207744012
#exercise 3 question 6

def pi(n):
    if n == 1:
        return n
    else:
        return pi(n-1) + ((pow(-1, n+1))/(2*n-1))#the equation
    #return (4*sum(map(lambda i: ((-1)**(i+1))/(2*i-1) ,range(1, n + 1))))

def helpFunc(n):
    return pi(n)*4


def main():
    n = abs(int(input("Enter a Number: ")))
    print("the sum is: ", str(helpFunc(n)))


