## Python sucks at recursion
## Will haveto iterate
## Result: 4613732 (4M) 188 (0.1K)

problem = '''By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms. \n'''

def fib(n):
  if n < 2:
    return 1
  prev = 1
  fib = 1
  for num in range(2, n):
    prev, fib = fib, fib + prev
  return fib

print(problem)
print(fib(10))


