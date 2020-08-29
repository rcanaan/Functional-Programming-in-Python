#Rinat Canaan 207744012
# shift to the left function
def shiftL(str1, n):
    if n == 0:
        return str1
    elif n:
        str2 = str1[n:]
        str3 = str2
        while n > 0:
            str3 = str(str3) + "0"
            n = n - 1
        return str3
    else:
        return "ERRoR"


# shift to the right function
# def shiftR (str1, n):

# if n==0:
# return str1
# elif n:


# third function
def shiftCL(str1, n):
    if n == 0:
        return str1
    elif n:
        tmp1 = str1[:n]
        tmp2 = str1[n:]
        str2 = tmp2 + tmp1
        return str2
    else:
        return "ERRoR"


# fourth function
def shiftCR(str1, n):
    if n == 0:
        return str1
    elif n:
        tmp1 = str1[:n]
        tmp2 = str1[n:]
        str2 = tmp1 + tmp2
        return str2
    else:
        return "ERRoR"


def main():
    print(shiftL("110001110", 2))
    print(shiftCL("110001110", 2))
    print(shiftCR("110001110", 2))


if __name__ == "__main__":
    main()