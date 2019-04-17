"""
iterative approach with a stack to convert a base 10 integer number to a different base

"""

stack = []

def to_str(n,base):
    convert_string = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            stack.append(convert_string[n])
        else:
            stack.append(convert_string[n % base])
        n = n // base
    res = ''
    while stack:
        res = res + str(stack.pop())
    return res

print(to_str(1453,16))