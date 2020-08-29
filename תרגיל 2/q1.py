#Rinat Canaan 207744012
#exercise 2 question 1

#question 1 a
def pentaNumRange(n1,n2):
    getPentaNum = lambda n: (n*(3*n - 1))/2
    return [getPentaNum(n) for n in range(n1,n2)] #using list comprehension

#output:
# pentaNumRange(1,10)
#[1.0, 5.0, 12.0, 22.0, 35.0, 51.0, 70.0, 92.0, 117.0]

#question 1 b
def toString(i , val):
    if i%10 == 0:
        return '\n' + str(val)
    else:
        return ' ' + str(val)

def toString2(l):
    count = 0
    for w in l:
        count = count + 1
        if count == 10:
            return ('\n' + str(w))
        else:
            return str(w)


def printPentaNum():
    n1  =int(input(("please enter n1")))
    n2 = int(input("please enter n2"))
    l = pentaNumRange(n1, n2)# a list of PenteNumbers
    #print(toString2(l))
    lprint = [toString(i, val) for i,val in enumerate(l)] #using list comprehension
    print("".join(lprint))




#output:
#printPentaNum()
#please enter n1>? 1
#please enter n2>? 100
#with list comprehension
#1.0 5.0 12.0 22.0 35.0 51.0 70.0 92.0 117.0 145.0
#176.0 210.0 247.0 287.0 330.0 376.0 425.0 477.0 532.0 590.0
#651.0 715.0 782.0 852.0 925.0 1001.0 1080.0 1162.0 1247.0 1335.0
#1426.0 1520.0 1617.0 1717.0 1820.0 1926.0 2035.0 2147.0 2262.0 2380.0
#2501.0 2625.0 2752.0 2882.0 3015.0 3151.0 3290.0 3432.0 3577.0 3725.0
#3876.0 4030.0 4187.0 4347.0 4510.0 4676.0 4845.0 5017.0 5192.0 5370.0
#5551.0 5735.0 5922.0 6112.0 6305.0 6501.0 6700.0 6902.0 7107.0 7315.0
#7526.0 7740.0 7957.0 8177.0 8400.0 8626.0 8855.0 9087.0 9322.0 9560.0
#9801.0 10045.0 10292.0 10542.0 10795.0 11051.0 11310.0 11572.0 11837.0 12105.0
#12376.0 12650.0 12927.0 13207.0 13490.0 13776.0 14065.0 14357.0 14652.0

