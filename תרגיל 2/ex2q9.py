#Rinat Canaan 207744012
#ex2 question 9
from q1 import *
from ex2q3 import *
from ex2q2 import *
from ex2q4 import *
from ex2q5 import *
from ex2q6 import *
from ex2q7 import *
from ex2q8 import *


f1 = q1.printPentaNumbers
f2 = ex2q2.main
f3 = ex2q3.main
f4 = ex2q4.main
f5 = ex2q5.main
f6 = ex2q6.main
f7 = ex2q7.main
f8 = ex2q8.main

QuestDict = {0: "have a nice day", 1: f1, 2: f2, 3: f3, 4: f4, 5: f5, 6: f6, 7: f7, 8: f8}


def main():
    x = int(input("please enter a number from 0-8: "))
    if x == 0:
        print(QuestDict[0]())
        SystemExit()

    while x != 0:
        if 0 < x and x < 9:
            QuestDict[x]()
        else:
            print("the number you have choosen is invalid, please enter again")

        x = int(input("please enter a number from 0-8: "))


if __name__ == "__main__":
    main()
