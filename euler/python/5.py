import itertools as iter

problem = '''
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?.\n
'''
def is_div_to(number, x):
    for i in reversed(range(1, x+1)):
        if number % i != 0:
            return False
    return True

def div_to(x):
    if x < 1:
        return False
    elif x == 1:
        return 1
    else:
        step = div_to(x-1)
        number = 0
        found = False
        while not found:
            number += step
            found = is_div_to(number, x)
        return number
