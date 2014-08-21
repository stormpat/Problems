problem = '''Find the sum of all the multiples of 3 or 5 below 1000. \n'''

# With nested func
def w_nested(limit):
  def criteria(n):
    return n % 3 == 0 or n % 5 == 0
  return sum(list(filter(criteria, range(1, limit))))

# With lambda
def w_lambda(limit):
  return sum(list(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(1, limit))))

print(problem)
print(w_nested(1000))
print(w_lambda(1000))
