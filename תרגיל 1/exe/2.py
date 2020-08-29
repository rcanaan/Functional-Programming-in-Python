#Rinat Canaan 207744012
import math


#
# Area calculation program
def rectangleArea(w, h): #rectangle
    return w * h

def circleArea(r): #circle
    return math.pi * r ** 2

def sphereArea(r): #sphere
    return (4 / 3) * math.pi * r ** 3

def coneArea(s, height):#cone
    return s * height * (1 / 3)

def squarePyramidArea(s, height):#square pyramid
    return s * height * (1 / 3)

# printing the menu options
def prtMenu(shapes):
    for i in range(len(shapes)):
        print(i + 1, shapes[i])
    return

# main program
#
def main():
    print("Welcome to the Area calculation program")
    print("---------------------------------------\n")
    # Print out the menu
    shapes = ("Rectangle", "Circle", "sphere", "cone", "square pyramid")
    while True:
        print("\nPlease select a shape (press 0 to quit):")
        prtMenu(shapes)
        # Get the user's choice:
        shape = input("> ")
        # Calculate the area:
        if shape == "1":
            height = float(input("Please enter the height: "))
            width = float(input("Please enter the width: "))
            area = rectangleArea(width, height)
            print("The area is", area)
            continue

        elif shape == "2":
            radius = float(input("Please enter the radius: "))
            area = circleArea(radius)
            print("The area is", area)
            continue

        elif shape == "3":
            radius = float(input("Please enter the radius: "))
            area = sphereArea(radius)
            print("The area is", area)
            continue

        elif shape == "4":
            radius = float(input("Please enter the radius: "))
            height = float(input("Please enter the height: "))
            s = circleArea(radius)
            area = coneArea(s, height)
            print("The area is", area)
            continue

        elif shape == "5":
            height = float(input("Please enter the height: "))
            s = float(input("Please enter the base area: "))
            area = squarePyramidArea(s, height)
            print("The area is", area)
            continue
        elif shape == "0":
            print("Bye!")
            break
        else:
            print("Invalid shape")


if __name__ == "__main__":#calling to the main func to work first
    main()
##example of output:
#Please select a shape (press 0 to quit):
#1 Rectangle
#2 Circle
#3 sphere
#4 cone
#5 square pyramid
#> 2
#Please enter the radius: 5
#The area is 78.53981633974483

#Please select a shape (press 0 to quit):
#1 Rectangle
#2 Circle
#3 sphere
#4 cone
#5 square pyramid
#> 1
#Please enter the height: 2
#Please enter the width: 3
#The area is 6.0

#Please select a shape (press 0 to quit):
#1 Rectangle
#2 Circle
#3 sphere
#4 cone
#5 square pyramid
#> 4
#lease enter the radius: 4
#Please enter the height: 5
#The area is 83.7758040957278