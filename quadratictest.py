import math

def quadratic(a, b, c):
    x1 = 0
    x2 = 0
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type params %s' % str(a))
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type params %s' % str(b))
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type params %s' % str(c))    
    return x1, x2
print(quadratic('l','b','c'))
