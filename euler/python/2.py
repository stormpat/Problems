
problem = '''By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms. \n'''

def fib(limit):
  evens, a, b = 0, 1, 2
  while b < limit:
    if b % 2 == 0:
      evens += b
    a, b = b, a + b
  return evens

print(problem)
print(fib(4000000))
