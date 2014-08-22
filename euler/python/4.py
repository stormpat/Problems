
problem = '''Find the largest palindrome made from the product of two 3-digit numbers.\n'''

def palindrome():
  return max(a * b for a in range(1,1000) for b in range(a,1000) if str(a * b) == str(a * b)[::-1])

print(problem)
print(palindrome())
