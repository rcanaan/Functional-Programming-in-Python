




def f(N, shir=[]):
    if N==0:
        return shir
    else:
        return f(N-1, shir +[list(map(chooseWord, ))])
