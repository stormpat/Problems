
problem = '''What is the largest prime factor of the number 600851475143 ? \n'''

def factorize(number):
  vector = []
  i, n = 2, number
  while (i * i) <= n:
    if n % i == 0:
      vector.append(i)
      n = n / i
    else:
      i += 1
  if n != 1:
    vector.append(n)
  return vector


# Result => 6857
print(problem)
print(max(factorize(600851475143)))
