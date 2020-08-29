#Rinat Canaan 207744012
#exercise 2 question 8

def add3dicts(d1, d2, d3):
    def val(d, key):
        if key in d:
            return d[key]
        else:
            return None

    def values(key):
        res = tuple(filter(lambda x: x != None, map(lambda dct: val(dct, key), [d1, d2, d3])))
        if len(res) == 1:
            return res[0]
        else:
            return res

    keys = set(d1) | set(d2) | set(d3)
    vals = map(values, keys)
    return dict(zip(keys, vals))


def main():
    d1 = {1: 'a', 3: 'd', 5: 'e'}
    d2 = {1: 'b', 3: (11, 22), 7: 'f', 4: 'q'}
    d3 = {2: 'c', 3: 'x', 4: 't', 8: 'g'}

    print(add3dicts(d1, d2, d3))


if __name__ == "__main__":
    main()


"""
output:

main()
{1: ('a', 'b'), 2: 'c', 3: ('d', (11, 22), 'x'), 4: ('q', 't'), 5: 'e', 7: 'f', 8: 'g'}
"""