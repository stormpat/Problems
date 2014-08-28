from random import randint

def get_randoms(n):
  '''return a vector of random integers of size n'''
  accu, vec = 0, []
  while accu < n:
    vec.append(randint(1,9))
    accu += 1
  return vec

def calc(expr):
  '''eval the expression and return conditionally'''
  answ = eval(expr)
  if answ == 24:
    return (True, "Good job! You got: " + str(answ))
  else:
    return (False, "Too bad! You got: " + str(answ) + ", try again!")

def main():
  randoms = get_randoms(4)
  print("\nYour numbers: " + str(randoms))
  print("You can only use the operators: + - * /")
  expr = input("Enter an expression that evaluates to 24.\n")
  if calc(expr)[0] == True:
    print(calc(expr)[1])
  if calc(expr)[0] == False:
    print(calc(expr)[1])
    return main()

main()