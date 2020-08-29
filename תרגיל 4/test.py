def f(Seq):
    D = {'a':'T', 't':'A', 'g':'C', 'c':'G'}
    seqOut = []
    for B in Seq:
        if B not in D:
            return []
        else:
            seqOut.append(D[B])
    for i in range(len(seqOut)):
        seqOut[i] = seqOut[i].lower()
    else:
        return ''.join(seqOut)

def dCount(seq1, seq2):
    return dict(map(lambda x: (x, seq1.count(x)), seq2))

def func(L,c,res=[]):
    if L==[]:
      return res
    else:
     return func(L[1:], c, res + [L[0]+c])

def func2(seq):
    return[(i, seq[i]) for i in range(len(seq))]# list comprehension [action for x in L]


def func3(T1,T2):
  D = dict(zip(T1,T2))
  return lambda x : D[x] + '1'

f1 = func3((1,5,10),('a','b','c'))

from functools import reduce

def dCount(s1,s2):
    return sum([1 for i in range(0,len(s1)) if s2==s1[i:i+len(s2)]])


def triangle(x):
    tuple1=(x,x*(x+1)/2)
    return tuple1


def m(n):
    return list(map(lambda i: (i*(i+1))/2, range(1,n+1)))#the equation

def helpFunc(n):
    dic = dict(zip(range(1,n+1), [m(i) for i in range(1, n + 1)]))
    return dic


def triangle1(n,i=1):
    if i==n:
     return []
    return [(i,i*(i+1)/2)]+triangle1(n,i+1)
def tri(n):
    def prod(L):
        if L==[]:
            return 1
        return L[0][1]*prod(L[1:])

    return prod(triangle1(n))

def fur(x):
    return (x, x*2, x*3,x*5)

def hammimngTuple(x):
    return tuple([fur(i) for i in range(1,x+1)])

def hammingLst(L):
    lst = [j for i in L for j in i]
    lst1 = list(map(lambda x,y: x+y,[j for i in L for j in i],[1,2,3]))
    return list(set(lst))

def hammingSum(x):
    #a = hammimngTuple(x)
    #b = hammingLst(a)
    #return sum(b)
     return sum(hammingLst(hammimngTuple(x)))

def subseq(L1,L):
    def helper(L1,L,lenL1,L1Original):
         if (L==[]):
            return False
         if (L1==[]):
              return True
         if (L1[0]==L[0]):
            return helper(L1[1:],L[1:],lenL1,L1Original)
         if (L1[0]!=L[0] and lenL1 != len(L1)):
             return helper(L1Original, L[1:], lenL1,L1Original)
         return helper(L1,L[1:],lenL1,L1Original)

    return helper(L1,L,len(L1),L1)



def subseqcount(L1,L):
    def helper(L1,L,lenL1,L1Original,counter=0):
         if (L1==[]):
             print(f"L: {L}, counter: {counter+1}")
             return helper(L1Original, L[1:], lenL1, L1Original, counter+1)
         if (L == []):
             if (len(L1)==lenL1):
                 return counter+1
             return counter

         if (L1[0]==L[0]):
             return helper(L1[1:],L[1:],lenL1,L1Original,counter)
         if (L1[0]!=L[0] and lenL1 != len(L1)):
             return helper(L1Original, L[1:], lenL1,L1Original,counter)

         return helper(L1,L[1:],lenL1,L1Original,counter)

    return helper(L1,L,len(L1),L1)



from functools import reduce
def g(x,y):
 if len(x) >= len(y) :
    return x
 else:
    return y

def ffff(L):
 mx=reduce(g, filter((lambda x : isinstance(x,str)), L))
 return mx




def removeCar(L,NumOfCar):
    if (L==[]):#for safety!
        return []
    return list([i for i in L if i[0]!=NumOfCar])#using the principle of filter
    #return list(filter(lambda x: x[0]!= NumOfCar, L))#using the pattern desing of filter itself

def totalTime(L):
    if(L==[]):
        return 0
    #return sum([i[2]  for i in L ])#will return the time
    return reduce(lambda x,y: x+y ,list(map(lambda z: z[2] ,L)) )

from functools import reduce
def rt():
    print(reduce(lambda x,y:x+y, [[x,] for x in range (1,10,3)]))

#([(1),(4)(7)]
#

def ff1(N):
    p = lambda x : x**2 + x +3
    def ff2(N):
        if N ==0:
            return [p(N)]
        else:
            return ff2(N-1) + [p(N)]
    return ff2(N)
print ((x for x in ff1(5)))


def f4(L):
    def f2():
        return dict(zip(range(len(L)),L))
    return f2()

def funccc(L):
    while(L==[]):
        print('a')
    else:
        print ('c')





















