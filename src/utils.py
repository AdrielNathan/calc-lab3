def add(n1, n2):
    return n1 + n2

def add_with_args(*args):
    sum = 0
    for n in sum :
        sum += n
    return sum

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2

def exponent(base, power):
    return base ** power
