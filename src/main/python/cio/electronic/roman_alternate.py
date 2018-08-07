symbols = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
## 4 and 9 is imp
def checkio(data):
    #replace this for solution
    res =''
    for val,key in symbols:
        while val<=data:
            data = data-val
            res += ''.join(key)
    print(res)
    return res