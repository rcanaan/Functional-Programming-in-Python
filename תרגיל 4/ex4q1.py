#rinat canaan 207744012
#exercise 4 question 1

from Targil4input import hujiMarks, teacherName
import statistics as stat

def my_stdev(inputData):
    if len(inputData) == 1:
        return 0.0
    return stat.stdev(inputData)

def my_mean_and_stdev(inputData):
    if len(inputData) == 0:
        return ()
    return (stat.mean(inputData),my_stdev(inputData))

def myStudList(list1,list2):

    def my_myStudList(list1,list2,Acc=[]):
        if not list2:
            return Acc, stat.mean([elem[1] for elem in list1]), my_stdev([elem[1] for elem in list1])
        return my_myStudList(list1,list2[1:], \
                             Acc + [[list2[0][0],[[elem[0] for elem in list1 if elem[2] == list2[0][1]], \
                                                  my_mean_and_stdev([elem[1] for elem in list1 if elem[2] == list2[0][1]])]]])

    return my_myStudList(list1,list2)


def myStudDict(inputData):

    def my_myStudDict(inputData,Acc = dict([])):
        if not inputData:
            return Acc
        return my_myStudDict(inputData[1:],dict(list(Acc.items()) + [(inputData[0][0],inputData[0][1][0]+[inputData[0][1][1]])]))

    return my_myStudDict(inputData)

def recursivePrint(inputData):
    if isinstance(inputData,list) and inputData:
        print(inputData[0])
        recursivePrint(inputData[1:])

def question1():

    def my_main(L,avr,stdev):
        recursivePrint(L)
        print("maen = " + str(avr))
        print("stdev = " + str(stdev))

    my_main(*myStudList(hujiMarks,teacherName))
