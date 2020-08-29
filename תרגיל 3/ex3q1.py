#Rinat Canaan 207744012
#ex 3 question 1

#question 1 a
def pentaNumRange(n1,n2):
    getPentaNum = lambda n: (n*(3*n - 1))/2
    numList = []
    def recursive(k):#for each n
        if k == n2:
            return
        else:
            numList.append(getPentaNum(k))#adding to the list
            recursive(k + 1)#going to the next item
        return numList
    return recursive(n1)


    #return [getPentaNum(n) for n in range(n1,n2)] #using list comprehension

def toString(i , val):
    if i%10 == 0:
        return '\n' + str(val)
    else:
        return ' ' + str(val)

def printPentaNum():
    n1  =int(input(("please enter n1")))
    n2 = int(input("please enter n2"))
    l = pentaNumRange(n1, n2)# a list of PenteNumbers
    #print(toString2(l))
    lprint = [toString(i, val) for i,val in enumerate(l)] #using list comprehension
    print("".join(lprint))

def main():
 printPentaNum()

 if __name__ == "__main__":
        main()
#output:
# pentaNumRange(1,10)
#[1.0, 5.0, 12.0, 22.0, 35.0, 51.0, 70.0, 92.0, 117.0]