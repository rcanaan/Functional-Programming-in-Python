#Rinat Canaan 207744012
#first question
def func(a,b,c):
    if (a+b > c) and (b+c > a) and (a+c > b):
        return True

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if func(a, b, c) == True:
    print("they are correct triangle length")
else:
    print("they are in error.")